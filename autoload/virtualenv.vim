let s:plugin_path = escape(expand('<sfile>:p:h'), '\')

function! virtualenv#init()
    exe 'pyfile ' . s:plugin_path . '/main.py'
    python initPythonModule()
endfunction

augroup init
    autocmd!
    autocmd VimEnter * call virtualenv#init()
augroup END
