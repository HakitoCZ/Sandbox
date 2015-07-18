execute pathogen#infect()

" autoreload .vimrc
autocmd! bufwritepost .vimrc source %

" Quicksave command
" ctrl + z
noremap <C-Z> :update<CR>

" moving blocks of code
" keeps selected visual mode
"vnoremap < <gv
"vnoremap > >gv

" repeat command . works in visual as well
vnoremap . :normal .<CR>

" syntax highlighting
syntax on
" detect filetype and sets indent etc etc
"filetype plugin indent on

" cursor line highlight
"set cursorline
"highlight CursorLine cterm=bold
" light grey text on active line
"highlight CursorLine ctermfg=white

" turn on completion menu
set wildmenu

" highlight searches with /
"set hlsearch
" ignore case sensitivity
set ignorecase
" if you search Capitalized searches case sensitive
set smartcase
" incremental search = search as you type
set incsearch

" automatic indentation
" copy indentation of last line
set autoindent
set smartindent

" yank to clipboard
set clipboard=unnamedplus

" line numbers
" should be working properly with vim7.4
" in 7.3.xx shows zero instead of absolute number
set number
set relativenumber
highlight LineNr ctermfg=3

"" line length
set textwidth=79
"" set formatoptions+=w
"set fo-=t " don't automaticly wrap text when typing
set lbr " wraping lines between words
set wrap
"set colorcolumn=80
"highlight colorcolumn ctermbg=4

" longer history
set history=500
set undolevels=500

" tabs to spaces etc
set tabstop=4
set softtabstop=4
set shiftwidth=4
set shiftround
set expandtab

" demap arrow keys
" still works in cmd mod
imap <Left> <Nop>
imap <Right> <Nop>
imap <Up> <Nop>
imap <Down> <Nop>
nmap <Left> <Nop>
nmap <Right> <Nop>
nmap <Up> <Nop>
nmap <Down> <Nop>
vmap <Left> <Nop>
vmap <Right> <Nop>
vmap <Up> <Nop>
vmap <Down> <Nop>

map <F2> :NERDTreeToggle<CR>

" Preven from going to ex mode with Q
map <S-Q> <Nop>

