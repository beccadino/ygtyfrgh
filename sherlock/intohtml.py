import os
import sys
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)

htmlHead = '<!DOCTYPE html>\n<html lang="en">\n<head>\n\t<meta charset="UTF-8">\n\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n\t<title>Sites From sherlock.py</title>\n</head>\n<body>'
htmlFoot = "</body>\n</html>"

def userError(str):
    print(Fore.RED+str)
def userWarn(str):
    print(f"{Fore.YELLOW}Warning: {str}")
def userFine(str):
    print(Fore.GREEN+str)

def run():
    if len(sys.argv) != 1 and len(sys.argv) < 3:
        username = sys.argv[1]
        linksFile = None
        try:
            if username.endswith(".txt"):
                linksFile = open(username, "r")
            else:
                linksFile = open(f"{username}.txt", "r")
            lines = linksFile.readlines()
            # removes the line at the end which isnt a link
            lines = lines[:-1]
            file = None
            if username.endswith(".txt"):
                userFine(f"Creating {username[:-4]}.html file...")
                file = open(f"{username[:-4]}.html", "w+")
            else:
                userFine(f"Creating {username}.html file...")
                file = open(f"{username}.html", "w+")
            file.write(htmlHead)
            for i in range(0, len(lines)):
                file.write(f"<input type=\"checkbox\" /><a href=\"{lines[i]}\" target=\"_blank\">{lines[i]}</a><br /><br />")
            file.write("\n"+htmlFoot)
            userFine("Action completed!")
        except:
            userError(f"No file with the name \"{username}.txt\"")
    else:
        if len(sys.argv) > 2:
            userError("Too many args!\nusage: py intohtml.py [filename(.txt optional)]")
        else:
            userError("Not enough args provided!\nusage: py intohtml.py [filename(.txt optional)]")

run()