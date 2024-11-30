#
# CS1010S --- Programming Methodology
#
# Mission 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *


##########
# Task 1 #
##########

def mosaic(i1, i2, i3, i4):
    p1 = stack(i4, i3)
    p2 = stack(i1, i2)
    return beside(p1, p2)

# Test
# show(mosaic(rcross_bb, sail_bb, corner_bb, nova_bb))
# show(mosaic(heart_bb, pentagram_bb, circle_bb, ribbon_bb))


##########
# Task 2 #
##########

def simple_fractal(i1):
    return beside(i1, stack(i1, i1))

# Test
# show(simple_fractal(make_cross(rcross_bb)))
# show(simple_fractal(heart_bb))


##########
# Task 3 #
##########

def egyptian(pic, n):
    p1 = stack(quarter_turn_left(pic), quarter_turn_left(pic))
    if n != 3:
        p2 = stack(pic, pic)
    else:
        p2 = pic


    row = quarter_turn_right(stackn(n, quarter_turn_left(pic)))
    col = quarter_turn_right(stackn(n-2, pic))
    
    mid = stack_frac(1/(n-1), col, quarter_turn_right(pic))
    mid = stack_frac((n-1)/n, mid, col)
    mid = quarter_turn_left(mid)

    out = stack_frac(1/(n-1), row, mid)
    out = stack_frac((n-1)/n, out, row)
    
    return out

# Test
# show(egyptian(make_cross(rcross_bb), 5))
# show(egyptian(make_cross(rcross_bb), 9))
# show(egyptian(nova_bb, 4))
