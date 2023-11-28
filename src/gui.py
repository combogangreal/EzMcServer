"""
Copyright (c) 2023 Combo Gang. All rights reserved.

This work is licensed under the terms of the MIT license.  
For a copy, see <https://opensource.org/licenses/MIT>.
"""
import os
import ttkbootstrap as ttk
from src.utils import get_craftbukkit_versions
from src.server import start_server, stop_server, open_folder, create_server

username = os.getenv("USERNAME")
main_path = f"C:/Users/{username}/Desktop/Minecraft Servers"

def _create_server():
    create_server(versionvar.get(), f"{main_path}/{servername.get()}", servername.get(), xmxvar.get(), xmsvar.get())

def list_servers():
    for server in os.listdir(main_path):
        # Adds the server in a gui and adds a start, stop, open folder buttons
        # to the gui.
        server_path = f"{main_path}/{server}"
        server_name = server.replace("_", " ")
        server_name = server_name.title()
        server_name = server_name.replace(" ", "")
        button = ttk.Button(master, text="Start Server", command=lambda: start_server(server_path))
        button.pack(pady=10)
        button = ttk.Button(master, text="Stop Server", command=lambda: stop_server(server_path))
        button.pack(pady=10)
        button = ttk.Button(master, text="Open Folder", command=lambda: open_folder(server_path))
        button.pack(pady=10)
    
    if not os.listdir(main_path):
        label = ttk.Label(master, text="No servers found.")
        label.pack(pady=10)

master = ttk.Window(title="Ez Minecraft Server")
master.geometry("400x300")
master.resizable(True, True)

title = ttk.Label(master, text="Ez Minecraft Server", font="Arial 18 bold")
title.pack(pady=10)

serverversionlabel = ttk.Label(master, text="Server Version")
serverversionlabel.pack(pady=10)

versionvar = ttk.StringVar(master)
versiondropdown = ttk.OptionMenu(master, versionvar, "1.20.1", *get_craftbukkit_versions())
versiondropdown.pack(pady=10)

servernamelabel = ttk.Label(master, text="Server Name")
servernamelabel.pack(pady=10)

servername = ttk.StringVar(master)
servernameentry = ttk.Entry(master, textvariable=servername)
servernameentry.pack(pady=10)

xmxvar = ttk.IntVar(master)
xmxvar.set(4096)
xmxlabel = ttk.Label(master, text="Xmx (MB) (Maximum Memory)", textvariable=xmxvar)
xmxlabel.pack(pady=10)

xmsvar = ttk.IntVar(master)
xmsvar.set(1024)
xmslabel = ttk.Label(master, text="Xms (MB) (Initial Memory)", textvariable=xmsvar)

runonready = ttk.BooleanVar(master)
runonready.set(False)
runonreadylabel = ttk.Checkbutton(master, text="Run on Ready", variable=runonready)
runonreadylabel.pack(pady=10)

servercreatebutton = ttk.Button(master, text="Create Server", command=_create_server)
servercreatebutton.pack(pady=10)

serverlistbutton = ttk.Button(master, text="Server List", command=list_servers)
serverlistbutton.pack(pady=10)