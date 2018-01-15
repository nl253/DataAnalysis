#!/usr/bin/env python3

import os

docstring = f"""
{os.path.basename(__file__)}

Usage:
  {os.path.basename(__file__)} requirements
  {os.path.basename(__file__)} unzip <zipped_file.zip>
  {os.path.basename(__file__)} help

Options:
  -h --help     Show this screen.
"""

if __name__ == '__main__':
    from docopt import docopt

    os.chdir(os.path.dirname(__file__))
    doc = docopt(docstring)

    if doc["requirements"]:
        from subprocess import run
        run(["pip", "install", "--user", '--pre', "-r", "requirements.txt"])

    elif doc["unzip"] and doc["<zipped_file.zip>"]:
        import zipfile

        if not (
            doc["<zipped_file.zip>"]
            and zipfile.is_zipfile(doc["<zipped_file.zip>"])
        ):
            print("Please pass a valid path to a zip file.")
            raise FileNotFoundError()

        with zipfile.ZipFile(doc["<zipped_file.zip>"]) as zipped:
            zipped.extractall(path=os.path.dirname(doc["<zipped_file.zip>"]))
