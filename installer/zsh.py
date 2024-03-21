import os

s = os.system
p = os.path


s("sudo pacman -Sy wget curl zsh")


def exists(path): return p.exists(p.expanduser(path))


# backup existing oh-my-zsh
if exists("~/.oh-my-zsh"):
    want_remove = input(
        "\nDo you want to remove current zsh and omz? ([yes],no): ")
    if want_remove == "no":
        s("mv ~/.oh-my-zsh ~/.oh-my-zsh.bak")
        s("mv ~/.zshrc ~/.zshrc.bak")
    else:
        s("rm -rf ~/.oh-my-zsh")
        s("rm -rf ~/.zshrc")

# install and configure oh-my-zsh
s("rm -rf install.sh")
s('sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"')
s("git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting")
s("git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions")
s("git clone https://github.com/agkozak/zsh-z ~/.oh-my-zsh/custom/plugins/zsh-z")

zsh_config = """
export ZSH="$HOME/.oh-my-zsh"

ZSH_THEME="daivasmara"

plugins=(
    git
    history-substring-search
    colored-man-pages
    zsh-autosuggestions
    zsh-syntax-highlighting
    zsh-z
)

source $ZSH/oh-my-zsh.sh

# common
alias re="source ~/.zshrc"
alias cls="clear"
alias :q="exit"
alias vim="nvim"
alias hx="helix"
alias tx="tmux"

# git
alias g="git"
alias gc="git clone"
alias ga="git add ."
alias gs="git status"
alias gcm="git commit -m"
alias gpsh="git push"
alias gpl="git pull"
"""


daivasmara_path = "~/.oh-my-zsh/themes/daivasmara.zsh-theme"
daivasmara_theme = """
MODE_INDICATOR="%{$fg_bold[red]%}❮%{$reset_color%}%{$fg[red]%}❮❮%{$reset_color%}"
local return_status="%{$fg[red]%}%(?..⏎)%{$reset_color%} "

ZSH_THEME_GIT_PROMPT_PREFIX="|"
ZSH_THEME_GIT_PROMPT_SUFFIX="%{$reset_color%}"
ZSH_THEME_GIT_PROMPT_DIRTY="%{$fg_bold[red]%} ⚡%{$reset_color%}"
ZSH_THEME_GIT_PROMPT_AHEAD="%{$fg_bold[red]%} !%{$reset_color%}"
ZSH_THEME_GIT_PROMPT_CLEAN="%{$fg_bold[green]%} ✓%{$reset_color%}"

ZSH_THEME_GIT_PROMPT_ADDED="%{$fg[green]%} ✚"
ZSH_THEME_GIT_PROMPT_MODIFIED="%{$fg[blue]%} ✹"
ZSH_THEME_GIT_PROMPT_DELETED="%{$fg[red]%} ✖"
ZSH_THEME_GIT_PROMPT_RENAMED="%{$fg[magenta]%} ➜"
ZSH_THEME_GIT_PROMPT_UNMERGED="%{$fg[yellow]%} ═"
ZSH_THEME_GIT_PROMPT_UNTRACKED="%{$fg[cyan]%} ✭"

# Format for git_prompt_long_sha() and git_prompt_short_sha()
ZSH_THEME_GIT_PROMPT_SHA_BEFORE="◯  %{$fg_bold[yellow]%}"
ZSH_THEME_GIT_PROMPT_SHA_AFTER="%{$reset_color%}"

function prompt_char() {
  echo "%{$fg[red]%}$%{$reset_color%}"
}

# Colors vary depending on time lapsed.
ZSH_THEME_GIT_TIME_SINCE_COMMIT_SHORT="%{$fg[green]%}"
ZSH_THEME_GIT_TIME_SHORT_COMMIT_MEDIUM="%{$fg[yellow]%}"
ZSH_THEME_GIT_TIME_SINCE_COMMIT_LONG="%{$fg[red]%}"
ZSH_THEME_GIT_TIME_SINCE_COMMIT_NEUTRAL="%{$fg[cyan]%}"

# Determine the time since last commit. If branch is clean,
# use a neutral color, otherwise colors will vary according to time.
function git_time_since_commit() {
    if git rev-parse --git-dir > /dev/null 2>&1; then
        # Only proceed if there is actually a commit.
        if [[ $(git log 2>&1 > /dev/null | grep -c "^fatal: bad default revision") == 0 ]]; then
            # Get the last commit.
            last_commit=`git log --pretty=format:'%at' -1 2> /dev/null`
            now=`date +%s`
            seconds_since_last_commit=$((now-last_commit))

            # Totals
            MINUTES=$((seconds_since_last_commit / 60))
            HOURS=$((seconds_since_last_commit/3600))

            # Sub-hours and sub-minutes
            DAYS=$((seconds_since_last_commit / 86400))
            SUB_HOURS=$((HOURS % 24))
            SUB_MINUTES=$((MINUTES % 60))

            if [[ -n $(git status -s 2> /dev/null) ]]; then
                if [ "$MINUTES" -gt 30 ]; then
                    COLOR="$ZSH_THEME_GIT_TIME_SINCE_COMMIT_LONG"
                elif [ "$MINUTES" -gt 10 ]; then
                    COLOR="$ZSH_THEME_GIT_TIME_SHORT_COMMIT_MEDIUM"
                else
                    COLOR="$ZSH_THEME_GIT_TIME_SINCE_COMMIT_SHORT"
                fi
            else
                COLOR="$ZSH_THEME_GIT_TIME_SINCE_COMMIT_NEUTRAL"
            fi

            if [ "$HOURS" -gt 24 ]; then
                echo "[$COLOR${DAYS}d${SUB_HOURS}h${SUB_MINUTES}m%{$reset_color%}]"
            elif [ "$MINUTES" -gt 60 ]; then
                echo "[$COLOR${HOURS}h${SUB_MINUTES}m%{$reset_color%}]"
            else
                echo "[$COLOR${MINUTES}m%{$reset_color%}]"
            fi
        else
            COLOR="$ZSH_THEME_GIT_TIME_SINCE_COMMIT_NEUTRAL"
            echo "[$COLOR~]"
        fi
    fi
}

PROMPT='
%{$fg[yellow]%}%m%{$reset_color%}%{$reset_color%} %{$fg[red]%}%(5~|%-1~/…/%3~|%4~) %{$reset_color%}$(git_prompt_short_sha)$(git_prompt_info)
$(prompt_char) '

RPROMPT='${return_status}$(git_time_since_commit)$(git_prompt_status)%{$reset_color%}'

"""

s("touch ~/.zshrc")
s(f"touch {daivasmara_path}")
s(f"sudo chmod 777 {daivasmara_path}")

with open(p.expanduser("~/.zshrc"), "w") as f:
    f.write(zsh_config)

with open(p.expanduser(daivasmara_path), "w") as f:
    f.write(daivasmara_theme)
