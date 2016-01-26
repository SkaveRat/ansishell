#!/usr/bin/env python2
from ansible import inventory
import subprocess
import ConfigParser
import sys
from os.path import expanduser


dotfile = ConfigParser.ConfigParser()
home = expanduser("~")
dotfile.read(home + "/.ansishell")

args = sys.argv

environments = dotfile.options("inventory")
config = dotfile.options("config")

# TODO check for missing defaults

env = "default"
group = args[1]

if len(args) >= 3:
    env = args[1]
    group = args[2]

inventory_path = dotfile.get("inventory", env)
shell_command = dotfile.get("config", "command")

inventory_manager = inventory.Inventory(inventory_path)
hosts = inventory_manager.list_hosts(group)

if len(hosts) == 0:
    print("No hosts found")
    exit(1)

args = [shell_command] + hosts

subprocess.call(args)