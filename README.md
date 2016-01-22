# Ansishell

A small tool to quickly open an ansible group in multi-ssh

## INI file

create an `.ansishell` file in your home directory:

```ini
[inventory]
default=/home/foobar/myproject/dev_inventory
dev=/home/foobar/myproject/dev_inventory
production=/home/foobar/myproject/production_inventory
```

## Usage

For default environment, you can just use the group name as a parameter:

`./ansishell web`

For a specific environment, use it as first parameter:

`./ansishell dev web`