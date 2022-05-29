

"""
    input T (1-100) test cases

    n = number of cards (1-1000)
    str(r) = 777
    str(b) = 111


   r (6)   (9)   (2) 

   b (7)   (1)   (5)

      3     2    1

"""

# 3! = 3*2*1 = 6


def red_blue_shuffle(n: int, r: str, b: str) -> str:

    r_list = list(r)
    b_list = list(b)

    

if __name__ == "__main__":

    T = int(input())

    for _ in range(T):
        n = int(input())
        r = input()
        b = input()
        print(red_blue_shuffle(n, r, b))

