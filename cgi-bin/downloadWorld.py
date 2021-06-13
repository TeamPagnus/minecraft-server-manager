#!/usr/bin/python
# -*- coding: utf-8 -*-

CGI_DIR = "cgi_bin/"
MINECRAFT_DIR = "minecraft/"

import cgi

# Headers
print("Content-Type: text/html")
print()

import cgitb
cgitb.enable()

# Core.
from os import walk
import shutil

def zip_world(world):
    shutil.make_archive(MINECRAFT_DIR + f"{world}.zip", 'zip', MINECRAFT_DIR + world)
    link = f"<a href=\"/{MINECRAFT_DIR + world}.zip\">{world}.zip</a> is ready to be downloaded."
    print(link)

EXCEPTION = ["logs"]

worlds = next(walk(MINECRAFT_DIR))[1]
for f in EXCEPTION:
    worlds.remove(f)

args = cgi.FieldStorage()

try:
    world = args["level-name"].value
except Exception:
    print("Wrong request.")
    assert False

if '/' in world:
    print("Wrong request.")
    assert False

if world not in worlds:
    print("Wrong request.")
    assert False

zip_world(world)
