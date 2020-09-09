call plug#begin('~/.vim/plugged')

Plug 'scrooloose/nerdtree', { 'on':  'NERDTreeToggle' }

Plug 'ycm-core/YouCompleteMe'
" colorscheme
Plug 'morhetz/gruvbox'
Plug 'jiangmiao/auto-pairs'
Plug 'tpope/vim-fugitive'
Plug 'airblade/vim-gitgutter'
Plug 'kien/ctrlp.vim'
Plug 'easymotion/vim-easymotion'

" Initialize plugin system
call plug#end()


syntax on
let g:mapleader=','
set background=dark
colorscheme gruvbox

set number
set numberwidth=6
set expandtab
set tabstop=4

set hlsearch
set incsearch
set termencoding=utf8


" mappings
map <C-n> :NERDTreeToggle<CR>
map <Leader> <Plug>(easymotion-prefix)

