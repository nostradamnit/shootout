Yet Another Web Framework Shootout
==================================

The idea for this project is to implement a non-trival application 
using a variety of web frameworks. The time and effort will be measured 
as well as the developers appreciate for each framework. Each implementation 
will reuse the same HTML user-interface, adapted to each frameworks templating 
system. The final rendered HTML should be virtually the same.

The Sample Project
------------------

The developers have tentatively decided to implement a social bookmarking 
application à la delicio.us. The application should have the following functionality.


 * User registration
 * Authenticated users can post URLs to bookmark publicly or privately
 * Authenticated users can upvote or otherwise note their URLs
 * URLs can be commented
 * URLs can have associated keywords (tags)
 * Authenticated users can note public URLs of any user
 * (more to come...)

### Technical Wishes
The best aspects of each framework should be used. Most will have the following


 * Friendly URLs
 * Transparent data access / object persistence
 * Intelligent Form handling
 * Unit-testable
 * Beautiful code


Frameworks
------------
The initial idea was to test Python frameworks. This has been expanded to 
include virtually any framework that appears to be interesting in its design 
and/or implementation or which distinguishes itself in some original way.

The inital **short** list of frameworks proposed is the following. 
There is also a more [https://github.com/nostradamnit/shootout/wiki/Potential-Framework-Candidates](complete list).


 * [Grok (py)](http://grok.zope.org/)
 * [Flask (py)](http://flask.pocoo.org/)
 * [Pyramid (py)](http://pyramid.readthedocs.org/en/1.3-branch/index.html)
 * [Bottle (py)](http://bottlepy.org/docs/dev/)
 * [web.py (py)](http://webpy.org/)
 * [Meteor (js)](http://www.meteor.com/)
 * [Silex(php)](http://silex.sensiolabs.org/)
