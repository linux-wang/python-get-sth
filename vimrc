set is
if has("syntax")
syntax on
endif
colo elflord
set nocopatible
set magic
set ru
set smarttab
set ai
set nu
set sw=4
set ts=4
set dy=lastline
set backspace=indent,eol,start
sy on

set ambiwidth=double
set ignorecase
set autoindent
set mousemodel=popup
set wildmenu
set nobackup
set hlsearch
set showmatch
set expandtab
set number
set tabstop=4


set sm
set cin
set lbr
set encoding=utf-8
set autowrite
set background=dark

let Tlist_Auto_Highlight_Tag=1
let Tlist_Auto_Open=1
let Tlist_Auto_Update=1
let Tlist_Display_Tag_Scope=1
let Tlist_Exit_OnlyWindow=1
let Tlist_Enable_Dold_Column=1
let Tlist_File_Fold_Auto_Close=1
let Tlist_Show_One_File=1
let Tlist_Use_Right_Window=1
let Tlist_Use_SingleClick=1
nnoremap <silent> <F8> :TlistToggle<CR>

autocmd FileType python set omnifunc=pythoncomplete#Complete
autocmd FileType javascr.pt set omnifunc=javascriptcomplete#CompleteJS
autocmd FileType html set omnifunc=htmlcomplete#CompleteTags
autocmd FileType css set omnifunc=csscomplete#CompleteCSS
autocmd FileType xml set omnifunc=xmlcomplete#CompleteTags
autocmd FileType php set omnifunc=phpcomplete#CompletePHP
autocmd FileType c set omnifunc=ccomplete#Complete
let g:pydiction_location='~/.vim/complete-dict'

