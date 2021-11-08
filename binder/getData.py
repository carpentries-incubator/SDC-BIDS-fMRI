import osfclient.cli as osfcli
from osfclient.api import OSF
from osfclient.utils import checksum
from osfclient.models.file import File
import os
from pathlib import Path

import argparse

# Lifted from
# https://github.com/osfclient/osfclient/blob/411497f67aae457a238f0b91ef864d38d6879918/osfclient/models/storage.py#L24
# to enable recursion from a folder object
RECURSE_KEYS = ('relationships', 'files', 'links', 'related', 'href')

def parse_download_list(download_list):

    with open(download_list, 'r') as f:
        to_download = [l.strip("\n") for l in f.readlines()]
        to_download = [
            p if p.startswith("/") else f"/{p}" for p in to_download
        ]

    return to_download


def main():

    parser = argparse.ArgumentParser(description="Download data from OSF project")
    parser.add_argument("directories", help="Text file containing list of directories"
                        " to download")
    parser.add_argument("destination", help="Root destination directory")
    parser.add_argument("--project", help="Project code")
    parser.add_argument("--username", help="Username for project")
    parser.add_argument("--password", help="Password for user")
    parser.add_argument("--token", help="Access token")

    args = parser.parse_args()

    # Override file config if provided
    config = osfcli.config_from_file()
    config.update({k:v for k,v in vars(args).items() if v is not None})

    osf = OSF(username=args.username, password=args.password, token=args.token)
    project = osf.project(config['project'])
    dest = args.destination
    to_download = parse_download_list(args.directories)
    for s in project.storages:
        download_folders(s, to_download, dest)


def download(folder, destination):
    '''
    Recursively download folders
    '''
    for file in folder._iter_children(folder._files_url, 'file', File, RECURSE_KEYS):

        path = file.path.strip("/")

        # Make directory structure if doesn't exist
        f_dir, _ = os.path.split(path)
        sub_dir = os.path.join(destination, f_dir)
        os.makedirs(sub_dir, exist_ok=True)
        write_path = os.path.join(destination, path)

        # If identical file already exists, skip
        if os.path.exists(write_path):
            if file.hashes.get("md5") == checksum(write_path):
                print(f"Identical file {write_path} already exists, skipping...")
                continue
        # Write file
        print("Downloading file:", file.path)
        with open(write_path, 'wb') as fp:
            file.write_to(fp)

def download_folders(storage, download_list, destination):
    '''
    Recursively identify folders to download from OSF
    Once detected, use OSF's download API to pull all
    files from folder
    '''

    def traverse(folder, targets):
        '''
        Traverse a folder
        '''
        nonlocal destination

        # Get all matching folders
        matches = []
        for t in targets:
            if is_relative_to(t, folder.path):
                if Path(t) == Path(folder.path):
                    # If an exact match is found, we're donesies with this tree
                    download(folder, destination)
                    return
                else:
                    matches.append(t)

        # No matches? No point in exploring further
        if not matches:
            return

        # For each sub-dir here traverse our matches
        for f in folder.folders:
            traverse(f, matches)

    for f in storage.folders:
        traverse(f, download_list)

def is_relative_to(a, b):
    '''
    Check if path a is relative to b
    '''

    if not isinstance(a, Path):
        a = Path(a)
    if not isinstance(b, Path):
        b = Path(b)

    try:
        value = a.relative_to(b)
    except ValueError:
        return
    else:
        return value

if __name__ == "__main__":
    main()
