#!flask/bin/python

import argparse
import subprocess
from app import db

parser = argparse.ArgumentParser()
parser.add_argument("command", help = "[dev-init]")
args = parser.parse_args();

def default_user():
    u = models.User('mxs', 'mxs', 'mxs@sbrk.org')
    db.session.add(u)
    db.session.commit()

def main(what):
    if what == "dev-init":
        subprocess.call("rm -f siduree.db", shell = True)
        db.create_all()
        default_user()
        
if __name__ == '__main__':
    main(args.command)
