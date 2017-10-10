"""
Program to simulate paint fill feature.
Changes the old color of a given point and surrounding old color points to new color.
"""

def is_pixel_in_matrix(matrix, point):
    if 0 <= point[0] < len(matrix) and 0 <= point[1] < len(matrix[0]):
        return True
    else:
        return False


def surrounding_pixels_of_old_color(matrix, pixel, old_color, new_color):
    """ checks if 8 points around pixel is in matrix and if they have old_color, change to new_color and add them to
        surrounding_pix list. Return list. """
    r, c = pixel
    surrounding_pix = []
    for i in range(r-1,r+2):
        for j in range(c-1,c+2):
            if is_pixel_in_matrix(matrix, (i,j)) and matrix[i][j] == old_color:
                if i == r and j == c:
                    matrix[i][j] = new_color
                else:
                    matrix[i][j] = new_color
                    surrounding_pix.append((i,j))
    return surrounding_pix


def fill(matrix, pixel, new_color):
    """ Mimics the Fill feqature of Paint"""
    rows = len(matrix)
    cols = len(matrix[0])
    old_color = matrix[pixel[0]][pixel[1]]

    if rows == 0 or cols == 0:
        return matrix

    # find nearby pixels that has old color, add them to a list.
    nearby_pix = surrounding_pixels_of_old_color(matrix, pixel, old_color, new_color)

    while nearby_pix != []:
        nearby_pix.extend(surrounding_pixels_of_old_color(matrix,nearby_pix.pop(),old_color, new_color))



if __name__ == "__main__":

    matrix = [["b","b","b","b","b","b","b"],
              ["b","b","b","b","b","b","b"],
              ["b","b","w","w","w","w","w"],
              ["w","w","w","w","w","w","w"],
              ["g","g","g","g","g","g","g"],
              ["g","g","g","g","g","g","g"]]
    print ("Fill method in Paint: change all 'g' adjacent to (4,5) to 'r', in matrix ")
    print (matrix)
    print (fill(matrix, (4,5), "r"))
    print(matrix)