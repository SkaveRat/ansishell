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

argparser.add_argument("env", help="name of environment", default="default", nargs="?")
argparser.add_argument("group", help="ansible group", nargs="?")
argparser.add_argument("-l", help="list groups", action="store_true")
argparser.add_argument("-e", help="list environments", action="store_true")
args = argparser.parse_args()

first_argument = args.env
second_argument = args.group

if second_argument is None and not args.l:
    # We only get one argument. Use default env and set given parameter as group
    env = "default"
    group = first_argument
else:
    env = first_argument
    group = second_argument

inventory_path = dotfile.get("inventory", env)
shell_command = dotfile.get("config", "command")

inventory_manager = inventory.Inventory(inventory_path)

if args.e:
    print("Configured groups:")
    for environment in environments:
        print(environment)
    exit(0)

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