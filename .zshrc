path+=$HOME/.local/bin
export PATH
export STEAM_COMPAT_DATA_PATH=$HOME/proton
#export EDITOR='nvim'
#export VISUAL='nvim'

# Enable vi mode
bindkey -v
bindkey "^?" backward-delete-char


###########
# HISTORY #
###########

HISTSIZE=10000
SAVEHIST=10000
HISTFILE=~/.cache/zsh_history
setopt appendhistory


##################
# AUTOCOMPLETION # 
##################

source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
autoload -Uz compinit
compinit
zstyle ':completion:*' menu select
zstyle ':completion::complete:*' gain-privileges 1


###########
# ALIASES #
###########

alias untar="tar -xvf"
#alias wine="WINEPREFIX=/mnt/Games/Wine wine"
alias vim="nvim"
alias grubcfg="sudo grub-mkconfig -o /boot/grub/grub.cfg"
alias ls="exa -lah --icons"
alias cat="bat"
alias yay="paru"
alias py="python"
alias neofetch="neofetch --disable gpu cpu memory resolution"
alias potato-enable="sudo tc qdisc add dev wlp3s0 root netem loss 0%"
alias potato-set="sudo tc qdisc change dev wlp3s0 root netem loss"
#alias code="vscodium"

#####################
# SPACESHIP PROMOPT #
#####################

# Spaceship could be installed using AUR (spaceship-prompt-git) or using yarn/npm (spaceship-prompt)

autoload -U promptinit; promptinit
SPACESHIP_PROMPT_FIRST_PREFIX_SHOW=true
prompt spaceship

SPACESHIP_PROMPT_ADD_NEWLINE=false
SPACESHIP_PROMPT_ORDER=(
  time          # Time stamps section
  user          # Username section
  host          # Hostname section
  dir           # Current directory section
  git           # Git section (git_branch + git_status)
  hg            # Mercurial section (hg_branch  + hg_status)
  package       # Package version
  gradle        # Gradle section
  maven         # Maven section
  node          # Node.js section
  ruby          # Ruby section
  elixir        # Elixir section
  xcode         # Xcode section
  swift         # Swift section
  golang        # Go section
  php           # PHP section
  rust          # Rust section
  haskell       # Haskell Stack section
  julia         # Julia section
  docker        # Docker section
  aws           # Amazon Web Services section
  gcloud        # Google Cloud Platform section
  venv          # virtualenv section
  conda         # conda virtualenv section
  pyenv         # Pyenv section
  dotnet        # .NET section
  ember         # Ember.js section
  kubectl       # Kubectl context section
  terraform     # Terraform workspace section
  exec_time     # Execution time
  line_sep      # Line break
  battery       # Battery level and status
  vi_mode       # Vi-mode indicator
  jobs          # Background jobs indicator
  exit_code     # Exit code section
  char          # Prompt character
)
SPACESHIP_USER_SHOW=always
SPACESHIP_USER_SUFFIX=""
SPACESHIP_USER_PREFIX=" "
SPACESHIP_HOST_SHOW=always
SPACESHIP_DIR_PREFIX="  "
SPACESHIP_HOST_PREFIX="@"
SPACESHIP_VI_MODE_SHOW=false
SPACESHIP_BATTERY_SHOW=false
fpath=($fpath "/home/kamil/.zfunctions")
fpath=($fpath "/home/kamil/.zfunctions")
