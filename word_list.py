import random

word_list = [
"whistle", "crimson", "jungle", "orbit", "flavor", "tumble", "glimmer", "hazard", "quiver", "sizzle",
"plasma", "ripple", "snatch", "velvet", "twinkle", "gadget", "mystic", "puzzle", "flicker", "breeze",
"clover", "sparkle", "echo", "drizzle", "fumble", "glitch", "hollow", "juggle", "knuckle", "latch",
"mumble", "nuzzle", "opaque", "paddle", "quartz", "rubble", "scoff", "trickle", "umpire", "vortex",
"waddle", "yonder", "zephyr", "amber", "blizzard", "cascade", "doodle", "ember", "flick", "gobble",
"hurdle", "ignite", "jigsaw", "kettle", "lunar", "mosaic", "nibble", "ooze", "plunge", "quack",
"riddle", "swoosh", "throttle", "unravel", "vanish", "whisk", "yelp", "zipper", "alchemy", "bramble",
"crackle", "dazzle", "entwine", "fizz", "grumble", "hatch", "inkling", "jolt", "knot", "lurk",
"mirth", "nudge", "obscure", "pounce", "quirk", "rustle", "slither", "tangle", "uplift", "vivid"
]
gamedata = {"num":0 ,
            "chosen_word":"none"
            }
def randomizer():
    WORDNUM = random.randrange(90)
    return gamedata.update({"num": WORDNUM})



def word_of_game():
    chosen_word = word_list[gamedata.get("num")]
    gamedata.update({"chosen_word": chosen_word})


def full_game_data():
    randomizer()
    word_of_game()
    return gamedata.get("chosen_word")


if __name__ == "__main__":
    print(full_game_data())
