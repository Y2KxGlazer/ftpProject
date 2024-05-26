# Standard Imports
import pathlib

# External Imports
import pyftpdlib

# User-Defined Imports
#import eventqueue
#import data
from ftpserver import UD_Server


# Initialize EventQueue
#events = eventqueue.EventQueue()


# Initialize Data
noFile = True
while noFile:
    path_to_file = input("Enter a file path")
    path_to_file = path_to_file.replace('"', '')
    try:
        if pathlib.Path(path_to_file).is_file():
            with open(path_to_file, "rb") as file:
                #events.appendEvent("File Read in Progress")
                data_bin = data.Data(file)
                #events.appendEvent("Read Success", eventID=123)
                noFile = False

                #print(data_bin.bin_data.read())
                break
        else:
            print("No File Found!")
    except Exception as e:
        print(f"Error: {e}")


# Authorization
n1 = "Username" # Auth Username, 
pw = "ThePassword" # Auth Password

# Server Initialization
server = UD_Server()
server.add_user(n1, pw)
server.ftp_start()
