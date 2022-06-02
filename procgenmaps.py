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
world = np.zeros(shape)
color_world = np.zeros(world.shape + (3,))


def generate_base_map(shape, scale, octaves):
    seed = np.random.randint(0, 100)
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


def island_gen():
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


def forest_gen():
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


def create_img():
    color_world_uint8 = np.uint8(color_world)  # lossy conversion without this.
    imwrite('islands.png', color_world_uint8)


def open_img():
    background = Image.open('islands.png')
    background.show()


def set_biome(given_biome):
    biomes_dict = {
        "Islands": island_gen,
        "Forest": forest_gen,
        # "Desert Oasis": oasis_gen,
        # "Cherry Blossom": blossom_gen,
        # "Caves": cave_gen,
        # "Terrace": terrace_gen
    }
    biomes_dict[given_biome]()


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
    return scale_dict.get(given_scale)


def set_shape(given_shape):
    shape_dict = {
        "400x400": (400, 400),
        "600x600": (600, 600),
        "800x800": (800, 800)
    }
    return shape_dict.get(given_shape)


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
    return octaves_dict.get(given_octaves)


def generate_map(given_biome, given_scale, given_shape, given_octaves):
    scale = set_scale(given_scale)
    shape = set_shape(given_shape)
    octaves = set_octaves(given_octaves)
    generate_base_map(shape, scale, octaves)
    set_biome(given_biome)
    create_img()
    open_img()


if __name__ == "__main__":
    set_biome("Islands")
