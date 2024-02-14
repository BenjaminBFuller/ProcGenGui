# Procedural generation python file for generating images from GUI inputs

from noise import pnoise2
import numpy as np
from PIL import Image
from imageio import imwrite
import random
import colorsets as cs

# shape = (800, 800)  # USER OPTIONAL: output size (x,y)
# scale = 250  # USER OPTIONAL: higher zoomed in factor = higher number
# octaves = 7  # USER OPTIONAL: number of layers; more layers = more detail added
persistence = 0.5  # amplitude that each octave contributes to overall shape
lacunarity = 2.0  # frequency of detail at each octave


def generate_base_map(shape, scale, octaves, world):
    """Generates base map; perlin noise generation with user inputted parameters"""
    seed = np.random.randint(0, 100)
    for i in range(shape[0]):
        for j in range(shape[1]):
            world[i][j] = pnoise2(
                i / scale,
                j / scale,
                octaves=octaves,
                persistence=persistence,
                lacunarity=lacunarity,
                repeatx=1024,
                repeaty=1024,
                base=seed,
            )
    return world


# The following functions create different biomes/environments (all ending with _gen in definition name)

def island_gen(shape, world, color_world):
    """Generates ocean islands image with given user parameters"""
    # Fills 2d array color_world with given colors based on perlin noise algorithm output values
    for i in range(shape[0]):
        for j in range(shape[1]):
            if world[i][j] < 0:
                color_world[i][j] = cs.deep_blue
            elif world[i][j] < 0.05:
                color_world[i][j] = cs.blue
            elif world[i][j] < 0.075:
                color_world[i][j] = cs.shelf_blue
            elif world[i][j] < 0.1:
                rand_int = random.randint(0, 1)
                if rand_int == 0:
                    color_world[i][j] = cs.beach
                else:
                    color_world[i][j] = cs.beach2
            elif world[i][j] < 0.25:
                rand_int = random.randint(0, 2)
                if rand_int == 0:
                    color_world[i][j] = cs.green
                elif rand_int == 1:
                    color_world[i][j] = cs.dark_green
                else:
                    color_world[i][j] = cs.dark_green2
            elif world[i][j] < 0.275:
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
            elif world[i][j] < 0.42:
                rand_int = random.randint(0, 1)
                if rand_int == 0:
                    color_world[i][j] = cs.snow
                else:
                    color_world[i][j] = cs.snow2
            elif world[i][j] <= 1.0:
                color_world[i][j] = cs.snow


def forest_gen(shape, world, color_world):
    """Generates forest image with given user parameters"""
    # Fills 2d array color_world with given colors based on perlin noise algorithm output values
    for i in range(shape[0]):
        for j in range(shape[1]):
            if world[i][j] < -0.1:
                random_int = random.randint(0, 1)
                if random_int != 0:
                    color_world[i][j] = cs.super_green
                else:
                    color_world[i][j] = cs.forest_dark_green
            elif world[i][j] < -0.05:
                random_int = random.randint(0, 1)
                if random_int == 0:
                    color_world[i][j] = cs.forest_dark_green
                else:
                    color_world[i][j] = cs.forest_green
            elif world[i][j] < -0.025:
                random_int = random.randint(0, 1)
                if random_int == 0:
                    color_world[i][j] = cs.dirt
                else:
                    color_world[i][j] = cs.dark_brown
            elif world[i][j] < 0.025:
                random_int = random.randint(0, 1)
                if random_int == 0:
                    color_world[i][j] = cs.black
                else:
                    color_world[i][j] = cs.dark_brown
            elif world[i][j] < 0.05:
                random_int = random.randint(0, 1)
                if random_int == 0:
                    color_world[i][j] = cs.dirt
                else:
                    color_world[i][j] = cs.dark_brown
            elif world[i][j] < 0.1:
                random_int = random.randint(0, 1)
                if random_int == 0:
                    color_world[i][j] = cs.forest_dark_green
                else:
                    color_world[i][j] = cs.forest_green
            elif world[i][j] < 0.35:
                random_int = random.randint(0, 1)
                if random_int == 0:
                    color_world[i][j] = cs.super_green
                else:
                    color_world[i][j] = cs.forest_dark_green
            elif world[i][j] <= 1:
                color_world[i][j] = cs.super_green


