" This is basic vim plugin boilerplate
let s:save_cpo = &cpo
set cpo&vim

function! s:restore_cpo()
  let &cpo = s:save_cpo
  unlet s:save_cpo
endfunction

if exists('g:virtualenv_config_loaded')
    call s:restore_cpo()
    finish
endif

let g:virtualenv_config_loaded = 1

if !has('python')
    call s:restore_cpo()
    finish
endif

augroup virtualenvConfigStart
    autocmd!
    autocmd FileType python call virtualenv#init()
augroup END

autocmd FileType python call virtualenv#init()

" This is basic vim plugin boilerplate
call s:restore_cpo()
