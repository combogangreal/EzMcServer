"""
Copyright (c) 2023 Combo Gang. All rights reserved.

This work is licensed under the terms of the MIT license.  
For a copy, see <https://opensource.org/licenses/MIT>.
"""
import ttkbootstrap as ttk
import os
import shutil
def replace_whitespace_with_hyphen(text):
    new_text = ""
    for char in text:
        if char.isspace():
            new_text += "-"
        else:
            new_text += char
    return new_text

def createServer():
    print("Creating server...")
    if not os.path.exists(f"{directory.get()}"):
        os.mkdir(f"{directory.get()}")
    with open(f"{directory.get()}/start.bat", "w+") as f:
        f.write(f"java -Xmx{xmxvar.get()}m -Xms{xmsvar.get()}m -jar {directory.get()}/{variable.get()}")
    shutil.copy(f"./src/jars/{variable.get()}", f"{directory.get()}/{variable.get()}")
    os.system(f"cd {directory.get()}")
    os.system(f"{directory.get()}/start.bat")
    shutil.move("./eula.txt", f"{directory.get()}/eula.txt")
    shutil.move("./server.properties", f"{directory.get()}/server.properties")
    os.mkdir(f"{directory.get()}/logs")
    shutil.move("./logs/latest.log", f"{directory.get()}/logs/latest.log")
    with open(f"{directory.get()}/eula.txt") as f:
        for lines in f.readlines():
            if lines.startswith("eula=false"):
                lines = lines.replace("eula=false", "eula=true")
                with open(f"{directory.get()}/eula.txt", "w") as f:
                    f.write(lines)
    serverreadyvar.set("Server Ready For Usage!")
    print("Server ready, just run ./start.bat")
    

window = ttk.Window(themename="superhero", title="Minecraft Server Installer")
window.geometry("1000x1000")

window.columnconfigure(0, weight = 1)
window.columnconfigure(1, weight = 1)
window.columnconfigure(2, weight = 2)
window.rowconfigure(0, weight = 1)
window.rowconfigure(1, weight = 1)

frame = ttk.Frame(master=window).pack()
labelPryProt = ttk.Label(frame, text='Minecraft Server Installer', font='Helvetica 18 bold')
labelPryProt.pack()

files = filter(lambda x: x.endswith('.jar'), os.listdir('./src/jars'))

variable = ttk.StringVar(window)
variable.set("spigot-1.20.2.jar")

w = ttk.OptionMenu(window, variable, *files)
w.pack()

servernamevar = ttk.StringVar(window)
servernamevar.set("My Server")
servernamevar.set(f"{replace_whitespace_with_hyphen(servernamevar.get())}")
L1 = ttk.Label(window, text="Server Name")
L1.pack()
E1 = ttk.Entry(window, textvariable=servernamevar)
E1.pack()

xmxvar = ttk.StringVar(window)
xmxvar.set("4096")
L2 = ttk.Label(window, text="XMX Amount (Maxium Heap Memory) (In MegaBytes)")
L2.pack()
E2 = ttk.Entry(window, textvariable=xmxvar)
E2.pack()

xmsvar = ttk.StringVar(window)
xmsvar.set("2048")
L3 = ttk.Label(window, text="XMS Amount (Inital Heap Memory)")
L3.pack()
E3 = ttk.Entry(window, textvariable=xmxvar)
E3.pack()

directory = ttk.StringVar(window)
username = os.getenv('USERNAME')
directory.set(f"C:/Users/{username}/Desktop/{servernamevar.get()}")
L4 = ttk.Label(window, text="Server Directory (Where server files are located)")
L4.pack()
E4 = ttk.Entry(window, textvariable=directory)
E4.pack()

serverreadyvar = ttk.StringVar(window)
serverreadyvar.set("Server Not Ready")
serverreadylabel = ttk.Label(window, textvariable=serverreadyvar)
serverreadylabel.pack()

button = ttk.Button(master=frame, text="Create Server", command=createServer)
button.pack()
