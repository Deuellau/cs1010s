#
# CS1010S --- Programming Methodology
#
# Mission 2
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *

###########
# Task 1a #
###########

def dual_fractal(img1, img2, n):
    if n == 1:
        return img1
        
    return stack(img1, beside(dual_fractal(img2, img1, n-1),dual_fractal(img2, img1, n-1)))

# Test
# show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 3))
# show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 4))
# show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 7))
# Write your additional test cases here

###########
# Task 1b #
###########

def dual_fractal_iter(img1, img2, n):
    if n % 2 == 0:
        combined = img2
    else:
        combined = img1
        
    for i in range(n-1, 0, -1):
        if i % 2 == 0:
            combined = stack(img2, beside(combined, combined))
        else:
            combined = stack(img1, beside(combined, combined))
    
    return combined

# Test
# show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 3))
# show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 4))
# show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 7))

###########
# Task 2a #
###########

def reverse(num):
    def length(num):
        count = 0
        while num//10 > 0:
            count += 1
            num //= 10
        return count+1
    
    num_length = length(num)
    result = 0
    for i in range(num_length-1, -1, -1):
        result += (num%10)*10**i
        num //= 10
        
    return result


def is_palindrome_using_reverse(num):
    return num == reverse(num)


# Uncomment to test
# print(reverse(12321) == 12321)
# print(reverse(110) == 11)
# print(reverse(0) == 0)

# Uncomment to test
# print(is_palindrome_using_reverse(12321) == True)
# print(is_palindrome_using_reverse(110) == False)
# print(is_palindrome_using_reverse(0) == True)

###########
# Task 2b #
###########

def is_palindrome_using_symmetry(string):
    
    def length(s):
        count = 0
        for char in string:
            count += 1
        return count
    
    s_length = length(string)

    for i in range(0, s_length//2, 1):
        if string[i] != string[s_length-1-i]:
            return False
    
    return True


# Uncomment to test
# print(is_palindrome_using_symmetry("today is a really long day") == False)
# print(is_palindrome_using_symmetry("saippuakivikauppias") == True)
# print(is_palindrome_using_symmetry("2002") == True)
# print(is_palindrome_using_symmetry("A man, a plan, a canal: Panama") == False)
# print(is_palindrome_using_symmetry("amanaplanacanalpanama") == True)

##########
# Task 3 #
##########

def num_of_steps(x, y, W, H):
    if x == 0 and y == 0:
        return 0
    
    cx, cy = 0, 0
    Wmin, Hmin, Wmax, Hmax = 0, 0, W-1, H-1
    d = 1
    
    count = 0
    travel_lr = 0
    
    while (True):

        for i in range(Wmin, Wmax, 1):
            cx += 1*d
            count += 1
            if (cx==x) and (cy==y):
                return count
            
        if travel_lr == 0:
            travel_lr += 1
        else:
            Wmax -= 1

        for i in range(Hmin, Hmax, 1):
            cy += 1*d
            count += 1
            if (cx==x) and (cy==y):
                return count
        Hmax -= 1

        d *= -1

# Uncomment to test
# print(num_of_steps(1, 1, 3, 3) == 8)
# print(num_of_steps(0, 0, 3, 3) == 0)
# print(num_of_steps(1, 3, 5, 7) == 30)
# print(num_of_steps(1, 1, 3, 2) == 4)
