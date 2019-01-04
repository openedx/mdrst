##########################
ReStructured Text Examples
##########################

Basic Stuff
***********

Emphasis
========

This word is *italicized*.

Strong emphasis
===============

This word is **bold**.

Code inline
===========

Call the ``function_name`` function.

Code blocks
===========

Look at this code::

    def fib(n):
        if n <= 2:
            return 1
        else:
            return fib(n-1) + fib(n-2)

Blockquotes
===========

Lincoln said:

   Four-score and seven years ago, our fathers
   brought forth on this continent a new nation,
   conceived in Liberty, and dedicated to the
   proposition that all men are created equal.


Lists
*****

Numbered
========

#. First ordered list item
#. Another item
#. Use hash marks for numbers

Bullets
=======

* First unordered list item
* Another item
* And another item

Nested
======

.. note: RST needs blank lines around the inner list.

#. First outer

   * First inner
   * Second inner

#. Second outer
#. Third outer

Links
*****

URLs
====

URLs make links: http://python.org.

Inline
======

`Inline link <http://python.org>`__
for brevity.

Indirect
========

`Indirect link`_
for readability.

.. _Indirect link: http://python.org


Headers
*******

Headers
=======

.. parse-headers-off

.. note: The overlines in RST are optional and characters are flexible as long as they are consistent.

############
First Header
############

Second Header
*************

Third Header
============

Fourth Header
-------------

.. parse-headers-on


Images
******

Images
======

.. image:: xsy_150.png
   :alt: Image of Xsy
