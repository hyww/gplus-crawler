gplus_crawler
=============

README Last Updated on 2014.09.15

Introduction
============

Download and backup Google Plus (Google+) ``Pictures`` or ``Videos`` in messages

* Just backup (download) pictures and videos in messages
* The best video quality

Requirements
============

+ Python == 2.7
+ wxPython >= 2.9.4  (For UI)


About How to Use
==================

* Download it (portable)
    * https://code.google.com/p/gplus-crawler/downloads/list
* Uncompress and execute ``start_ui.exe`` to run
* Input Google+ id that you want to backup (download) user into text field
    * ex: 105229500895781124316
* Press ``Go Download!`` button
* If yout want to ``Stop``, press ``Stop`` button

Change log
===========
* `0.4`_ (2014-09-08)
    * Added: Video date
    * Fixed: Regex bugs
    * Enhanced: Refactored system structure for download efficiency
    * Enhanced: Integrated Video and Pictures crawlers.
* `0.3`_ (2013-05-30)
    * Fixed: Full crawl fail (Only 1000 messages).
    * Fixed: Refactored system for Google+ change design
* `0.2.4`_ (2013-05-16)
    * Implemented: Videos full crawler from G+ message
    * Enhanced: Download efficiency
* `0.1`_ (2013-04-05)
    * Implemented: Pictures full crawler from G+ message

Licence
========
MIT License