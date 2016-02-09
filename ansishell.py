#!/usr/bin/env python2
from ansible import inventory
import subprocess
import ConfigParser
import argparse
from os.path import expanduser, isfile


dotfile = ConfigParser.ConfigParser()
home = expanduser("~")
dotfile_path = home + "/.ansishell"

if not isfile(dotfile_path):
    print("~/.ansishell config not found")
    exit(1)

dotfile.read(dotfile_path)

argparser = argparse.ArgumentParser()

environments = dotfile.options("inventory")
config = dotfile.options("config")

# TODO check for missing defaults

argparser.add_argument("env", help="name of environment", default="default")
argparser.add_argument("group", help="ansible group", nargs="?")
argparser.add_argument("-l", help="name of environment", action="store_true")
args = argparser.parse_args()

env = args.env
group = args.group

inventory_path = dotfile.get("inventory", env)
shell_command = dotfile.get("config", "command")

inventory_manager = inventory.Inventory(inventory_path)

if args.l:
    inventory_manager = inventory.Inventory(inventory_path)
    print("Groups in %s:" % inventory_path)
    for group_item in inventory_manager.list_groups():
        print(group_item)
    exit(0)


hosts = inventory_manager.list_hosts(group)
if len(hosts) == 0:
    print("No hosts found")
    exit(1)

cmd_args = [shell_command] + hosts

subprocess.call(cmd_args)