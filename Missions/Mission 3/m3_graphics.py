########################################## DON'T CHANGE ###########################################
from tkinter import *
from m3_testcase import *
from random import randint, getrandbits
from PIL import Image


######################################## Drawing to screen ########################################
master = Tk()
master.resizable(width=FALSE, height=FALSE)
viewport_size = 600
canvas = Canvas(master, width=viewport_size, height=viewport_size)
canvas.pack()


class Rgb:
    def __init__(self, r, g, b):
        assert self.check_valid_rgb(r, g, b)
        self.r = min(round(r), 255)
        self.g = min(round(g), 255)
        self.b = min(round(b), 255)

    def hexcode(self):
        return "#%02x%02x%02x" % (self.r, self.g, self.b)

    def check_valid_rgb(self, r, g, b):
        if any(not isinstance(i, int) for i in [r, g, b]):
            raise TypeError("RGB values must be integers")
        if all(0 <= i <= 255 for i in [r, g, b]):
            return True
        else:
            raise ValueError("Invalid RGB value")


def get_color(pixel, image_type: str):
    if image_type == "RGB":
        return Rgb(*pixel).hexcode()
    elif image_type == "Gray":
        return Rgb(pixel, pixel, pixel).hexcode()
    else:
        return "white" if pixel else "black"


def clear_all():
    canvas.create_rectangle(
        0, 0, viewport_size, viewport_size, fill="white"
    )  # Clear the canvas


def draw(x: int, y: int, color: str, pixel_size: int):
    x0, y0 = x * pixel_size, y * pixel_size
    x1, y1 = x0 + pixel_size, y0 + pixel_size
    canvas.create_rectangle(x0, y0, x1, y1, outline=color, fill=color)


######################################## CheckRepresenation ########################################
def check_representation(image_data: tuple[tuple]):
    """Checks if an image is represented as a tuple of tuples with the same width every row"""
    if not all(len(row) == len(image_data[0]) for row in image_data):
        raise ValueError(
            "Invalid image representation. All rows must have the same length as the width."
        )
    return True


####################################### Image ADT operations #######################################
def display(image_data: list[list]):
    # Clear Tkinter window and canvas
    clear_all()
    assert check_representation(image_data) == True
    # Calculate the size of each "pixel" in the display
    width, height = len(image_data[0]), len(image_data)
    pixel_size = min(viewport_size / width, viewport_size / height)
    canvas.config(width=width * pixel_size, height=height * pixel_size)
    canvas.pack()

    # Get image type
    image_type = get_image_type(image_data)

    # Draw each pixel
    for y, row in enumerate(image_data):
        for x, pixel in enumerate(row):
            color = get_color(pixel, image_type)
            draw(x, y, color, pixel_size)


def get_image_type(img) -> str:
    pixel = get_pixel(img, 0, 0)  # Get first pixel
    # Order matters, bool is an int.
    if isinstance(pixel, bool):
        return "Binary"
    elif isinstance(pixel, int):
        return "Gray"
    else:
        return "RGB"


################################# Additional Image ADT operations #################################
def transpose_image(image):
    return tuple(zip(*image))


def save_image(img, file_path):
    """Save Image ADT to file"""
    match get_image_type(img):
        case "Gray":
            image_type = "L"
        case "RGB":
            image_type = "RGB"
        case "Binary":
            image_type = "1"
    pil_img = Image.new(image_type, (get_width(img), get_height(img)))
    pil_img.putdata([pix for row in img for pix in row])
    pil_img.save(file_path)


def make_from_file(file_path):
    """Creates a RGB image from a file."""
    img = Image.open(file_path).convert("RGB")
    h = img.width
    w = img.height
    return tuple(tuple(img.getdata())[_ * h : _ * h + h] for _ in range(w))


###################################### Random Image Generator ######################################
def NOISE_IMG(height, width, rand_pix: callable):
    return tuple(tuple(rand_pix() for _ in range(width)) for _ in range(height))


def RGB_NOISE(height, width):
    return NOISE_IMG(
        height, width, lambda: (randint(0, 255), randint(0, 255), randint(0, 255))
    )


def GRAY_NOISE(height, width):
    return NOISE_IMG(height, width, lambda: randint(0, 255))


def BINARY_NOISE(height, width):
    return NOISE_IMG(height, width, lambda: bool(getrandbits(1)))


get_pixel = lambda a, b, c: a[b][c]
get_height = lambda a: len(a)
get_width = lambda a: len(a[0])


########################################### Coded Images ###########################################
def DIAMOND_BB():
    size = 100
    diamond = [[True] * size for _ in range(size)]

    for i in range(size):
        for j in range(size):
            if i < size // 2:
                within_upper_lobe = j in range(size // 2 - i, size // 2 + i)
                diamond[i][j] = not within_upper_lobe
            else:
                within_lower_triangle = j in range(i - size // 2, size + size // 2 - i)
                diamond[i][j] = not within_lower_triangle

    diamond[3][49] = True
    diamond[3][50] = True

    diamond[4][48] = True
    diamond[4][49] = True
    diamond[4][50] = True
    diamond[4][51] = True

    diamond[5][48] = True
    diamond[5][49] = True
    diamond[5][50] = True
    diamond[5][51] = True

    diamond[6][49] = True
    diamond[6][50] = True
    return tuple(map(tuple, diamond))


########################################## Sample Images ##########################################
checkerboard = ((False, True), (True, False))
diamond_bb = DIAMOND_BB()
rgb_noise = RGB_NOISE(16, 16)
gray_noise = GRAY_NOISE(16, 16)
binary_noise = BINARY_NOISE(16, 16)
