# CS1010S --- Programming Methodology
# Mission 3
#

from m3_graphics import *

###########
# Task 1a #
###########


def flip_vertical(image):
    # Your code here
    pass


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
    # Your code here
    pass


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
    # Your code here
    pass


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


def invert(image):
    # Your code here
    pass


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


def rgb_to_grayscale(rgb_image):
    # Your code here
    pass


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


def threshold(img, val):
    # Your code here
    pass


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
    # Your code here
    pass


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
