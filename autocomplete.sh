_script()
{
  _script_commands=$(ansishell default -l| tail -n +2 | tr "\n" " ")

  local cur prev
  COMPREPLY=()
  cur="${COMP_WORDS[COMP_CWORD]}"
  COMPREPLY=( $(compgen -W "${_script_commands}" -- ${cur}) )

  return 0
}
complete -o nospace -F _script ansishell