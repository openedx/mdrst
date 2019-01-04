#################################
RST cheat sheet for Markdown fans
#################################

This is a comparison of Markdown and ReStructured Text to help people
authoring or editing RST files.

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

          *emphasis*

     - ::

          *emphasis*

     -



   * - Strong emphasis
     - ::

          **emphasis**

     - ::

          **emphasis**

     -



   * - Code inline
     - ::

          Call the `function_name` function.

     - ::

          Call the ``function_name`` function.

     -



   * - Code blocks
     - ::

          Look at this code:

          ```
          def fib(n):
              if n <= 2:
                  return 1
              else:
                  return fib(n-1) + fib(n-2)
          ```

     - ::

          Look at this code::

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



