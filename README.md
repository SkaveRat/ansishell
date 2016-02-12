# Ansishell

A small tool to quickly ssh into an ansible host group

## Dependencies

* Ansible
* Python2 ConfigParser

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

## Usage

For default environment, you can just use the group name as a parameter:

`./ansishell.py web`

For a specific environment, use it the first parameter:

`./ansishell.py dev web`

Unsure which groups are configured? Use group listing of an environment:

`./ansishell.py dev -l`

Need a list of environments?

`./ansishell.py -e`