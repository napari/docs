(how-to-build-a-plugin)=
# Building a plugin

Plugins allow developers to customize and extend napari.  This includes

- Adding file format support with [readers] and [writers]
- Adding custom [widgets] and user interface elements
- Providing [sample data][sample_data]
- Changing the look of napari with a color [theme]

If you're just getting started with napari plugins, try our
[Your First Plugin](../building_a_plugin/first_plugin) tutorial.

For a list of all available contribution points and specifications,
see the [Contributions reference](../technical_references/contributions)

If you're ready to publish your plugin, see [Test and deploy](../testing_and_publishing/test_deploy)

For special considerations when building a napari plugin, see
{ref}`best-practices`.

```{admonition} Introducing npe2
:class: important

We introduced a new plugin engine [`npe2`][npe2] in December 2021.

Unless otherwise stated, most of the documentation herein pertains
to the new npe2 format (which uses a static `napari.yaml` manifest)

Plugins targeting the first generation `napari-plugin-engine` 
(using `@napari_hook_implementation` decorators, see [npe1]) will
continue to work for at least the first half of 2022, but we
recommend migrating to `npe2`. See the
[migration guide](npe2-migration-guide) for details.
```

[npe1]: https://github.com/napari/napari-plugin-engine
[npe2]: https://github.com/napari/npe2
[readers]: contributions-readers
[writers]: contributions-writers
[widgets]: contributions-widgets
[sample_data]: contributions-sample-data
[theme]: contributions-themes