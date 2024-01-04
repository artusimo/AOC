# --- Day 15: Science for Hungry People ---
# Today, you set out on the task of perfecting your milk-dunking cookie recipe. All you have to do is find the right balance of ingredients.

# Your recipe leaves room for exactly 100 teaspoons of ingredients. You make a list of the remaining ingredients you could use to finish the recipe (your puzzle input) and their properties per teaspoon:

# capacity (how well it helps the cookie absorb milk)
# durability (how well it keeps the cookie intact when full of milk)
# flavor (how tasty it makes the cookie)
# texture (how it improves the feel of the cookie)
# calories (how many calories it adds to the cookie)
# You can only measure ingredients in whole-teaspoon amounts accurately, and you have to be accurate so you can reproduce your results in the future. The total score of a cookie can be found by adding up each of the properties (negative totals become 0) and then multiplying together everything except calories.

# For instance, suppose you have these two ingredients:

# Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
# Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
# Then, choosing to use 44 teaspoons of butterscotch and 56 teaspoons of cinnamon (because the amounts of each ingredient must add up to 100) would result in a cookie with the following properties:

# A capacity of 44*-1 + 56*2 = 68
# A durability of 44*-2 + 56*3 = 80
# A flavor of 44*6 + 56*-2 = 152
# A texture of 44*3 + 56*-1 = 76
# Multiplying these together (68 * 80 * 152 * 76, ignoring calories for now) results in a total score of 62842880, which happens to be the best score possible given these ingredients. If any properties had produced a negative total, it would have instead become zero, causing the whole score to multiply to zero.

# --- Part Two ---
# Your cookie recipe becomes wildly popular! Someone asks if you can make another recipe that has exactly 500 calories per cookie (so they can use it as a meal replacement). Keep the rest of your award-winning process the same (100 teaspoons, same ingredients, same scoring system).

# For example, given the ingredients above, if you had instead selected 40 teaspoons of butterscotch and 60 teaspoons of cinnamon (which still adds to 100), the total calorie count would be 40*8 + 60*3 = 500. The total score would go down, though: only 57600000, the best you can do in such trying circumstances.

# Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you can make with a calorie total of 500?
#--------------------------------
#Solution:

#represents cooking component (e.g. sugar)
class Ingredient:

    def __init__(self, name, capa, dura:int, flav:int, text:int, calo:int):
        self.name = name
        self.capacity = int(capa)
        self.durability = int(dura)
        self.flavour = int(flav)
        self.texture = int(text)
        self.kalories = int(calo)

#Cookie is made of components
class Cookie:

    def __init__(self, vec:tuple):
        self.vector = vec

    #get how many scoops of given ingredient the cookie has
    def get_ingr_amount(self, ingr_name):
        #ingredient number in global list of available ingredients
        ingredient_list = [i for i in INGREDS.keys()] 
        ord = ingredient_list.index(ingr_name)
        return self.vector[ord]

#parse flat file input with rows as Ingredient object attributes
def load_input():
    f = open('myapp\input_data.txt', 'r')
    rows = f.read().splitlines()

    #register of avalailable ingredients and their properties
    global INGREDS
    INGREDS = {}
    for row in rows:
        rows_as_list = row.split(' ')
        name = rows_as_list[0][:-1]
        capa = rows_as_list[2][:-1]
        dura = rows_as_list[4][:-1]
        flav = rows_as_list[6][:-1]
        text = rows_as_list[8][:-1]
        calo = rows_as_list[10]
        INGREDS[name] = Ingredient(name, capa, dura, flav, text, calo)


scoops_avail = 101 #amount of ingredients available from instructions
#vector generator representing scoops amount
def get_vec():
    for r in range(0, scoops_avail):    #sugar scoops
        for s in range(0, scoops_avail):    #sprinkles scoops
            for y in range(0, scoops_avail):    #candy scoops
                for e in range(0, scoops_avail):    #chocolate scoops
                    if r + s + y + e == 100:    #linear combination must add up to 100 scoops
                        vec = (r, s, y, e)
                        yield vec


def find_max():

    global ob_max

    #get scoops vector generator
    gen = get_vec()

    #get vector from generator
    for vec in gen:

        #create cookie by new properties by assigning vector to ingredients
        c = Cookie(vec)

        #scoops of ingredient in current cookie
        mr = c.get_ingr('Sugar')
        ms = c.get_ingr('Sprinkles')
        my = c.get_ingr('Candy')
        me = c.get_ingr('Chocolate')

        #get properties of each ingredient
        (cr, cs, cy, ce) = [x.capacity for x in INGREDS.values()]
        (dr, ds, dy, de) = [x.durability for x in INGREDS.values()]
        (fr, fs, fy, fe) = [x.flavour for x in INGREDS.values()]
        (tr, ts, ty, te) = [x.texture for x in INGREDS.values()]
        (kr, ks, ky, ke) = [x.kalories for x in INGREDS.values()]

        #equation system describing cookie properties, m*: amount of scoops of ingredient *
        C = mr*cr + ms*cs + my*cy + me*ce   #capacity
        D = mr*dr + ms*ds + my*dy + me*de   #durability
        F = mr*fr + ms*fs + my*fy + me*fe   #flavour
        T = mr*tr + ms*ts + my*ty + me*te   #texture
        K = mr*kr + ms*ks + my*ky + me*ke   #kalories

        #constraints (feasibility region is positive, as per instructions)
        C = 0 if C < 0 else C
        D = 0 if D < 0 else D
        F = 0 if F < 0 else F
        T = 0 if T < 0 else T

        #objective function (as per instructions)
        ob = C*D*T*F

        #find objective function maximum
        if ob_max < ob:
            if K == 500: #additinal constraint - a cooking must be just of 500 cal
                ob_max = ob


#init objective function value at start
ob_max = 0

load_input()
find_max()
print(ob_max)

