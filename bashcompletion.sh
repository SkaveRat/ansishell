#!/usr/bin/env bash
_script()
{
  local envs env group
  COMPREPLY=()
  env="${COMP_WORDS[1]}" #first parameter

  #get list of environments
  envs=$(ansishell -e| tail -n +2 | tr "\n" " ")

  # given autocomplete is not an environment
  # autocomplete with default environment instead
  if ! [[ "${envs[@]}" =~ "${env}" ]]; then
    env="default"
  fi;

  _script_commands=$(ansishell ${env} -l| tail -n +2 | tr "\n" " ")
  COMPREPLY=( $(compgen -W "${_script_commands}" ) )

  return 0
}
complete -o nospace -F _script ansishell