def oasis_gen(shape, world, color_world):
    """Generates desert oasis image with given user parameters"""
    # Fills 2d array color_world with given colors based on perlin noise algorithm output values
    for i in range(shape[0]):
        for j in range(shape[1]):
            if world[i][j] < -0.3:
                color_world[i][j] = cs.sandstone
            elif world[i][j] < -0.15:
                rand_int = random.randint(0, 5)
                if rand_int == 0:
                    color_world[i][j] = cs.sand
                else:
                    color_world[i][j] = cs.sandstone
            elif world[i][j] < -0.1:
                rand_int = random.randint(0, 1)
                if rand_int == 0:
                    color_world[i][j] = cs.sandstone
                else:
                    color_world[i][j] = cs.sand
            elif world[i][j] < 0:
                rand_int = random.randint(0, 3)
                if rand_int == 0:
                    color_world[i][j] = cs.sandstone
                else:
                    color_world[i][j] = cs.sand
            elif world[i][j] < 0.1:
                color_world[i][j] = cs.sand
            elif world[i][j] < 0.14:
                rand_int = random.randint(0, 3)
                if rand_int == 0:
                    color_world[i][j] = cs.sandstone
                else:
                    color_world[i][j] = cs.sand
            elif world[i][j] < 0.16:
                color_world[i][j] = cs.sandstone
            elif world[i][j] < 0.2:
                rand_int = random.randint(0, 1)
                if rand_int == 0:
                    color_world[i][j] = cs.oasis_green
                else:
                    color_world[i][j] = cs.sandstone
            elif world[i][j] < 0.21:
                color_world[i][j] = cs.oasis_green
            elif world[i][j] <= 1.0:
                color_world[i][j] = cs.oasis_water


def blossom_gen(shape, world, color_world):
    """Generates cherry blossom forest image with given user parameters"""
    # Fills 2d array color_world with given colors based on perlin noise algorithm output values
    for i in range(shape[0]):
        for j in range(shape[1]):
            if world[i][j] < -0.2:
                random_int = random.randint(0, 1)
                if random_int == 0:
                    color_world[i][j] = cs.pink
                else:
                    color_world[i][j] = cs.light_pink
            elif world[i][j] < -.1:
                random_int = random.randint(0, 1)
                if random_int == 0:
                    color_world[i][j] = cs.light_pink
                else:
                    color_world[i][j] = cs.light_yellow
            elif world[i][j] < -.05:
                random_int = random.randint(0, 1)
                if random_int == 0:
                    color_world[i][j] = cs.light_yellow
                else:
                    color_world[i][j] = cs.blossom_green
            elif world[i][j] < 0:
                color_world[i][j] = cs.blossom_river
            elif world[i][j] < .05:
                random_int = random.randint(0, 1)
                if random_int == 0:
                    color_world[i][j] = cs.light_yellow
                else:
                    color_world[i][j] = cs.blossom_green
            elif world[i][j] < .15:
                random_int = random.randint(0, 1)
                if random_int == 0:
                    color_world[i][j] = cs.light_pink
                else:
                    color_world[i][j] = cs.light_yellow
            elif world[i][j] <= 1:
                random_int = random.randint(0, 1)
                if random_int == 0:
                    color_world[i][j] = cs.pink
                else:
                    color_world[i][j] = cs.light_pink


def cave_gen(shape, world, color_world):
    """Generates lava cave image with given user parameters"""
    # Fills 2d array color_world with given colors based on perlin noise algorithm output values
    for i in range(shape[0]):
        for j in range(shape[1]):
            if world[i][j] < -0.05:
                color_world[i][j] = cs.black
            elif world[i][j] < .2:
                color_world[i][j] = cs.cave_gray
            elif world[i][j] <= 1:
                random_int = random.randint(0, 1)
                if random_int == 0:
                    color_world[i][j] = cs.lava_red
                else:
                    color_world[i][j] = cs.lava_orange


