"""Table generation utilities for napari documentation.

This module provides functionality to create formatted ASCII and Markdown tables
for use in the napari documentation. It supports multiple border styles and
customizable formatting options.

The primary use case is generating well-formatted tables for event documentation,
preferences documentation, and other tabular data that needs to be displayed in
the napari documentation.

Example:
    Basic usage with markdown style (default)::

        >>> from _table_maker import table_repr
        >>> data = [
        ...     ['Event', 'Description', 'Type'],
        ...     ['theme', 'Theme changed', 'str'],
        ...     ['title', 'Title changed', 'str']
        ... ]
        >>> print(table_repr(data, header=data[0], style='markdown'))

    Using different border styles::

        >>> # Double-line borders
        >>> print(table_repr(data, style='double'))

        >>> # Heavy borders
        >>> print(table_repr(data, style='heavy'))

        >>> # Light borders
        >>> print(table_repr(data, style='light'))

Attributes:
    STYLES (dict): Dictionary of border style definitions. Each style contains:
        - TOP: Characters for top border (left corner, separator, right corner, line)
        - MID: Characters for middle borders (left, separator, right, line)
        - BOT: Characters for bottom border (left corner, separator, right corner, line)
        - V: Characters for vertical borders (outer, inner)

Available styles:
    - 'double': Double-line box drawing characters (╔═╤═╗)
    - 'heavy': Heavy box drawing characters (┏━┯━┓)
    - 'light': Light box drawing characters (┌─┬─┐)
    - 'markdown': Markdown-compatible table format (| | |)

Attribution
-----------
This docstring was drafted with the assistance of Claude Code.
The output was reviewed and edited for accuracy and clarity.
"""

import numpy as np

STYLES = {
    'double': {
        'TOP': ('╔', '╤', '╗', '═'),
        'MID': ('╟', '┼', '╢', '─'),
        'BOT': ('╚', '╧', '╝', '═'),
        'V': ('║', '│'),
    },
    'heavy': {
        'TOP': ('┏', '┯', '┓', '━'),
        'MID': ('┠', '┼', '┨', '─'),
        'BOT': ('┗', '┷', '┛', '━'),
        'V': ('┃', '│'),
    },
    'light': {
        'TOP': ('┌', '┬', '┐', '─'),
        'MID': ('├', '┼', '┤', '─'),
        'BOT': ('└', '┴', '┘', '─'),
        'V': ('│', '│'),
    },
    'markdown': {
        'TOP': (' ', ' ', ' ', ' '),
        'MID': ('|', '|', '|', '-'),
        'BOT': (' ', ' ', ' ', ' '),
        'V': ('|', '|'),
    },
}


def table_repr(
    data,
    padding=2,
    ncols=None,
    header=None,
    cell_width=None,
    divide_rows=True,
    style='markdown',
):
    """Pretty string repr of a 2D table."""
    try:
        nrows = len(data)
    except TypeError:
        raise TypeError('data must be a collection')
    if not nrows:
        return ''

    try:
        ncols = ncols or len(data[0])
    except TypeError:
        raise TypeError('data must be a collection')
    except IndexError:
        raise IndexError('data must be a 2D collection of collections')

    _widths = list(data)
    if header:
        _widths.append(list(header))
    _widths = np.array([[len(str(item)) for item in row] for row in _widths])
    cell_widths = _widths.max(0).tolist()

    _style = STYLES[style]
    TOP, MID, BOT, V = _style['TOP'], _style['MID'], _style['BOT'], _style['V']

    pad = ' ' * padding
    cell_templates = [(pad + '{{:{0}}}' + pad).format(max(cw, 5)) for cw in cell_widths]
    row_template = V[0] + V[1].join(cell_templates) + V[0]

    def _border(left, sep, right, line):
        _cells = [len(ct.format('')) * line for ct in cell_templates]
        return left + sep.join(_cells) + right

    body = [_border(*TOP)]

    if header:
        body.append(row_template.format(*header))
        body.append(_border(*MID))

    for i, row in enumerate(data):
        body.append(row_template.format(*row))
        if divide_rows and i < nrows - 1:
            body.append(_border(*MID))

    body.append(_border(*BOT))
    return '\n'.join(body)
