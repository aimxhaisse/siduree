#!flask/bin/python

import argparse
import subprocess
from app import db, models
from random import random

parser = argparse.ArgumentParser()
parser.add_argument("command", help = "[dev-init]")
args = parser.parse_args();

def get_words():
    words = []
    with open('/usr/share/dict/cracklib-small', 'r') as d:
        for line in d.readlines():
            words.append(line.strip())
    return words

words = get_words()

def random_sentence(size = 10):
    sentence = []
    for i in range(size):
        sentence.append(words[int(len(words) * random())])
    return ' '.join(sentence)

def populate():
    u = models.User()
    u.create('mxs', 'mxs@sbrk.org', 'mxs')
    db.session.add(u)
    db.session.commit()

    for i in range(3):
        j = models.Journey()
        j.create(random_sentence(), random_sentence(), u.id)
        db.session.add(j)
        db.session.commit()

        for k in range(3):
            s = models.Slide()
            s.create(random_sentence(), random_sentence(), j.id)
            db.session.add(s)
            db.session.commit()

            for l in range(3):
                p = models.Photo()
                p.create(random_sentence(), random_sentence(), s.id, 'path')
                db.session.add(p)
                db.session.commit()

def main(what):
    if what == "dev-init":
        subprocess.call("rm -f siduree.db", shell = True)
        db.create_all()
        populate()
        
if __name__ == '__main__':
    main(args.command)
