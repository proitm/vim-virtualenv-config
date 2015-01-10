if exists('g:virtualenv_config_loaded')
    finish
endif

let g:virtualenv_config_loaded = 1

if !has('python')
    finish
endif

augroup init
    autocmd!
    autocmd VimEnter * call virtualenv#init()
augroup END
