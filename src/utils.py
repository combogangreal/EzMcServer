"""
Copyright (c) 2023 Combo Gang. All rights reserved.

This work is licensed under the terms of the MIT license.  
For a copy, see <https://opensource.org/licenses/MIT>.
"""
import requests
import shutil
from bs4 import BeautifulSoup

def download_bukkit_jar(version: str, server_path: str) -> bool:
    """
    Downloads the Bukkit.jar file from the Bukkit download page.
    """
    url = f"https://getbukkit.org/download/craftbukkit/{version}/craftbukkit-{version}.jar"
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(f"{server_path}/craftbukkit-{version}.jar", "wb") as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
        return True
    else:
        return False
    
def get_craftbukkit_versions() -> list:
    """
    Returns a list of all available versions of CraftBukkit.
    """
    url = "https://getbukkit.org/download/craftbukkit"
    r = requests.get(url)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, "html.parser")
        versions = [a.text for a in soup.find_all("a")]
        return versions
    else:
        return []