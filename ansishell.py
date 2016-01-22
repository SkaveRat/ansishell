#!/usr/bin/env python2
from ansible import inventory
import subprocess
import ConfigParser
import sys
from os.path import expanduser


config = ConfigParser.ConfigParser()
home = expanduser("~")
config.read(home + "/.ansishell")
args = sys.argv

environments = config.options("inventory")

# TODO check for missing defaults

env = "default"
group = args[1]

if len(args) >= 3:
    env = args[1]
    group = args[2]

inventory_path = config.get("inventory", env)

inventory_manager = inventory.Inventory(inventory_path)
hosts = inventory_manager.list_hosts(group)

args = ["mssh"] + hosts

subprocess.call(args)