##########################
ReStructured Text Examples
##########################

Basic Stuff
***********

Emphasis
========

*emphasis*

Strong emphasis
===============

**emphasis**

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
