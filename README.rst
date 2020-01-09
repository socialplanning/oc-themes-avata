===============
oc-themes-avata
===============

The CoActivate.org theme aka avata theme for OpenCore Software (http://coactivate.org/projects/opencore).


Features
========

- Provides support to overrides for custom viewlets and views.


Examples
========

This add-on can be seen in action at the following sites:

- http://coactivate.org/

- http://openfsm.net/


Translations
============

This product has been translated into:

- Greek

- Spanish

- French

- Portuguese


How to use it
=============

This is a theme for opencore (http://coactivate.org/projects/opencore).

To use it, configure your front-end proxy to hit Zope at the following URL:
http://localhost:<port>/VirtualHostBase/http/<hostname>/++skin++avata/<instance>

... where <port> is the port that Zope runs on, <hostname> is the public
hostname at which people visit the site, and <instance> is the name of
your opencore instance (by convention this is normally "openplans").

Note that you really do need to configure your front-end proxy to hit Zope at
that URL! Visiting http://localhost:<port>/++skin++avata/<instance> directly
will not work, because all the css and image links will still be pointing at 
the unskinned site root.

It should be possible to instead use the zcml browser:defaultSkin directive,
but for some reason I'm told that doesn't work with this skin.


Contribute
==========

- Issue Tracker: https://github.com/socialplanning/oc-themes-avata/issues
- Source Code: https://github.com/socialplanning/oc-themes-avata
- Documentation: https://www.coactivate.org/projects/opencore/
- Translations: https://www.transifex.com/plone/social-planning/dashboard/


Support
=======

If you are having issues, please let us know.
We have a mailing list located at: opencore-dev@lists.coactivate.org

License
=======

The project is licensed under the GPLv2.

