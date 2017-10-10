
# pseudo code
# N = len(A)
# if N == 0
# return
# find midpoint
# if i < midpoint : no MI in the lower half: call magic_index(upper_half)
# if i == midpoint : MI
# if i > midpoint: no MI in upper half call magic_index(lower_half)def helper(lst, midpoint):

def magic_index(A_list, add_to_index = 0):
    """ Magic Index (MI)- see if i exists so as: i == A[i] """

    if len(A_list) == 0:
        return None

    midpoint = len(A_list ) //2

    if add_to_index + midpoint == A[midpoint]:
        return A[midpoint]
    elif midpoint < A_list[midpoint]:
        return magic_index(A_list[:midpoint], add_to_index)
    else:
        add_to_index += midpoint
        return magic_index(A_list[midpoint:], add_to_index)

if __name__ == "__main__":
    A = [-10, -4, 0, 2, 3, 5, 7, 9]
    print("See if i exists so as: i == list[i] \nMagic Index for A[-10,-4,0,2,3,5,7,9] :: ", magic_index(A))