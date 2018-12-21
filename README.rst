################################
Markdown-to-RST Cheatsheet Maker
################################

Open edX uses ReStructured Text (RST) for its documentation.  People have told
us they are unfamiliar with RST, and that a comparison of the two would be
welcome.

I started by editing a document with side-by-side examples of both Markdown and
RST, but it was difficult to edit, and difficult to know that I had gotten all
of the details right.

In this repo are two files: md.md and rst.rst.  They have parallel heading
structures, each showing how their format represents each construct.

The convert.py tool reads those two files, and produces:

* md.html, the HTML output from md.md.
* rst.html, the HTML output from rst.rst.
* mdrst.rst, the source for the side-by-side comparison.
* mdrst.html, the HTML output from mdrst.rst.

To run the tool::

   $ python3.6 -m pip install -r requirements.txt
   $ python3.6 convert.py
