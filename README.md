pyramid_asbool
==============

This is an extension to the Pyramid webframework's asbool to support extra truthy options.

Getting Started
===================

In your `__init__.py` of your application just put this at the top:


    from pyramid_asbool import patch_asbool
    patch_asbool()


and now you will be be able to switch your configs from:

    pyramid.reload_templates = true
    pyramid.debug_authorization = false

to

    pyramid.reload_templates = ✔
    pyramid.debug_authorization = ✖


Vim
===================
If you are using vim, you can enter insert mode by typing `i` and then typing
`ctrl-k` and then `OK` you will get the ✓ character
