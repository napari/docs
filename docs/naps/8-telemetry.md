:orphan: 
  
 (nap-8)= 
  
 # NAP-8 — Telemetry
  
 ```{eval-rst} 
 :Author: Grzegorz Bokota 
 :Created: <date created on, in yyyy-mm-dd format> 
 :Resolution: <url> (required for Accepted | Rejected | Withdrawn) 
 :Resolved: <date resolved, in yyyy-mm-dd format> 
 :Status: Draft
 :Type: Standards Track 
 :Version effective: <version-number> (for accepted NAPs) 
 ``` 
  
 ## Abstract 
  
 This NAP is describing why Telemetry is helpful to the Napari project and describes the architecture and solutions selected to maximize the privacy of our users. 
 
 ## Motivation and Scope

With the growth of napari, the standard feedback loop through napari community meetings and napari-related events at conferences has reached its capacity. Also, we collect many feature requests for which we cannot find volunteers for implementation. 

To have the possibility of sustainable development of the project we need either have funds to pay contractors or have some company that donates their worker times manageable by core-devs.

Both these scenarios require our side the ability to provide some information about the estimated number of users to prove to potential founders that their donation/grant will be used in a valuable way. 

Adding the option for monitoring plugin usage allows us to identify the most important plugins and try to establish cooperation with their maintainers to reduce the probability that the plugin will not be ready for a new release. Such monitoring could contain not only the list of installed plugins but also which commands contributions are used most often.

Also collecting information about data types and their size will provide valuable information about the typical use cases of napari.

Still, a user need to be able to opt out of such monitoring. And adjust the level of detail of the information that is sent to the napari server.
 
  
 ## Detailed Description

`napari-telemetry` will be a package responsible for collecting and sending telemetry data to the napari server. It will be installed after user confirmation. It will contain callbacks for collection data, and utils for its storage and sending. Also, this package will contain utils for validation if the user has agreed to telemetry. 

In the main package, there is a need to add code to ask users if they want to enable telemetry. This 1code should be executed only once per environment.

Telemetry should contain following way to disable it:

1. uninstall `napari-telemetry` package
2. Environment variable `NAPARI_TELEMETRY=0`
3. Full list of endpoints used for collecting telemetry, that could be filtered on the firewall level.

The user should be able to adjust the telemetry level of detail. The following levels are proposed:

1. `none` - no telemetry is collected
2. `basic` - information about the napari version, python version, OS, and CPU architecture is collected and if it is the first report by the user. There is also a user identifier created based on computer details that will be rerendered each week to prevent tracking the user, but allow to not count a user multiple times. 
3. `middle` - same as in `basic` but also information about the list of installed plugins and their versions is collected. We take care to not collect data about plugins that are not indented to be public. 
4. `full` - same as in `middle` but also information about plugin usage by binding to app-model and collect information about called plugins command. Also basic information about data like type (`np.ndarray`, `dask.array`, `zarr.Array`, etc.) and its size is collected.

There should be a visible indicator that telemetry is enabled (for example on the status bar). 

The second part of this work should be setup the server to collect telemetry data. Next to collecting data, it should provide a basic public dashboard that will allow a community to see aggregated information.

I propose to have the following data retention policy:

1) Up to 2 weeks for logs.
2) up 2 months of raw data (1 month of collection, then aggregation and time to validate aggregated data),
3) infinite of aggregated data.
  
## Privacy assessment

During the preparation of this NAP we assume that none of the collected data will be presented in 
a form that allows to identify a single user or identify a research area of user. We also select a set of data that will be collected to minimize the possibility of reval of fragile data, but it is impossible to guarantee that it will not be possible to identify a single user (for example checking plugins combination).

Because of this, we decided to not publish raw data and only show aggregated results. The aggregation will be performed using scripts. Napari core-devs will access raw data only when there will be some errors in the aggregation process.

We also will publish a list of endpoints for each level of telemetry, so the given level of telemetry could be blocked on the organization level (for example by the rule on the firewall).


If someone found that we are publishing some problematic data we will remove them and update the aggregation process to prevent such a situation in the future.
This NAP will be updated to reflect the current state of telemetry. 

 
## Related Work 

