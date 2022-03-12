from characters import barbarians, dragons


def rage_spell(King):
    if King.alive == True:
        King.rage_effect()
    for barb in barbarians:
        if barb.alive == True:
            barb.rage_effect()
    for dr in dragons:
        if dr.alive == True:
            dr.rage_effect()

def heal_spell(King):
    if King.alive == True:
        King.heal_effect()
    for barb in barbarians:
        if barb.alive == True:
            barb.heal_effect()
    for dr in dragons:
        if dr.alive == True:
            dr.heal_effect()