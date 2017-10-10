# three stacks a, b, c
# 1..N numbers on a move them to c
# can only move 1 at a time from the top, can't stack a bigger one on top of a smaller one

def hanoi(N, from_lst, to_stack, other_stack):

    if N == 0:
        return

    hanoi(N-1, from_lst, other_stack, to_stack)
    to_stack.append(from_lst.pop())
    hanoi(N-1, other_stack, to_stack, from_lst)

if __name__ == "__main__":
    a = [5,4,3,2,1]
    b = []
    c = []
    hanoi(5, a, c, b)
    print(a)
    print(b)
    print(c)
    a1 = [7]
    b1 = []
    c1 = []
    hanoi(1, a1, c1, b1)
    print(a1)
    print(b1)
    print(c1)
