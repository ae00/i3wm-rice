#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '

export EDITOR=vim
export VISUAL=vim

# Import colorscheme from 'wal' asynchronously
# &   # Run the process in the background.
# ( ) # Hide shell job control messages.
# Not supported in the "fish" shell.
(cat ~/.cache/wal/sequences &)

# Alternative (blocks terminal for 0-3ms)
cat ~/.cache/wal/sequences

# To add support for TTYs this line can be optionally added.
source ~/.cache/wal/colors-tty.sh

alias feh='feh --scale-down --image-bg black'
alias du='du -sh'
alias ddg='w3m duckduckgo.com'
alias gpt='tgpt -m'
alias bat='bat'
alias grep='grep --color=auto'
alias myip="curl http://ipecho.net/plain; echo"
alias df='pydf'
alias cl='clear'
alias dl='cd ~/Downloads'
alias doc='cd ~/Documents'
alias i3c='vim ~/.config/i3/config'

alias ls='exa'
alias ll='exa -alh'
alias lg='exa -alh | grep --ignore-case'

alias lsd='ls -D -l'
alias lsf='ls -f -l'
