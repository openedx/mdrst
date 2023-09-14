################################
Markdown-to-RST Cheatsheet Maker
################################

Open edX uses ReStructured Text (RST) for its documentation.  People have told
us they are unfamiliar with RST, and that a comparison of the two would be
welcome.

The cheatsheet: `mdrst.rst`_.

In this repo are two files: `md.md`_ and `rst.rst`_.  They have parallel
heading structures, each showing how their format represents each construct.
Together, they produce `mdrst.rst`_, which shows the examples side-by-side.

The convert.py tool reads those two files, and produces:

* md.html, the HTML output from md.md.
* rst.html, the HTML output from rst.rst.
* mdrst.rst, the source for the side-by-side comparison.
* mdrst.html, the HTML output from mdrst.rst.

To run the tool::

   $ python3.8 -m pip install -r requirements.txt
   $ python3.8 convert.py

.. _md.md: https://github.com/openedx/mdrst/blob/master/md.md
.. _rst.rst: https://github.com/openedx/mdrst/blob/master/rst.rst
.. _mdrst.rst: https://github.com/openedx/mdrst/blob/master/mdrst.rst
