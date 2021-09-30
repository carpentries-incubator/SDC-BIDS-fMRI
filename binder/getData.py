import osfclient.cli as osfcli
from osfclient.api import OSF
from osfclient.utils import checksum
import os

import argparse

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

    with open(args.directories, 'r') as f:
        to_download = [l.strip("\n") for l in f.readlines()]
        to_download = [
            d[1:] if d.startswith("/") else d
            for d in to_download
        ]
        to_download = [
            d + "/" if not d.endswith("/") else d
            for d in to_download
        ]

    # Loop through project storage
    for store in project.storages:
        for f in store.files:

            # Remove beginning "/"
            path = f.path
            if f.path.startswith("/"):
                path = path[1:]

            # Check for hits
            matched = any([d for d in to_download if path.startswith(d)])
            if matched:

                # Make base-directory if not exists
                f_dir, _ = os.path.split(path)
                sub_dir = os.path.join(dest, f_dir)
                os.makedirs(sub_dir, exist_ok=True)
                write_path = os.path.join(dest, path)

                # If identical file already exists, skip
                if os.path.exists(write_path):
                    if f.hashes.get("md5") == checksum(write_path):
                        print("Identical file already exists, skipping...")
                        continue
                # Write file
                print("Downloading file:", f.path)
                with open(write_path, 'wb') as fp:
                    f.write_to(fp)

if __name__ == "__main__":
    main()