def terrace_gen(shape, world, color_world):
    """Generates rice terrace image with given user parameters"""
    # Fills 2d array color_world with given colors based on perlin noise algorithm output values
    for i in range(shape[0]):
        for j in range(shape[1]):
            if world[i][j] < -.30:
                random_int = random.randint(0, 2)
                if random_int == 0:
                    color_world[i][j] = cs.spring
                else:
                    color_world[i][j] = cs.terr_dark_green
            elif world[i][j] < -.28:
                random_int = random.randint(0, 1)
                if random_int == 0:
                    color_world[i][j] = cs.terr_dirt
                else:
                    color_world[i][j] = cs.tan
            elif world[i][j] < -.22:
                random_int = random.randint(0, 2)
                if random_int == 0:
                    color_world[i][j] = cs.spring
                else:
                    color_world[i][j] = cs.terr_green
            elif world[i][j] < -.2:
                random_int = random.randint(0, 1)
                if random_int == 0:
                    color_world[i][j] = cs.terr_dirt
                else:
                    color_world[i][j] = cs.tan
            elif world[i][j] < -.14:
                random_int = random.randint(0, 2)
                if random_int == 0:
                    color_world[i][j] = cs.spring
                else:
                    color_world[i][j] = cs.light_green
            elif world[i][j] < -.12:
                random_int = random.randint(0, 1)
                if random_int == 0:
                    color_world[i][j] = cs.terr_dirt
                else:
                    color_world[i][j] = cs.tan
            elif world[i][j] < -.07:
                color_world[i][j] = cs.river
            elif world[i][j] < -.05:
                random_int = random.randint(0, 1)
                if random_int == 0:
                    color_world[i][j] = cs.terr_dirt
                else:
                    color_world[i][j] = cs.tan
            elif world[i][j] < .01:
                random_int = random.randint(0, 2)
                if random_int == 0:
                    color_world[i][j] = cs.spring
                else:
                    color_world[i][j] = cs.light_green
            elif world[i][j] < .03:
                random_int = random.randint(0, 1)
                if random_int == 0:
                    color_world[i][j] = cs.terr_dirt
                else:
                    color_world[i][j] = cs.tan
            elif world[i][j] < .09:
                random_int = random.randint(0, 2)
                if random_int == 0:
                    color_world[i][j] = cs.spring
                else:
                    color_world[i][j] = cs.terr_green
            elif world[i][j] < .11:
                random_int = random.randint(0, 1)
                if random_int == 0:
                    color_world[i][j] = cs.terr_dirt
                else:
                    color_world[i][j] = cs.tan
            elif world[i][j] < .17:
                random_int = random.randint(0, 2)
                if random_int == 0:
                    color_world[i][j] = cs.spring
                else:
                    color_world[i][j] = cs.terr_dark_green
            elif world[i][j] < .19:
                random_int = random.randint(0, 1)
                if random_int == 0:
                    color_world[i][j] = cs.terr_dirt
                else:
                    color_world[i][j] = cs.tan
            elif world[i][j] < .25:
                random_int = random.randint(0, 2)
                if random_int == 0:
                    color_world[i][j] = cs.spring
                else:
                    color_world[i][j] = cs.darkest_green
            elif world[i][j] < .27:
                random_int = random.randint(0, 1)
                if random_int == 0:
                    color_world[i][j] = cs.terr_dirt
                else:
                    color_world[i][j] = cs.tan
            elif world[i][j] < .33:
                random_int = random.randint(0, 2)
                if random_int == 0:
                    color_world[i][j] = cs.spring
                else:
                    color_world[i][j] = cs.terr_dark_green
            elif world[i][j] < .35:
                random_int = random.randint(0, 1)
                if random_int == 0:
                    color_world[i][j] = cs.terr_dirt
                else:
                    color_world[i][j] = cs.tan
            elif world[i][j] <= 1:
                random_int = random.randint(0, 2)
                if random_int == 0:
                    color_world[i][j] = cs.spring
                else:
                    color_world[i][j] = cs.green


def cloud_gen(shape, world, color_world):
    """Generates cloud image with given user parameters"""
    # Fills 2d array color_world with given colors based on perlin noise algorithm output values
    for i in range(shape[0]):
        for j in range(shape[1]):
            if world[i][j] < -0.205:
                color_world[i][j] = cs.cloud
            elif world[i][j] < -0.19:
                color_world[i][j] = cs.cloud_2
            elif world[i][j] < -0.175:
                color_world[i][j] = cs.cloud_3
            elif world[i][j] < -0.16:
                color_world[i][j] = cs.cloud_4
            elif world[i][j] < -0.15:
                color_world[i][j] = cs.cloud_5
            elif world[i][j] < 0.15:
                random_int = random.randint(0, 1)
                if random_int == 0:
                    color_world[i][j] = cs.sky
                else:
                    color_world[i][j] = cs.sky_2
            elif world[i][j] < 0.16:
                color_world[i][j] = cs.cloud_5
            elif world[i][j] < 0.175:
                color_world[i][j] = cs.cloud_4
            elif world[i][j] < 0.19:
                color_world[i][j] = cs.cloud_3
            elif world[i][j] < 0.205:
                color_world[i][j] = cs.cloud_2
            elif world[i][j] <= 1.0:
                color_world[i][j] = cs.cloud


