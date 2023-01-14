import extcolors
import webcolors
import ColorTranslator

class ImageProcessor(object):

    def __init__(self):
        print("Process Image Color Initialized")
        self.colors = []
        self.selectedColor = Color((0,0,0),0)

    def processColor(self):
        input_name = '/Users/mariaagustinamarkosich/Documents/Facultad/Robots/TP3/yolov5/runs/detect/exp/crops/cartera/prediction_image_2.jpg'
        colors_x = extcolors.extract_from_path(input_name, tolerance=10, limit=10)
        #Example result colors_x:
        #Total result:
        # ([((156, 61, 57), 115587),
        # ((214, 71, 73), 25691),
        # ((240, 216, 192), 9119),
        # ((188, 147, 119), 8694),
        # ((28, 28, 38), 8606),
        # ((132, 139, 167), 6265),
        # ((10, 5, 2), 6260),
        # ((56, 21, 19), 6141),
        # ((126, 35, 32), 6021),
        # ((224, 224, 224), 5260)],
        # 247040)
        self.selectedColor = Color(colors_x[0][0][0],colors_x[0][0][1])

        print(" ")
        print("Selected color: ")
        self.selectedColor.print()
        print(" ")

        for color in colors_x[0]:
            parsedColor = Color(color[0],color[1])
            self.colors.append(parsedColor)

class Color(object):

    def __init__(self, rgb, count):
        self.count = count
        self.rgb = rgb
        self.name = self.get_colour_name(rgb)
        self.translation = ColorTranslator.ColorTranslator().translate(self.name)
        self.r = rgb[0]
        self.g = rgb[1]
        self.b = rgb[2]

    def closest_colour(self, requested_colour):
        min_colours = {}
        for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
            r_c, g_c, b_c = webcolors.hex_to_rgb(key)
            rd = (r_c - requested_colour[0]) ** 2
            gd = (g_c - requested_colour[1]) ** 2
            bd = (b_c - requested_colour[2]) ** 2
            min_colours[(rd + gd + bd)] = name
        return min_colours[min(min_colours.keys())]

    def get_colour_name(self, requested_colour):
        try:
            closest_name = webcolors.rgb_to_name(requested_colour)
        except ValueError:
            closest_name = self.closest_colour(requested_colour)
        return closest_name

    def print(self):
        print("Color name: " + self.name + " Color Translation: " + self.translation + " Color rgb: " + str(self.rgb))


