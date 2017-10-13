from random import randint


def rand7():
    """ returns a random value between 1 and 7"""
    dict_rand_7 = {(1,1):1,(1,2):1,(1,3):1,
                   (1,4):2,(1,5):2,(2,1):2,
                   (2,2):3,(2,3):3,(2,4):3,
                   (2,5):4,(3,1):4,(3,2):4,
                   (3,3):5,(3,4):5,(3,5):5,
                   (4,1):6,(4,2):6,(4,3):6,
                   (4,4):7,(4,5):7,(5,1):7,
                   (5, 2):0,(5,3):0,(5,4):0,(5,5):0}


    rand7_val = 0

    while rand7_val == 0:
        rand7_val = dict_rand_7[(randint(1,5), randint(1,5))]

    return rand7_val

def roll_rand7(n):

    rolls = {}

    for i in range(n):
        num = rand7()
        if num in rolls:
            rolls[num] += 1
        else:
            rolls[num] = 1
    return rolls

if __name__ == "__main__":

    print(roll_rand7(10000))

