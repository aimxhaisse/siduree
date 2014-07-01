#!flask/bin/python
# -*- coding: utf-8 -*-

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

def random_sentence(size = 5):
    sentence = []
    for i in range(size):
        sentence.append(words[int(len(words) * random())])
    return ' '.join(sentence)

def populate():
    u = models.User()
    u.create('mxs', 'mxs@sbrk.org', 'mxs')
    db.session.add(u)
    db.session.commit()

    """
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
                p.create(random_sentence(), random_sentence(), s.id, 'assets/lost.jpg')
                db.session.add(p)
                db.session.commit()
    """

    j = models.Journey()
    j.create(u"Italy, Juin 2014", u"Trek de 6 jours dans les Alpes Italiennes au sein du parc national du Gran Paradiso", u.id)
    db.session.add(j)
    db.session.commit()

    s = models.Slide()
    s.create(u"Colle Del Nivolet, 2616m", u"21 Juin 2014", j.id)
    db.session.add(s)
    db.session.commit()

    p = models.Photo()
    p.create(u"Vallone di Seiva", "", s.id, 'assets/italy/day_01/IMG_4257.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u"Vallone di Nivolet", "", s.id, 'assets/italy/day_01/IMG_4263.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u"Colle del Nivolet", "", s.id, 'assets/italy/day_01/IMG_4275.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u"Colle del Nivolet", "", s.id, 'assets/italy/day_01/IMG_4283.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u"Colle del Nivolet", "", s.id, 'assets/italy/day_01/IMG_4284.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u"Colle del Nivolet", "", s.id, 'assets/italy/day_01/IMG_4286.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u"Colle del Nivolet", "", s.id, 'assets/italy/day_01/IMG_4290.jpg')
    db.session.add(p)
    db.session.commit()

def main(what):
    if what == "dev-init":
        subprocess.call("rm -rf siduree.db app/static/uploads", shell = True)
        subprocess.call("mkdir -p app/static/uploads", shell = True)
        db.create_all()
        populate()

if __name__ == '__main__':
    main(args.command)
