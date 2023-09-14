
.. Don't edit this file directly.  It's created from four parts:
..      sheet_head.rst is the first content
..      md.md is a Markdown file parsed for content to go in the table.
..      rst.rst is an RST file parsed for content to go in the table.
..      sheet_foot.rst is the final content
..
.. See the README.rst for instructions.


#################################
RST cheat sheet for Markdown fans
#################################

This cheatsheet provides a quick reference for translating
Markdown to ReStructured Text (RST) to help someone author or edit
RST files.

You can look at the `original Markdown file <md.md>`_ and the
`original RST file <rst.rst>`_ that the examples were culled from
to see the formatting as GitHub presents it.



Basic Stuff
***********

.. list-table::
   :widths: 15 30 30 15
   :header-rows: 1

   * - What
     - Markdown
     - reStructuredText
     - Notes


   * - Emphasis
     - ::

          This word is *italicized*, _underscores_ also work

     - ::

          This word is *italicized*.

     -

          RST only allows asterisks for emphasis and strong emphasis.

   * - Strong emphasis
     - ::

          This word is **bold** and *markup __can__ be nested*.

     - ::

          This word is **bold**.

     -

          RST cannot nest inline markup, so there is no way to have an emphasized sentence with a strongly emphasized word, nor a link in strongly emphasized text, for example.

   * - Code inline
     - ::

          Call the `function_name` function.

     - ::

          Call the ``function_name`` function.

     -



   * - Code blocks
     - ::

          Look at this output:

          ```
          $ ls /usr/
          bin        lib        libexec
          ```

          Look at this code:

          ```python
          def fib(n):
              if n <= 2:
                  return 1
              else:
                  return fib(n-1) + fib(n-2)
          ```

     - ::

          Look at this output::

             $ ls /usr/
             bin        lib        libexec

          Look at this code:

          .. code-block:: python

              def fib(n):
                  if n <= 2:
                      return 1
                  else:
                      return fib(n-1) + fib(n-2)

     -



   * - Blockquotes
     - ::

          Lincoln said:

          > Four-score and seven years ago, our fathers
          > brought forth on this continent a new nation,
          > conceived in Liberty, and dedicated to the
          > proposition that all men are created equal.

     - ::

          Lincoln said:

             Four-score and seven years ago, our fathers
             brought forth on this continent a new nation,
             conceived in Liberty, and dedicated to the
             proposition that all men are created equal.

     -



Lists
*****

.. list-table::
   :widths: 15 30 30 15
   :header-rows: 1

   * - What
     - Markdown
     - reStructuredText
     - Notes


   * - Numbered
     - ::

          1. First ordered list item
          1. Another item
          1. Actual numbers don't matter

     - ::

          #. First ordered list item
          #. Another item
          #. Use hash marks for numbers

     -



   * - Bullets
     - ::

          * First unordered list item
          * Another item
          * And another item

     - ::

          * First unordered list item
          * Another item
          * And another item

     -



   * - Nested
     - ::

          1. First outer
             * First inner
             * Second inner
          2. Second outer
          3. Third outer

     - ::

          #. First outer

             * First inner
             * Second inner

          #. Second outer
          #. Third outer

     -

          RST needs blank lines around the inner list.

Links
*****

.. list-table::
   :widths: 15 30 30 15
   :header-rows: 1

   * - What
     - Markdown
     - reStructuredText
     - Notes


   * - URLs
     - ::

          URLs make links: http://python.org.

     - ::

          URLs make links: http://python.org.

     -

          Classic Markdown doesn't auto-link URLs.

   * - Inline
     - ::

          [Inline link](http://python.org)
          for brevity.

     - ::

          `Inline link <http://python.org>`__
          for brevity.

     -



   * - Indirect
     - ::

          [Indirect link][indirect]
          for readability.

          [indirect]: http://python.org

     - ::

          `Indirect link`_
          for readability.

          .. _Indirect link: http://python.org

     -



Headers
*******

.. list-table::
   :widths: 15 30 30 15
   :header-rows: 1

   * - What
     - Markdown
     - reStructuredText
     - Notes


   * - Headers
     - ::

          # First Header

          ## Second Header

          ### Third Header

          #### Fourth Header

     - ::

          ############
          First Header
          ############

          Second Header
          *************

          Third Header
          ============

          Fourth Header
          -------------

     -

          The overlines and characters are flexible in RST as long as they are consistent.  RST requires strict nesting; even after the hierarchy is established, you can't use, say, a third-tier header right under a first-tier whereas MD allows this.

Images
******

.. list-table::
   :widths: 15 30 30 15
   :header-rows: 1

   * - What
     - Markdown
     - reStructuredText
     - Notes


   * - Images
     - ::

          ![Image of Xsy](xsy_150.png)

     - ::

          .. image:: xsy_150.png
             :alt: Image of Xsy

     -



Notes etc
*********

.. list-table::
   :widths: 15 30 30 15
   :header-rows: 1

   * - What
     - Markdown
     - reStructuredText
     - Notes


   * - Notes
     - ::

          Markdown has no specialized syntax for notes.

     - ::

          .. note::
             This is the text of a note.

     -

          GitHub's RST rendering doesn't make this stand out much.

   * - Footnotes
     - ::

          Extended Markdown supports footnotes[^1].

          [^1]: The footnote will mostly be displayed in the bottom
          no matter where you define it, hence _the name_.

     - ::

          An example of footnote [1]_.

          .. [1] It's similar to hyperlink syntax.

     -



   * - Warnings
     - ::

          Markdown has no specialized syntax for warnings.

     - ::

          .. warning::
             This is the text of a warning.

     -

          GitHub's RST rendering doesn't make this stand out much.


Additional Resources
********************

Both MD and RST have many more features, please add examples you would find useful.  Also check out the official `RST User Documentation`_.

.. _RST User Documentation: http://docutils.sourceforge.net/rst.html

