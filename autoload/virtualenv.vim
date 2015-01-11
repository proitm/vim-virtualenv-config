let s:plugin_path = escape(expand('<sfile>:p:h'), '\')

function! virtualenv#init()
    if &diff
        return
    endif

    exe 'pyfile ' . s:plugin_path . '/main.py'
    python initPythonModule()

endfunction
