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

" line length
set tw=79
set nowrap
set colorcolumn=80
highlight ColorColumn ctermfg=233 
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
