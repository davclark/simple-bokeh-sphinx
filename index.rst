.. Simple Bokeh Sphinx documentation master file, created by
   sphinx-quickstart on Thu Mar  2 16:39:32 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Simple Bokeh Sphinx's!
=================================

The following plot may be broken. But note that it is copy-pasted from
`Bokeh source
<https://github.com/bokeh/bokeh/blob/master/bokeh/sphinxext/bokeh_plot.py>`_

.. bokeh-plot::

     from bokeh.plotting import figure, output_file, show
     output_file("example.html")
     x = [1, 2, 3, 4, 5]
     y = [6, 7, 6, 4, 5]
     p = figure(title="example", plot_width=300, plot_height=300)
     p.line(x, y, line_width=2)
     p.circle(x, y, size=10, fill_color="white")
     show(p)
