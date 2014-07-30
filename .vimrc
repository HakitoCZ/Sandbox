" custom .vimrc

" autoreload .vimrc
autocmd! bufwritepost .vimrc source %

" Quicksave command
" ctrl + z
noremap <C-Z> :update<CR>
vnoremap <C-Z> <C-C>:update<CR>
inoremap <C-Z> <C-O>:update:<CR>

" moving blocks of code
" using shift + > / <
vnoremap < <gv
vnoremap > >gv

" syntax highlighting
syntax on

" automatic indentation
" copy indentation of last line
set autoindent

" somehow better Copy&Paste
set clipboard=unnamed

"" line length
set tw=79
" set formatoptions+=w
set fo-=t " don't automaticly wrap text when typing
set lbr " wrap ong lines between words
set wrap
set colorcolumn=80
highlight colorcolumn ctermfg=233 
  " dark grey color of the line >
  " doesn't quite work well..

" longer history
set history=500
set undolevels=500

" tabs to spaces etc
set tabstop=2
set softtabstop=2
set shiftwidth=2
set shiftround
set expandtab

" show line numbers
set number

" demap arrow keys
" arrows are bad habbit
map <Left> <Nop>
map <Right> <Nop>
map <Up> <Nop>
map <Down> <Nop>
map! <Left> <Nop>
map! <Right> <Nop>
map! <Up> <Nop>
map! <Down> <Nop>

