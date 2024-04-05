import os

s = os.system

# clone configs
s("git clone https://github.com/zawkindev/dotfiles")
s("cp -r ./dotfiles/nvim_gruvbox ~/.config")
s("mv ~/.config/nvim_gruvbox ~/.config/nvim")
s("rm -rf dotfiles")

# install dependencies
s("paru -Sy nvm xclip")
s("echo 'source /usr/share/nvm/init-nvm.sh' >> ~/.bashrc")
s("echo 'source /usr/share/nvm/init-nvm.sh' >> ~/.zshrc")
s("""
export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \\. "$NVM_DIR/nvm.sh" # This loads nvm
  """)

# install and use node&npm lts
s("nvm install --lts")
s("nvm use --lts")