def rainbow_gen(shape, world, color_world):
    """Generates rainbow land image with given user parameters"""
    # Fills 2d array color_world with given colors based on perlin noise algorithm output values
    for i in range(shape[0]):
        for j in range(shape[1]):
            if world[i][j] < -.3:
                color_world[i][j] = cs.rbviolet
            elif world[i][j] < -.15:
                color_world[i][j] = cs.rbindigo
            elif world[i][j] < -.05:
                color_world[i][j] = cs.rbblue
            elif world[i][j] < .05:
                color_world[i][j] = cs.rbgreen
            elif world[i][j] < .15:
                color_world[i][j] = cs.rbyellow
            elif world[i][j] < .3:
                color_world[i][j] = cs.rborange
            elif world[i][j] < 1.0:
                color_world[i][j] = cs.rbred


def graylands_gen(shape, world, color_world):
    """Generates graylands image with given user parameters"""
    for i in range(shape[0]):
        for j in range(shape[1]):
            if world[i][j] < -.15:
                color_world[i][j] = cs.black
            elif world[i][j] < 0:
                color_world[i][j] = cs.gldark_gray
            elif world[i][j] < .15:
                color_world[i][j] = cs.glgray
            elif world[i][j] < .3:
                color_world[i][j] = cs.gllight_gray
            elif world[i][j] < 1.0:
                color_world[i][j] = cs.white


def topographic_map_gen(shape, world, color_world):
    """Generates topographic map image with given user parameters"""
    for i in range(shape[0]):
        for j in range(shape[1]):
            if world[i][j] < -.3:
                color_world[i][j] = cs.white
            elif world[i][j] < -.29:
                color_world[i][j] = cs.black
            elif world[i][j] < -.2:
                color_world[i][j] = cs.white
            elif world[i][j] < -.19:
                color_world[i][j] = cs.black
            elif world[i][j] < -.1:
                color_world[i][j] = cs.white
            elif world[i][j] < -.09:
                color_world[i][j] = cs.black
            elif world[i][j] < 0:
                color_world[i][j] = cs.white
            elif world[i][j] < .01:
                color_world[i][j] = cs.black
            elif world[i][j] < .1:
                color_world[i][j] = cs.white
            elif world[i][j] < .11:
                color_world[i][j] = cs.black
            elif world[i][j] < .2:
                color_world[i][j] = cs.white
            elif world[i][j] < .21:
                color_world[i][j] = cs.black
            elif world[i][j] < .3:
                color_world[i][j] = cs.white
            elif world[i][j] < 1.0:
                color_world[i][j] = cs.white


def create_img(color_world):
    """Converts image data and writes to png file in the directory"""
    # converts float6 to uint8 to prevent lossy conversion
    color_world_uint8 = np.uint8(color_world)
    imwrite("map_gen_img.png", color_world_uint8)
    # imwrite("map_gen_img.png", color_world)


def open_img():
    """Open and display image on screen"""
    background = Image.open("map_gen_img.png")
    background.show()


def set_biome(given_biome, shape, world, color_world):
    """Sets biome/terrain/colors for generation based on user input"""
    # Caller dispatch: A dictionary key calls its value, an encapsulated function
    biomes_dict = {
        "Islands": island_gen,
        "Forest": forest_gen,
        "Desert Oasis": oasis_gen,
        "Cherry Blossom": blossom_gen,
        "Caves": cave_gen,
        "Terraces": terrace_gen,
        "Clouds": cloud_gen,
        "Rainbow": rainbow_gen,
        "Graylands": graylands_gen,
        "Topographic Map": topographic_map_gen}
    return biomes_dict[given_biome](shape, world, color_world)


def set_scale(given_scale):
    """Sets scale for generation based on user input"""
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
        "1000": 1000}
    return scale_dict.get(given_scale)


def set_shape(given_shape):
    """Sets shape of image based on user input"""
    shape_dict = {
        "400x400": (400, 400),
        "600x600": (600, 600),
        "800x800": (800, 800)}
    return shape_dict.get(given_shape)


def set_octaves(given_octaves):
    """Sets octaves of generation based on user input"""
    # Map user given octaves parameter to int values
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
        "10": 10}
    return octaves_dict.get(given_octaves)


def generate_map(given_biome, given_scale, given_shape, given_octaves):
    """Creates base map from given parameters, colors in with biome specs, creates final image"""
    scale = set_scale(given_scale)
    shape = set_shape(given_shape)
    octaves = set_octaves(given_octaves)
    world = np.zeros(shape)
    generate_base_map(shape, scale, octaves, world)
    color_world = np.zeros(world.shape + (3,))

    # Test function: prints given biome in console for test purposes
    print(given_biome)

    set_biome(given_biome, shape, world, color_world)
    create_img(color_world)
    open_img()
