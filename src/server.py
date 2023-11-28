"""
Copyright (c) 2023 Combo Gang. All rights reserved.

This work is licensed under the terms of the MIT license.  
For a copy, see <https://opensource.org/licenses/MIT>.
"""
import os
from sys import platform
import shutil
from src import utils

def create_server(version: str, path: str, name: str, xmx: int, xms: int) -> bool:
    """
    Creates a Minecraft server.
    """
    if not os.path.exists(path):
        os.mkdir(path)
    if utils.download_bukkit_jar(version, path):
        os.mkdir(f"{path}/{name}")
        shutil.copyfile(f"{path}/craftbukkit-{version}.jar", f"{path}/{name}/craftbukkit.jar")
        with open(f"{path}/{name}/eula.txt", "w") as f:
            f.write("eula=true")
        if platform == "linux" or platform == "linux2" or platform == "darwin":
            with open(f"{path}/{name}/start.sh", "w") as f:
                f.write(f"java -Xmx{xmx}M -Xms{xms}M -jar craftbukkit.jar nogui")
        elif platform == "win32":
            with open(f"{path}/{name}/start.bat", "w") as f:
                f.write(f"java -Xmx{xmx}M -Xms{xms}M -jar craftbukkit.jar nogui")

def start_server(path: str, name: str) -> bool:
    """
    Starts a Minecraft server.
    """
    os.chdir(f"{path}/{name}")
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        os.system("./start.sh")
    elif platform == "win32":
        os.system("start.bat")
        
def stop_server(path: str, name: str) -> bool:
    """
    Stops a Minecraft server.
    """
    os.chdir(f"{path}/{name}")
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        os.system("killall java")
    elif platform == "win32":
        os.system("taskkill /f /im java.exe")
        
def delete_server(path: str, name: str) -> bool:
    """
    Deletes a Minecraft server.
    """
    os.chdir(path)
    shutil.rmtree(f"{path}/{name}")
    
def list_servers(path: str) -> list:
    """
    Lists all Minecraft servers.
    """
    servers = []
    for server in os.listdir(path):
        servers.append(server)
    return servers

def get_server_path(path: str, name: str) -> str:
    """
    Gets the path of a Minecraft server.
    """
    return f"{path}/{name}"

def open_folder(path: str) -> bool:
    """
    Opens the folder of a Minecraft server.
    """
    os.startfile(path)