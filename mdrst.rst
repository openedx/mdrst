#################################
RSt cheat sheet for Markdown fans
#################################


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
          #. Actual numbers don't matter

     - 


   * - Bullets
     - ::

          * First unordered list item
          * Another item
          * And another item.

     - ::

          * First unordered list item
          * Another item
          * And another item.

     - 


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

          (URLs don't automatically link.)

     - ::

          URLs make links: http://python.org.

     - 


   * - Inline
     - ::

          [Inline link](http://python.org) for brevity.

     - ::

          `Inline link <http://python.org>`__ for brevity.

     - 


   * - Indirect
     - ::

          [Indirect link][indirect] for readability.

          [indirect]: http://python.org

     - ::

          `Indirect link`_ for readability.

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


