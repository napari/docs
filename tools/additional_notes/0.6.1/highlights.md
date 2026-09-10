### The HiLo👋 Colormap!

Introducing the HiLo colormap to napari! 🎨 This much-loved colormap (LUT) is like grayscale, except it displays values at or above the maximum contrast limit as red 🔴 and values at or below the minimum contrast limit as blue 🔵. In the scientific imaging world, the HiLo colormap is often used to assess overexposed (saturated) ☀️ and underexposed (dark) 🌑 regions in images.
Enjoy this animation of the HiLo colormap in action! 👇
![HiLo colormap animation](https://github.com/user-attachments/assets/b77e98b4-3f9c-437a-b169-2444544ee454)

The HiLo colormap is now available as a result of the dependency bump to VisPy 0.15.0 [(#7846)](https://github.com/napari/napari/pull/7846), which will soon unlock even more great new features in the coming napari releases.

### The `dims` widget shines brighter! ✨

Have you ever tried to use the `dims` pop-up widget (accessed by right clicking on the third viewer button) and found it to not work as expected? As part of our bugfixes [#7937](https://github.com/napari/napari/pull/7937) , the `dims` widget will continue to interact as expected. The widget is now available in 3D view!
❓Did you know that the `dims` widget allows you to rename the axis labels of your data?
![dims popup widget](https://github.com/user-attachments/assets/3b38462b-8fe2-47b2-be02-66a714d18d8f)
