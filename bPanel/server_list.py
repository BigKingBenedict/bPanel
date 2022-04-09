import os
import glob

def load_servers(user=str):
    users_servers = []

    all_folders = []
    for dir, sub_dirs, files in os.walk("servers/"):
       all_folders.extend(sub_dirs)
       if user in sub_dirs:
           users_servers.extend(sub_dirs)

    return users_servers       

    