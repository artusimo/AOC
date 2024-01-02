

class Ingredient:

    def __init__(self, name, capa, dura:int, flav:int, text:int, calo:int):
        self.name = name
        self.capacity = int(capa)
        self.durability = int(dura)
        self.flavour = int(flav)
        self.texture = int(text)
        self.kalories = int(calo)


class Cookie:

    def __init__(self, ingreds, vec):
        self.ingredients = ingreds
        self.vector = vec

    #@property
    def get_ingr(self, ingr_name):
        i = self.ingredients.index(ingr_name)
        return self.vector[i]


f = open('myapp\input_data.txt', 'r')
rows = f.read().splitlines()

ingreds = {}
for row in rows:
    rows_as_list = row.split(' ')
    name = rows_as_list[0][:-1]
    capa = rows_as_list[2][:-1]
    dura = rows_as_list[4][:-1]
    flav = rows_as_list[6][:-1]
    text = rows_as_list[8][:-1]
    calo = rows_as_list[10]
    ingreds[name] = Ingredient(name, capa, dura, flav, text, calo)

def get_vec():
    for r in range(0, 101):
        print(r)
        for s in range(0, 101):
            for y in range(0, 101):
                for e in range(0, 101):
                    if r + s + y + e == 100:
                        vec = (r, s, y, e)
                        yield vec

ob_max = 0
gen = get_vec()
for vec in gen:
    c = Cookie([i for i in ingreds.keys()], vec)

    mr = c.get_ingr('Sugar')
    ms = c.get_ingr('Sprinkles')
    my = c.get_ingr('Candy')
    me = c.get_ingr('Chocolate')

    cr = ingreds['Sugar'].capacity
    cs = ingreds['Sprinkles'].capacity
    cy = ingreds['Candy'].capacity
    ce = ingreds['Chocolate'].capacity

    dr = ingreds['Sugar'].durability
    ds = ingreds['Sprinkles'].durability
    dy = ingreds['Candy'].durability
    de = ingreds['Chocolate'].durability

    fr = ingreds['Sugar'].flavour
    fs = ingreds['Sprinkles'].flavour
    fy = ingreds['Candy'].flavour
    fe = ingreds['Chocolate'].flavour

    tr = ingreds['Sugar'].texture
    ts = ingreds['Sprinkles'].texture
    ty = ingreds['Candy'].texture
    te = ingreds['Chocolate'].texture

    kr = ingreds['Sugar'].kalories
    ks = ingreds['Sprinkles'].kalories
    ky = ingreds['Candy'].kalories
    ke = ingreds['Chocolate'].kalories

#rovnice
    C = mr*cr + ms*cs + my*cy + me*ce
    D = mr*dr + ms*ds + my*dy + me*de
    F = mr*fr + ms*fs + my*fy + me*fe
    T = mr*tr + ms*ts + my*ty + me*te
    K = mr*kr + ms*ks + my*ky + me*ke

    C = 0 if C < 0 else C
    D = 0 if D < 0 else D
    F = 0 if F < 0 else F
    T = 0 if T < 0 else T

    ob = C*D*T*F
    #print("ObjFuncVal: ", ob)

    if ob_max < ob:
        if K == 500:
            ob_max = ob





print(ob_max)

pass