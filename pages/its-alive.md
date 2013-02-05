title: It's Alive!
date: 2012-12-15
type: post

I've ran this site on a few platforms in the past. This started out with
Wordpress, moved to Tumblr, then Octopress. All of these services have their
pros and cons, but I decided that I wanted something a bit more custom.

My main requirements were to be able to write content in a simple format like
Markdown, and have all content exist as files instead of in a database.
I stumbled across [this article](https://nicolas.perriault.net/code/2012/dead-easy-yet-powerful-static-website-generator-with-flask/)
which showed how to use [Flask](http://flask.pocoo.org/) to generate static
pages. I was using Flask for some other stuff, so I figured it was a good fit.

The content on the site is static. All the pages are written in Markdown, and
[Flask-FlatPages](http://packages.python.org/Flask-FlatPages/)
indexes the files. I run a Flask server on my development box to create
posts and such, then generate a static version using
[Frozen-Flask](http://packages.python.org/Frozen-Flask/). That gets pushed to a
server as static HTML and CSS.

There's still a lot of improvements to make, but if you're interested, the
code is available on [Github](http://www.github.com/ericevenchick/site).
