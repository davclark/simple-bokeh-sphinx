#!/usr/bin/env python3

from __future__ import print_function

from bokeh.plotting import figure
from bokeh.embed import autoload_static
from bokeh.resources import INLINE

x = [1, 2, 3, 4, 5]
y = [6, 7, 6, 4, 5]
p = figure(title="example", plot_width=300, plot_height=300)
p.line(x, y, line_width=2)
p.circle(x, y, size=10, fill_color="white")

# When sphinx copies the file, it will not retain the subdirectory
js, tag = autoload_static(p, INLINE, 'plot.js')

with open('static/plot.js', 'w') as js_file:
    js_file.write(js)

with open('static/tag.html', 'w') as tag_file:
    tag_file.write(tag)
