

# More than 2 lines will result in 0 score. Do not leave a blank line also
for i in range(1, int(input())+1):
    print((pow(10, i)//9)**2)


"""
    one liner code with math concept

    1^2 = 1
    11^2 = 121
    111^2 = 12321
    1111^2 = 1234321
    11111^2 = 123454321

    pow(10, i) ->  10^i
    pow(10, i)//9 -> 10^i/9 - 11 is the first digit of the number
    pow(10, i)//9**2 -> 10^i/9^2 - the multiplication i.e final anser
"""
