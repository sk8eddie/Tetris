import collections
Coord = collections.namedtuple('coord', 'x y')


def translate_coord_to_screen(x, y):
    return Coord((x*20), (y*20))



