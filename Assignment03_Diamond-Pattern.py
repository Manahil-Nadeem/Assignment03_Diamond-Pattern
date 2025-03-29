def draw_diamond(height):
    #For upper part of the diamond (pyramid)
    for i in range(height):
        stars = '*' * (2 * i + 1)
        spaces = ' ' * (height - i - 1)
        print(spaces + stars)
    
    # For lower part of the diamond (inverted pyramid)
    for i in range(height - 2, -1, -1):
        stars = '*' * (2 * i + 1)
        spaces = ' ' * (height - i - 1)
        print(spaces + stars)

# Calling the function with height 5
draw_diamond(5)


#The output is;
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
