The sequence of events to draw a polygon or path are almost the same 
when using either the mouse or a tablet.

<ins>Drawing with mouse</ins>

1. Click mouse (left-click) to begin drawing.
2. Move mouse -- without holding down the mouse button -- to draw the path.
3. Click mouse (left-click) or press `Esc` to end drawing the path or polygon.
   In case of drawing a polygon the polygon will be automatically completed.


<ins>Drawing with tablet</ins>

The polygon lasso and the path tool can also be used to draw `Polygons` or `Paths` 
using a tablet. In this case, drawing the polygon or path is started by touching 
the tablet screen with the tablet stylus and drawing will continue for as long 
as the pencil is moved while touching the tablet screen. Note that similar behavior 
is also available when using a macOS trackpad, using three-finger drag mode.

<ins>Adding of vertices while drawing</ins>

For both mouse and tablet mode, vertices are added only if the vertex to be added 
is at a certain number of screen pixels away from the previous vertex. This value 
can be adjusted in the settings in napari by going to `File` -> `Preferences` (or
`control + shift + p`), then in the menu on the left-clicking on `Experimental` 
and then adjusting the value of `Minimum distance threshold of shapes lasso tool`. 
The default is 10 and can be any integer higher than 0 and lower than 50. As with 
the polygon creation tool, drawing the shape can also be finished by pressing the 
`Esc` key.

<ins>Reducing the number of vertices</ins>

After finishing drawing a polygon or path, an implementation of the 
[Ramer–Douglas–Peucker algorithm](https://en.wikipedia.org/wiki/Ramer–Douglas–Peucker_algorithm)
is applied to reduce the number of vertices that make up the geometry. In case of the
path the structure is preserved while in case of a polygon the contour is preserved.
The aggressiveness with which the algorithm reduces the number of vertices is determined 
by an `epsilon` parameter, which is a perpendicular distance threshold. Any vertices 
beyond the threshold will be preserved, so if `epsilon` is set to `0`, no vertices 
will be removed. With increasing values of `epsilon`, more and more vertices will 
be removed. The value of `epsilon` can be set in napari by going to `File` ->
`Preferences` (or `control + shift + p`), then in the menu on the left-clicking 
on `Experimental` and then adjusting the value of `RDP epsilon`. The default value 
is 0.5 and cannot be set lower than 0.