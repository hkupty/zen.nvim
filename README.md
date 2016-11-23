# zen.nvim
A simple nvim ui framework for python

## Motivation

This framework intends to provide a range of functions to allow remote plugins
interact visually with neovim.

Whether you want to create a new window, prompt the user for some input or
toggle the visibility of a buffer, zen will provide a function for that, so you
can focus solely on the functionality, removing the window/buffer management
hassle from your code.

## Using this framework

While this is a simple python module that expects you to have neovim installed,
it does not require anything explicitly and can simply be embedded into you
application.

One can do so in several ways:

  * Adding this as module a git submodule of your application [preferred]
  * Requiring the user to explicitly install
  * Copying the files from this module to your app

### Using as submodule

Simply `git submodule add https://github.com/hkupty/zen.nvim.git` to your app.

It is recommended that you checkout a version branch so you'll ensure
compatibility if zen gets updated.