Total systems:
https://plausible.io/
https://sentry.io/
https://opentelemetry.io/

Visualizations:
https://github.com/grafana/grafana
  

  
## Implementation 

The main thing for implementation should be the low cost of maintenance. So the solution should be as simple as possible. We could either use existing solutions on the server side or implement our own.

The benefit of the existing solution is that most of the work is already done. The downside is that it may require additional cost of maintenance. This cost may be caused by many features that are not needed for napari and could increase the risk of leaking data.  As I check they are implemented in techniques that are not familiar to napari core-devs. So if there will be a decision to use them we should select an SAS solution that will be maintained by the company.


For the current, I suggest creating a simple REST API server for collecting the data. 
It could be a simple Python FastAPI server that will store data in the SQLite database.

Data for aggregation should be extracted from the database using a script running on the same machine.

The output of the aggregation script should be loaded to some existing visualization tool, like grafana.

It may be nice to host them on separate servers, then even if the data presented on the dashboard will be compromised, the raw data will be not exposed to the world.

Having both server and aggregation scripts in Python will reduce maintenance costs for napari core-devs.

We should register the `telemetry.napari.org` domain and use it for the server. The main page contains this NAP and a link to the summary dashboard.


The main part of the application side should be implemented in `napari-telemetry` package. 
The package should not report in stream mode, but collect data on the disk and send it in batches. This will reduce the risk of leaking data. The package should implement a utility to allow users to preview collected data before sending it to the server.

In the napari itself following changes should be implemented:

1) The indicator that shows the telemetry status
2) The dialog that asks a user if they want to enable telemetry
3) code to check if telemetry is enabled (to not load the `napari-telemetry` package if it is disabled)
4) code required to init `napari-telemetry` package


## Potential problems 

There is a risk that someone may try to highjack the telemetry module name to have code executed at every napari start. 

I do not expect that it is a high risk, but exists. We could address it by code signing. This will require additional procedures to protect private cryptographic keys.

Another option is to scan public plugins and their dependencies. This is simpler but will require establishing additional communication channels to be able to warn users about the potential problem. 


  
## Backward Compatibility 
  
 Not relevant
  
## Future Work 

A nice extension may be the ability for the steering council to create a certificate of telemetry output that could be given to plugin maintainers to prove to supervisors that their plugin is used by the community. 

  
 ## Alternatives 

 During the discussion, there is a proposal to use the same approach as used in ImageJ. 
 
 Mean that instead of implementing telemetry on the client side we could implement it on the update server side. The advantage and disadvantage of such a solution is that no user could opt out of telemetry. Also, such a method could potentially provide information about the Python version, napari version and list of installed plugins. All others will require a mechanism from this NAP.

 It will also require updates on the Napari side as currently we only communicate with the update server when a user opens the plugin manager. Also, to have proper information about installed plugins we will need to send information about the list of installed plugins instead of just downloading the information about all plugins from the server. 

 As this solution provides less information, does not allow for opt-out and could cause blacklisting of the update server IP address, I do not recommend it.

 But based on talks that happen during the discussion we may think about more frequent checks for updates to inform users that they could update their Napari or plugin version. For such a change we need to update our update server to provide information per Python version (as some plugins could drop old Python earlier).


The second alternative is use a third-party solution like [plausable.io](https://plausible.io/). But from my perspective, it is harder to adjust a set of data that is collected as these services are designed to monitor webpages. 

  
 ## Discussion 
  
 This section may just be a bullet list including links to any discussions 
 regarding the NAP, but could also contain additional comments about that 
 discussion: 
  
 - This includes links to discussion forum threads or relevant GitHub discussions. 
  
 ## References and Footnotes 
  
 All NAPs should be declared as dedicated to the public domain with the CC0 
 license [^id3], as in `Copyright`, below, with attribution encouraged with 
 CC0+BY [^id4]. 
  
 [^id3]: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication, 
     <https://creativecommons.org/publicdomain/zero/1.0/> 
  
 [^id4]: <https://dancohen.org/2013/11/26/cc0-by/> 
  
 ## Copyright 
  
 This document is dedicated to the public domain with the Creative Commons CC0 
 license [^id3]. Attribution to this source is encouraged where appropriate, as per 
 CC0+BY [^id4].