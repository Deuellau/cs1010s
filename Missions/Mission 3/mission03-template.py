# CS1010S --- Programming Methodology
# Mission 3
#

from m3_graphics import *

###########
# Task 1a #
###########


def flip_vertical(image):
    w = get_width(image)
    h = get_height(image)
    res = ()
    
    for row_idx in range(h-1, -1, -1):
        row = ()
        
        for col_idx in range(0, w):
            row += (get_pixel(image, row_idx, col_idx),)

        res += (row,)

    return res


# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 1A
# print("## Task 1A ##")
# felix_vert = flip_vertical(felix)
# print(felix_vert == TESTCASE1A)

# UNCOMMENT THE CODE BELOW TO DISPLAY felix
# display(felix)

# UNCOMMENT THE CODE BELOW TO DISPLAY felix_vert
# display(felix_vert)

###########
# Task 1b #
###########


def flip_horizontal(image):
    w = get_width(image)
    h = get_height(image)
    res = ()
    
    for row_idx in range(0, h):
        row = ()
        
        for col_idx in range(w-1, -1, -1):
            row += (get_pixel(image, row_idx, col_idx),)

        res += (row,)

    return res


# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 1B
# print("## Task 1B ##")
# luna_horiz = flip_horizontal(luna)
# print(luna_horiz == TESTCASE1B)

# UNCOMMENT THE CODE BELOW TO DISPLAY luna
# display(luna)

# UNCOMMENT THE CODE BELOW TO DISPLAY luna_horiz
# display(luna_horiz)

###########
# Task 1c #
###########


def rotate_clockwise(image):
    w = get_width(image)
    h = get_height(image)
    res = ()

    for col_idx in range(0, w):
        col = ()
        
        for row_idx in range(h-1, -1, -1):
            col += (get_pixel(image, row_idx, col_idx),)

        res += (col,)

    return res


# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 1C
# print("## Task 1C ##")
# heart_cw = rotate_clockwise(heart_bb)
# print(heart_cw == TESTCASE1C)

# UNCOMMENT THE CODE BELOW TO DISPLAY heart_bb
# display(heart_bb)

# UNCOMMENT THE CODE BELOW TO DISPLAY heart_cw
# display(heart_cw)

###########
# Task 2a #
###########


# helper
def pixel_inversion(pixel, img_type):
    if img_type == 'Binary':
        if pixel:
            return False
        else:
            return True
        
    elif img_type == 'Gray':
        return abs(pixel - 255)
    
    else:
        ret = ()
        for single in pixel:
            ret += (abs(single - 255),)
        return ret


def invert(image):
    w = get_width(image)
    h = get_height(image)
    res = ()

    for row_idx in range(0, h):
        row = ()
        
        for col_idx in range(0, w):
            img_type = get_image_type(image)
            
            old_pixel = get_pixel(image, row_idx, col_idx)
            new_pixel = pixel_inversion(old_pixel, img_type)
            row += (new_pixel,)

        res += (row, )

    return res


# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 2A
# print("## Task 2A ##")
# rgb_invert = invert(rgb_img)
# print(rgb_invert == TESTCASE2A)

# UNCOMMENT THE CODE BELOW TO DISPLAY rgb_img)
# display(rgb_img)

# UNCOMMENT THE CODE BELOW TO DISPLAY rgb_invert
# display(rgb_invert)

###########
# Task 2b #
###########


# helper
def relative_lum(rgb):
    return int(0.21 * rgb[0] + 0.72 * rgb[1] + 0.07* rgb[2])


def rgb_to_grayscale(rgb_image):
    w = get_width(rgb_image)
    h = get_height(rgb_image)
    res = ()
        
    for row_idx in range(0, h):
        row = ()
        
        for col_idx in range(0, w):
            old_pixel = get_pixel(rgb_image, row_idx, col_idx)
            new_pixel = relative_lum(old_pixel)
            row += (new_pixel,)

        res += (row, )

    return res


# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 2B
# print("## Task 2B ##")
# rgb_gray = rgb_to_grayscale(rgb_img)
# print(rgb_gray == TESTCASE2B)

# UNCOMMENT THE CODE BELOW TO DISPLAY rgb_img
# display(rgb_img)

# UNCOMMENT THE CODE BELOW TO DISPLAY rgb_gray
# display(rgb_gray)


###########
# Task 3a #
###########


# helper
def rgb_grayscale(pixel, threshold_val, img_type):
    if img_type == 'RGB':
        gray_val = int(0.21 * pixel[0] + 0.72 * pixel[1] + 0.07* pixel[2])
    elif img_type == 'Binary':
        gray_val = pixel * 255
    else:
        gray_val = pixel

    if gray_val >= threshold_val:
        return True
    else:
        return False



def threshold(img, val):
    w = get_width(img)
    h = get_height(img)
    res = ()
        
    for row_idx in range(0, h):
        row = ()
        
        for col_idx in range(0, w):
            img_type = get_image_type(img)
            old_pixel = get_pixel(img, row_idx, col_idx)
            
            new_pixel = rgb_grayscale(old_pixel, val, img_type)
            row += (new_pixel,)

        res += (row, )

    return res


# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 3A
# print("## Task 3A ##")
# luna_bw = threshold(luna, 85)
# print(luna_bw == TESTCASE3A)

# UNCOMMENT THE CODE BELOW TO DISPLAY luna
# display(luna)

# UNCOMMENT THE CODE BELOW TO DISPLAY luna_bw
# display(luna_bw)


###########
# Task 3b #
###########


def green_screen(foreground, background, pixel):
    w = get_width(background)
    h = get_height(background)
    res = ()
        
    for row_idx in range(0, h):
        row = ()
        
        for col_idx in range(0, w):
            testing_pixel = get_pixel(foreground, row_idx, col_idx)
            
            if testing_pixel == pixel:
                new_pixel = get_pixel(background, row_idx, col_idx)
            else:
                new_pixel = testing_pixel
                
            row += (new_pixel,)

        res += (row, )

    return res


# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 3B
# print("## Task 3B ##")
# holiday_cats = green_screen(luna_felix, background, GREENSCREEN_COLOR)
# print(holiday_cats == TESTCASE3B)

# UNCOMMENT THE CODE BELOW TO DISPLAY foreground and background
# display(luna_felix)
# display(background)

# UNCOMMENT THE CODE BELOW TO DISPLAY holday_cats
# display(holiday_cats)


######################################### EXTRA (OPTIONAL) #########################################


def save_all():
    # Modify as you like
    save_image(felix, "felix.png")
    save_image(luna, "luna.png")
    save_image(heart_bb, "heart_bb.png")
    save_image(rgb_img, "rgb.png")

    save_image(felix_vert, "felix_vert.png")
    save_image(luna_horiz, "luna_horiz.png")
    save_image(heart_cw, "heart_rot.png")

    save_image(rgb_invert, "rgb_invert.png")
    save_image(rgb_gray, "rgb_gray.png")

    save_image(luna_bw, "luna_bw.png")
    save_image(luna_felix, "luna_felix.png")
    save_image(background, "background.png")
    save_image(holiday_cats, "holiday_cats.png")


# UNCOMMENT TO SAVE ALL IMAGES IN THE CURRENT FOLDER
# save_all()


def decode_your_1010s_grade():
    # How will you see through the noise?
    display(grade)
    # Your code here


# Have fun!
# decode_your_1010s_grade()
