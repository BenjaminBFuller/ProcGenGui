import noise
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
from PIL import Image
from imageio import imwrite
import random
import colorsets as cs

shape = (800, 800)  # USER OPTIONAL: output size (x,y)
scale = 250  # USER OPTIONAL: higher zoomed in factor = higher number
octaves = 7  # USER OPTIONAL: number of layers; more layers = more detail added
persistence = 0.5  # amplitude that each octave contributes to overall shape
lacunarity = 2.0  # frequency of detail at each octave
seed = np.random.randint(0, 100)
world = np.zeros(shape)
color_world = np.zeros(world.shape + (3,))


def generate_base_map(shape, scale, octaves):
    for i in range(shape[0]):
        for j in range(shape[1]):
            world[i][j] = noise.pnoise2(i / scale,
                                        j / scale,
                                        octaves=octaves,
                                        persistence=persistence,
                                        lacunarity=lacunarity,
                                        repeatx=1024,
                                        repeaty=1024,
                                        base=seed)


def add_color(world):
    island_gen(world, color_world)
    return color_world


def island_gen(world, color_world):
    for i in range(shape[0]):
        for j in range(shape[1]):
            if world[i][j] < 0:
                color_world[i][j] = cs.deep_blue
            elif world[i][j] < .05:
                color_world[i][j] = cs.blue
            elif world[i][j] < .075:
                color_world[i][j] = cs.shelf_blue
            elif world[i][j] < .1:
                rand_int = random.randint(0, 1)
                if rand_int == 0:
                    color_world[i][j] = cs.beach
                else:
                    color_world[i][j] = cs.beach2
            elif world[i][j] < .25:
                rand_int = random.randint(0, 2)
                if rand_int == 0:
                    color_world[i][j] = cs.green
                elif rand_int == 1:
                    color_world[i][j] = cs.dark_green
                else:
                    color_world[i][j] = cs.dark_green2
            elif world[i][j] < .275:
                rand_int = random.randint(0, 4)
                if rand_int == 0:
                    color_world[i][j] = cs.green
                elif rand_int == 1:
                    color_world[i][j] = cs.dark_green
                elif rand_int == 2:
                    color_world[i][j] = cs.dark_green2
                elif rand_int == 3:
                    color_world[i][j] = cs.mountain
                else:
                    color_world[i][j] = cs.mountain2
            elif world[i][j] < 0.35:
                rand_int = random.randint(0, 1)
                if rand_int == 0:
                    color_world[i][j] = cs.mountain
                else:
                    color_world[i][j] = cs.mountain2
            elif world[i][j] < 0.36:
                rand_int = random.randint(0, 3)
                if rand_int == 0:
                    color_world[i][j] = cs.mountain
                elif rand_int == 1:
                    color_world[i][j] = cs.mountain2
                else:
                    color_world[i][j] = cs.snow2
            elif world[i][j] < .42:
                rand_int = random.randint(0, 1)
                if rand_int == 0:
                    color_world[i][j] = cs.snow
                else:
                    color_world[i][j] = cs.snow2
            elif world[i][j] < 1.0:
                color_world[i][j] = cs.snow


def forest_gen(world, color_world):
    for i in range(shape[0]):
        for j in range(shape[1]):
            if world[i][j] < -0.2:
                random_int = random.randint(0, 1)
                if random_int == 0:
                    color_world[i][j] = cs.super_green
                elif random_int == 1:
                    color_world[i][j] = cs.forest_dark_green
            elif world[i][j] < -.1:
                random_int = random.randint(0, 1)
                if random_int == 0:
                    color_world[i][j] = cs.forest_dark_green
                elif random_int == 1:
                    color_world[i][j] = cs.forest_green
            elif world[i][j] < -.05:
                random_int = random.randint(0, 1)
                if random_int == 0:
                    color_world[i][j] = cs.dirt
                elif random_int == 1:
                    color_world[i][j] = cs.dark_brown
            elif world[i][j] < 0:
                random_int = random.randint(0, 1)
                if random_int == 0:
                    color_world[i][j] = cs.gray
                elif random_int == 1:
                    color_world[i][j] = cs.black
            elif world[i][j] < .05:
                random_int = random.randint(0, 1)
                if random_int == 0:
                    color_world[i][j] = cs.dirt
                elif random_int == 1:
                    color_world[i][j] = cs.dark_brown
            elif world[i][j] < .15:
                random_int = random.randint(0, 1)
                if random_int == 0:
                    color_world[i][j] = cs.forest_dark_green
                elif random_int == 1:
                    color_world[i][j] = cs.forest_green
            elif world[i][j] < 1:
                random_int = random.randint(0, 1)
                if random_int == 0:
                    color_world[i][j] = cs.super_green
                elif random_int == 1:
                    color_world[i][j] = cs.forest_dark_green


def create_img(world):
    new_world = add_color(world)
    color_world_uint8 = np.uint8(new_world)  # lossy conversion without this.
    imwrite('islands.png', color_world_uint8)


def open_img():
    background = Image.open('islands.png')
    background.show()


def set_biome(biome):
    biomes_dict = {
        "Islands": island_gen(world, color_world),
        "Forest": forest_gen(world, color_world),
        # "Desert Oasis": oasis_gen,
        # "Cherry Blossom": blossom_gen,
        # "Caves": cave_gen,
        # "Terrace": terrace_gen
    }
    add_color(world)
    chosen_biome = biomes_dict.get(biome)
    # chosen_biome(world, color_world)


def set_scale(given_scale):
    scale_dict = {
        "50": 50,
        "100": 100,
        "200": 200,
        "300": 300,
        "400": 400,
        "500": 500,
        "600": 600,
        "700": 700,
        "800": 800,
        "900": 900,
        "1000": 1000
    }
    scale = scale_dict.get(given_scale)


def set_shape(given_shape):
    shape_dict = {
        "400x400": (400, 400),
        "600x600": (600, 600),
        "800x800": (800, 800),
        "1000x1000": (1000, 1000),
        "1200x1200": (1200, 1200),
        "400x1200": (400, 1200)
    }
    shape = shape_dict.get(given_shape)


def set_octaves(given_octaves):
    octaves_dict = {
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10
    }
    octaves = octaves_dict.get(given_octaves)


def generate_map(given_biome, given_scale, given_shape, given_octaves):
    set_biome(given_biome)
    set_scale(given_scale)
    set_shape(given_shape)
    set_octaves(given_octaves)
    generate_base_map(shape, scale, octaves)
    add_color(world)
    create_img(world)
    open_img()

# my_dpi = 100  # set screen dots per inch

# grid = plt.figure(figsize=(float(background.size[0]) / my_dpi, float(background.size[1]) / my_dpi), dpi=my_dpi)
# ax = grid.add_subplot(111)

# grid.subplots_adjust(left=0, right=1, bottom=0, top=1)

# myInterval = 50  # USER OPTIONAL: each grid plot will be (myInterval x myInterval) pixels
# a = plticker.MultipleLocator(base=myInterval)
# ax.xaxis.set_major_locator(a)
# ax.yaxis.set_major_locator(a)

# Adds grid to image with set values
# USER OPTIONAL: linewidth = line thickness
# ax.grid(which='major', axis='both', linestyle='-', color='black', linewidth=1)

# ax.imshow(background)

# grid.savefig('islands_grid.png', dpi=my_dpi)

# im = Image.open('islands_grid.png')
# im.show()


# if __name__ == "__main__":
#   generate_map()
