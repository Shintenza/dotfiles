### PATH ###
set -e fish_user_paths
set -U fish_user_paths $HOME/.local/bin $fish_user_paths

### EXPORTS ###
set fish_greeting 
set EDITOR "nvim"
set VISUAL "neovide"

### BASIC COLORING ###
set fish_color_error -o red
set fish_color_normal white
set fish_color_command white
set fish_color_param white

### VI MODE ENABLED ###
function fish_user_key_bindings
  # fish_default_key_bindings
  fish_vi_key_bindings
end

### ALIASES ###
alias untar="tar -xvf"
alias vim="nvim --clean"
alias grubcfg="sudo grub-mkconfig -o /boot/grub/grub.cfg"
alias ls="exa -lah --icons"
alias cat="bat"
alias py="python"
alias neofetch="neofetch --disable gpu cpu memory resolution"

### PROMPT ###
starship init fish | source
