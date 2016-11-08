# zen.nvim
A simple nvim ui framework for python

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
