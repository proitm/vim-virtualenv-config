# virtualenv-config vim plugin
This plugin was created to simplify routine with virtualenv activation in vim.
Using this pluging you can have `.virtualenv_config` file in your project
directory and run vim from any subdirectory of your project root or from
project root exactly and you will get all benefits of having activated virtual
environment in your edtor like proper goto and autocompletion for 3dparty 
packages in vim-jedi for example.

## IMPORTANT NOTE
This plugin doesn't replace python executable in vim like 
vim-virtualenv (https://github.com/jmcantrell/vim-virtualenv/) does so you
shouldn't expect virtualenv python execution by running :python or :!python in
vim but you can easily implement such behaviour and extend this plugin by
creating pull a request.

## CONTIBUTION
Any pull requests, improvement proposals, bug reports are welcome.
