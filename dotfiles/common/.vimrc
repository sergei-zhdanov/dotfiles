" All system-wide defaults are set in $VIMRUNTIME/archlinux.vim (usually just
" /usr/share/vim/vimfiles/archlinux.vim) and sourced by the call to :runtime
" you can find below.  If you wish to change any of those settings, you should
" do it in this file (/etc/vimrc), since archlinux.vim will be overwritten
" everytime an upgrade of the vim packages is performed.  It is recommended to
" make changes after sourcing archlinux.vim since it alters the value of the
" 'compatible' option.

set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'

" The following are examples of different formats supported.
" Keep Plugin commands between vundle#begin/end.
" plugin on GitHub repo
" Plugin 'tpope/vim-fugitive'
" plugin from http://vim-scripts.org/vim/scripts.html
" Plugin 'L9'
" Git plugin not hosted on GitHub
" Plugin 'git://git.wincent.com/command-t.git' 
" git repos on your local machine (i.e. when working on your own plugin)
" Plugin 'file:///home/gmarik/path/to/plugin'
" The sparkup vim script is in a subdirectory of this repo called vim.
" Pass the path to set the runtimepath properly.
" Plugin 'rstacruz/sparkup', {'rtp': 'vim/'}
" Install L9 and avoid a Naming conflict if you've already installed a
" different version somewhere else.
" Plugin 'ascenator/L9', {'name': 'newL9'}
Plugin 'vim-scripts/ruscmd'
Plugin 'godlygeek/tabular'
Plugin 'plasticboy/vim-markdown'
Plugin 'vim-airline/vim-airline'
Plugin 'vim-airline/vim-airline-themes'
Plugin 'lervag/vimtex'
Plugin 'vim-pandoc/vim-pandoc'
"Plugin 'vim-pandoc/vim-pandoc-syntax'
Plugin 'vim-scripts/vim-punto-switcher'
"Plugin 'neomake/neomake'
"Plugin 'zuckonit/vim-airline-tomato'
"Plugin 'idbrise/asynccommand'
"Plugin 'mnick/vim-pomodoro'
"
" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required
" To ignore plugin indent changes, instead use:
"filetype plugin on
"
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line

" This line should not be removed as it ensures that various options are
" properly set to work with the Vim-related packages.
runtime! archlinux.vim

" If you prefer the old-style vim functionalty, add 'runtime! vimrc_example.vim'
" Or better yet, read /usr/share/vim/vim80/vimrc_example.vim or the vim manual
" and configure vim to your own liking!

" do not load defaults if ~/.vimrc is missing
"let skip_defaults_vim=1

set number relativenumber
"augroup numbertoggle
"	autocmd!	
"	autocmd BufEnter,FocusGained,InsertLeave * set relativenumber
"	autocmd BufLeave,FocusLost,InsertEnter * set norelativenumber
"augroup END

" colorscheme desert

syntax on

let maplocalleader = "\\"

set tw=99
set fo-=l
set wm=2
set lbr

set nofoldenable
autocmd Filetype tex setlocal nofoldenable

:nnoremap "" ciw""<Esc>P
:nnoremap '' ciw''<Esc>P
":nnoremap <Leader>qd daW"=substitute(@@,"'\\\|\"","","g")<CR>P

let g:vimtex_fold_manual = 0
let g:vimtex_fold_enabled = 0
let g:vimtex_view_method = 'zathura'
let g:vimtex_complete_close_braces = 1

let g:airline_theme='murmur'
let g:airline_powerline_fonts=1
set ttimeoutlen=1
set noshowmode

let g:pandoc#spell#enabled=0
"let g:pandoc#spell#default_langs='ru'
let g:pandoc#modules#disabled = ["formatting"]
