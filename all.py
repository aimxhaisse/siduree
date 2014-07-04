#!flask/bin/python
# -*- coding: utf-8 -*-

import argparse
import subprocess
import os
from app import db, models
from random import random

parser = argparse.ArgumentParser()
parser.add_argument("command", help = "[dev-init]")
args = parser.parse_args();

def get_words():
    words = []
    try:
        with open('/usr/share/dict/cracklib-small', 'r') as d:
            for line in d.readlines():
                words.append(line.strip())
    except:
        pass
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

def populate_italy():
    u = models.User()
    u.create('mxs', 'mxs@sbrk.org', 'mxs')
    db.session.add(u)
    db.session.commit()

    j = models.Journey()
    j.create(u"Italy, June 2014", u"6 days trek in the Italian Alps in the national park of the Gran Paradiso.", u.id)
    db.session.add(j)
    db.session.commit()

    print "slide 1"

    s = models.Slide()
    s.create(u'Day 1: Colle del Nivolet, 2616m', u'21th June 2014', j.id)
    db.session.add(s)
    db.session.commit()

    p = models.Photo()
    p.create(u'Croce della Roley, 2310m', '', s.id, 'assets/italy/day_01/IMG_4257.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u'Piano del Nivolet, 2399m', '', s.id, 'assets/italy/day_01/IMG_4263.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u'Colle del Nivolet, 2612m', '', s.id, 'assets/italy/day_01/IMG_4283.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u'Valle dell\' Orco, 2585m', '', s.id, 'assets/italy/day_01/IMG_4286.jpg')
    db.session.add(p)
    db.session.commit()

    s.cover_id = p.id
    db.session.add(s)
    db.session.commit()

    p = models.Photo()
    p.create(u'Lac di Orco, 1912m', '', s.id, 'assets/italy/day_01/IMG_4290.jpg')
    db.session.add(p)
    db.session.commit()

    j.cover_id = s.id
    db.session.add(j)
    db.session.commit()

    print "slide 2"

    s = models.Slide()
    s.create(u'Day 2: Rifugio Noaschetta, 1549m', '22th June 2014', j.id)
    db.session.add(s)
    db.session.commit()

    p = models.Photo()
    p.create(u'Abandoned house near Pian Domeni, 1194m', '', s.id, 'assets/italy/day_02/IMG_4294.jpg')
    db.session.add(p)
    db.session.commit()

    s.cover_id = p.id
    db.session.add(s)
    db.session.commit()

    p = models.Photo()
    p.create(u'Valle dell\' Orco, 1167m', '', s.id, 'assets/italy/day_02/IMG_4298.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u'Tunnel to Noasca, 1146m', '', s.id, 'assets/italy/day_02/IMG_4308.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u'Break at Noasca, 1061m', '', s.id, 'assets/italy/day_02/IMG_4328.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u'Storm near Pian Segio, 1429m', '', s.id, 'assets/italy/day_02/IMG_4331.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u'Around Rifugio Noaschetta, 1549m', '', s.id, 'assets/italy/day_02/IMG_4336.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u'Rio Noaschetta, 1549m', '', s.id, 'assets/italy/day_02/IMG_4340.jpg')
    db.session.add(p)
    db.session.commit()

    print "slide 3"

    s = models.Slide()
    s.create(u"Day 3: Bivouac Ivrea, 2770m", "23th June 2014", j.id)
    db.session.add(s)
    db.session.commit()

    p = models.Photo()
    p.create(u"Vallone di Noaschetta, 1568m", "", s.id, 'assets/italy/day_03/IMG_4353.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u"Vallone di Noaschetta, 1589m", "", s.id, 'assets/italy/day_03/IMG_4357.jpg')
    db.session.add(p)
    db.session.commit()

    s.cover_id = p.id
    db.session.add(s)
    db.session.commit()

    p = models.Photo()
    p.create(u"Vallone di Noaschetta, 1804m", "", s.id, 'assets/italy/day_03/IMG_4359.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u"Crossroads, 2414m", "", s.id, 'assets/italy/day_03/IMG_4370.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u"Around Piano della Bruna, 2473m", "", s.id, 'assets/italy/day_03/IMG_4375.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u"Around Piano della Bruna, 2473m", "", s.id, 'assets/italy/day_03/IMG_4379.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u"Around Piano della Bruna, 2473m", "", s.id, 'assets/italy/day_03/IMG_4380.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u"A. la Motta, 2653m", "", s.id, 'assets/italy/day_03/IMG_4384.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u"Chamois near A. la Motta, 2653m", "", s.id, 'assets/italy/day_03/IMG_4393.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u"Near Bivouac Ivrea, 2770m", "", s.id, 'assets/italy/day_03/IMG_4396.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u"Near Bivouac Ivrea, 2770m", "", s.id, 'assets/italy/day_03/IMG_4398.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u"Bivouac Ivrea, 2770m", "", s.id, 'assets/italy/day_03/IMG_4412.jpg')
    db.session.add(p)
    db.session.commit()

    print "slide 4"

    s = models.Slide()
    s.create(u'Day 4: Colle dei Becchi, 2990m', u'24th June 2014', j.id)
    db.session.add(s)
    db.session.commit()    

    p = models.Photo()
    p.create(u'Bivouac Ivrea, 2770m', '', s.id, 'assets/italy/day_04/IMG_4424.jpg')
    db.session.add(p)
    db.session.commit()

    s.cover_id = p.id
    db.session.add(s)
    db.session.commit()

    p = models.Photo()
    p.create(u'Becchi della Tribolazione, 2836m', '', s.id, 'assets/italy/day_04/IMG_4433.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u'Becchi della Tribolazione, 2836m', '', s.id, 'assets/italy/day_04/IMG_4438.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u'Colle dei Becchi, 2990m', '', s.id, 'assets/italy/day_04/IMG_4443.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u'Colle dei Becchi, 2665m', '', s.id, 'assets/italy/day_04/IMG_4461.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u'Near Rifugio Pontese, 2200m', '', s.id, 'assets/italy/day_04/IMG_4469.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u'Lago di Teleccio, 1917m', '', s.id, 'assets/italy/day_04/IMG_4477.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u'Near Rifugio Pontese, 2200m', '', s.id, 'assets/italy/day_04/IMG_4487.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u'Near Rifugio Pontese, 2200m', '', s.id, 'assets/italy/day_04/IMG_4490.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u'Scala di Teleccio, 1740m', '', s.id, 'assets/italy/day_04/IMG_4511.jpg')
    db.session.add(p)
    db.session.commit()

    print "slide 5"

    s = models.Slide()
    s.create(u'Day 5: Back to Valsavarenche, 1960m', u'25th June 2014', j.id)
    db.session.add(s)
    db.session.commit()

    p = models.Photo()
    p.create(u'Lago di Ceresole Reale, 1588m', '', s.id, 'assets/italy/day_05/IMG_4519.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u'Costa della Civetta, 2593m', '', s.id, 'assets/italy/day_05/IMG_4522.jpg')
    db.session.add(p)
    db.session.commit()

    s.cover_id = p.id
    db.session.add(s)
    db.session.commit()

    p = models.Photo()
    p.create(u'Break at Colle del Nivolet, 2612m', '', s.id, 'assets/italy/day_05/IMG_4567.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u'Marmots in Piano del Nivolet, 2399m', '', s.id, 'assets/italy/day_05/IMG_4580.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u'Piano del Nivolet, 2399m', '', s.id, 'assets/italy/day_05/IMG_4588.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u'Costa Arolley, 2310m', '', s.id, 'assets/italy/day_05/IMG_4590.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u'Costa Arolley, 2310m', '', s.id, 'assets/italy/day_05/IMG_4593.jpg')
    db.session.add(p)
    db.session.commit()

    print "slide 6"

    s = models.Slide()
    s.create(u'Day 6: Pian della Tumetta, 2418m', u'26th June 2014', j.id)
    db.session.add(s)
    db.session.commit()

    p = models.Photo()
    p.create(u'Aosta, city center', '', s.id, 'assets/italy/day_06/IMG_4599.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u'Aosta, city center', '', s.id, 'assets/italy/day_06/IMG_4602.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u'Cogne, the church', '', s.id, 'assets/italy/day_06/IMG_4605.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u'Back into the wild, an ibex', '', s.id, 'assets/italy/day_06/IMG_4630.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u'Near Grandzetta, 2140m', '', s.id, 'assets/italy/day_06/IMG_4636.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u'Near Grandzetta, 2140m', '', s.id, 'assets/italy/day_06/IMG_4640.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u'Pian de la Tumetta, 2418m', '', s.id, 'assets/italy/day_06/IMG_4657.jpg')
    db.session.add(p)
    db.session.commit()

    s.cover_id = p.id
    db.session.add(s)
    db.session.commit()

    p = models.Photo()
    p.create(u'Pian de la Tumetta, 2418m', '', s.id, 'assets/italy/day_06/IMG_4662.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u'Pian de la Tumetta, 2418m', '', s.id, 'assets/italy/day_06/IMG_4671.jpg')
    db.session.add(p)
    db.session.commit()

    print "slide 7"

    s = models.Slide()
    s.create(u'Day 7: Gran Lauson, 3101m', u'27th June 2014', j.id)
    db.session.add(s)
    db.session.commit()

    p = models.Photo()
    p.create(u'Ibex in the morning near Toule, 1994m', '', s.id, 'assets/italy/day_07/IMG_4675.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u'Near La Pascieu, 2114m', '', s.id, 'assets/italy/day_07/IMG_4679.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u'Near Rifugio V. Sella, 2584m', '', s.id, 'assets/italy/day_07/IMG_4681.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u'Near Gran Lauson, 2844m', '', s.id, 'assets/italy/day_07/IMG_4683.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u'Near Gran Lauson, 2844m', '', s.id, 'assets/italy/day_07/IMG_4684.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u'Near Gran Lauson, 3000m', '', s.id, 'assets/italy/day_07/IMG_4686.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u'Near Gran Lauson, 3000m', '', s.id, 'assets/italy/day_07/IMG_4692.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u'Near Gran Lauson, 3101m', '', s.id, 'assets/italy/day_07/IMG_4693.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u'Near Rifugio V. Sella, 2584m', '', s.id, 'assets/italy/day_07/IMG_4697.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u'Tramouial, 2227m', '', s.id, 'assets/italy/day_07/IMG_4702.jpg')
    db.session.add(p)
    db.session.commit()

    p = models.Photo()
    p.create(u'Near La Pascieu, 2114m', '', s.id, 'assets/italy/day_07/IMG_4708.jpg')
    db.session.add(p)
    db.session.commit()

    s.cover_id = p.id
    db.session.add(s)
    db.session.commit()

def main(what):
    if what == "dev-init":
        subprocess.call("rm -rf siduree.db app/static/uploads", shell = True)
        subprocess.call("mkdir -p app/static/uploads", shell = True)
        db.create_all()
        populate_italy()

if __name__ == '__main__':
    main(args.command)
