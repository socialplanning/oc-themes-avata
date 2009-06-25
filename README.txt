This is a theme for opencore (http://coactivate.org/projects/opencore).

To use it, configure your front-end proxy to hit Zope at the following URL:
http://localhost:<port>/VirtualHostBase/http/<hostname>/++skin++avata/<instance>

... where <port> is the port that Zope runs on, <hostname> is the public
hostname at which people visit the site, and <instance> is the name of
your opencore instance (by convention this is normally "openplans").

It should be possible to instead use the zcml browser:defaultSkin directive,
but for some reason I'm told that doesn't work with this skin.

