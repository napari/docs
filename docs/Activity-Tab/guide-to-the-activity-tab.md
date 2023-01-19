# Guide to the Activity Tab

## Draft for Review
## Overview
The activity tab shows the installation statistics for a particular plugin, including: 
* How many times the plugin has been installed since it was released
* How many times the plugin has been installed in the past 30 days  
* Installs of the plugin in the past year are graphed

## Installs
We aim to represent plugin installations from plugin users, excluding those done by plugin developers or for non-user purposes, but there are many caveats. For example, since the installation data we utilize is anonymous, we may show multiple installs from a single user. 

We use the [Linehaul project](https://github.com/pypa/linehaul-cloud-function/) to gather install data, which is the same tool used by [PyPI](https://pypi.org/). Linehaul shows all installs, including developer installs used for troubleshooting or building the package. The developer installs can fall into multiple buckets including continuous integration (CI), [mirror installs](https://pypi.org/project/bandersnatch/), and [release candidate installs](https://en.wikipedia.org/wiki/Software_release_life_cycle#Release_candidate). PyPI shows all installs. You can view install data from PyPI at [pypistats.org](https://pypistats.org/). 

We select for installs made by plugin users and exclude as many developer installs as possible. We clean the install data from Linehaul by excluding CI installs such as those from AWS (Amazon Web Services), mirror installs, and release candidate installs. Our data may not match pypi stats due to this data exclusion. (e.g. napari-allencell-segmenter on [the hub](https://www.napari-hub.org/plugins/napari-allencell-segmenter) vs napari-allencell-segmenter [on pypi](https://pypistats.org/packages/napari-allencell-segmenter)).

## Install data graphs 
* We show the past 12 completed months from the previous month to the current month. So if it’s December 2022, we show December 2021 through November 2022 as in this example:  

    ![](.\Images\1220-installs.png)  

* The dashed line indicating “Public release” aligns with the month it was publicly released, as shown in this example:

   ![](.\Images\74-installs.png)

* The data for the first month of the plugin’s public existence may not be for a complete month if the plugin was released at any date after the first of the month. We still show what data we had for that month in aggregate once that month is complete and we are in the next month. In this example, the plugin was released more than one month ago but not two months ago. It shows one install in the past 30 days, which may not be all the installs for the current month.   

  ![](.\Images\7-installs.png)

* Graphs are not displayed if a plugin was released in the current month.  
![](.\Images\no-graph.png)

## Terminology used to describe installs 
* If a plugin was publicly released < 7 days ago, we say “**less than a week ago**”.
* If a plugin was publicly released >= 7 days, but < 14 days prior, we say "**a week ago**".
* If a plugin was publicly released >= 14 days, but < 30 days prior, we say "**n weeks ago**". e.g., “3 weeks ago”
* If a plugin was publicly released >=  30 days, but < 24 months prior, we say "**n months ago**". e.g., “7 months ago” or “19 months ago”
* If a plugin was publicly released > 24 months prior, we say "**n years ago**". 
e.g., "2 years ago" or “6 years ago”
 
## Future 

### How we source citation information 

#### We pull from a variety of data sources to monitor the napari ecosystem’s short-term progress and impact such as:
* Python Package Index 
* Twitter
* GitHub
* ImageSC
* Plausible

#### For long term impacts we look at:
* Cold Spring Harbor Laboratory
* BioRxiv
* MedRxiv
* Europe PMC
* Semantic Scholar
* CZ KG
* CZ Software Mentions Dataset
* arXiv

For more detailed information on sources, see [this presentation](https://docs.google.com/presentation/d/1S-oAEDTxub0hWKvONFuPEhawYNsoglpJCcGE8oaZByI/edit#slide=id.g19615f5848d_0_11).

### Other GitHub metrics that we may surface:  
 
#### Maintenance statistics:
* Commits since released     
* Commits since plugin repo was created  
* The time of the latest commit  
* Monthly commits in past year  

#### Citations:
* Literature mentions  
* Formal citations
* Top citations, which are the most highly cited papers among the papers that cite the plugin
* Most recent citations
* Top research fields citing the plugin, which is the aggregate of the fields of papers citing the plugin

## Supporting Info
* Planning and copy for [this wiki](https://github.com/chanzuckerberg/napari-hub/wiki/Guide-to-Activity-Tab)  
* Design mockup of activity tab with [citation information tab](https://www.figma.com/proto/d3t84J9Uzmj0GZnYROzdQX/Activity-Dashboard?page-id=2175%3A7860&node-id=2196%3A15129&viewport=-458%2C4607%2C0.25&scaling=min-zoom&starting-point-node-id=2196%3A15129&show-proto-sidebar=1)  
* [Chart treatment of plugins of various ages](https://www.figma.com/file/d3t84J9Uzmj0GZnYROzdQX/Activity-Dashboard?node-id=1356%3A2443&t=96sNUeclbGDJQbYT-0)
* Citation gathering [information](https://docs.google.com/presentation/d/1S-oAEDTxub0hWKvONFuPEhawYNsoglpJCcGE8oaZByI/edit#slide=id.gf6b05418ce_0_218)
* Data collection comes from python and other sources.  
* Python uses the Linehaul project.  
* Other sources of data are mentioned [here.](https://docs.google.com/document/d/1ooKjIVnydgYTaYwWczKTCVlNwlSrT1StITC6T8Pyogw/edit#bookmark=id.6tsxxcbygci)














































































