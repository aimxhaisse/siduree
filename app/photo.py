from PIL import Image

LARGE_WIDTH = 1920
MEDIUM_WIDTH = 640
SMALL_WIDTH = 320
OUTPUT_DIR = 'app/static/uploads/'

def resize(w, path, name, kind):
    im = Image.open(path)
    r = float(im.size[1]) / float(im.size[0])
    h = int(float(w) * float(r))
    res = im.resize((w, h), Image.ANTIALIAS)
    where = '%s/%s-%s.jpg' % (OUTPUT_DIR, name, kind)
    res.save(where)
    return where

def small(path, name):
    return resize(SMALL_WIDTH, path, name, 'small')

def medium(path, name):
    return resize(MEDIUM_WIDTH, path, name, 'medium')

def large(path, name):
    return resize(LARGE_WIDTH, path, name, 'large')

def original(path, name):
    im = Image.open(path)
    where = '%s/%s-original.jpg' % (OUTPUT_DIR, name)
    im.save(where)
    return where
