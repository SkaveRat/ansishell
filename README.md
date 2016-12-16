# Ansishell

A small tool to quickly ssh into an ansible host group

## Dependencies

* Ansible 2.2
* Python 3
* pyyaml
* jinja2

## INI file

create an `.ansishell` file in your home directory:

```ini
[inventory]
; "default" is required
default=/home/foobar/myproject/dev_inventory
dev=/home/foobar/myproject/dev_inventory
production=/home/foobar/myproject/production_inventory

[config]
; the command to open multiple shells. Needs to support syntax "$command $host1 $host2 ..."
command=mssh
```

## Installation

Add the `bin` dir or symlink the executable somewhere in your `$PATH`

## Bash completion

If you want bash completion, source the `bashcompletion.sh` or `bashcompletion.zsh.sh`

## Usage

For default environment, you can just use the group name as a parameter:

`ansishell web`

For a specific environment, use it the first parameter:

`ansishell dev web`

Unsure which groups are configured? Use group listing of an environment:

`ansishell dev -l`

Need a list of environments?

`ansishell -e`
