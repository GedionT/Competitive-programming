import math


class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        c = Complex(None, None)
        c.real = self.real+no.real
        c.imaginary = self.imaginary+no.imaginary
        return c

    def __sub__(self, no):
        c = Complex(None, None)
        c.real = self.real-no.real
        c.imaginary = self.imaginary-no.imaginary
        return c

    def __mul__(self, no):
        c = Complex(None, None)
        c.real = self.real*no.real-no.imaginary*self.imaginary
        c.imaginary = self.imaginary*no.real+self.real*no.imaginary
        return c

    def __truediv__(self, no):
        c = Complex(None, None)
        c.real = (self.real*no.real+self.imaginary*no.imaginary) / \
            (no.imaginary**2+no.real**2)
        c.imaginary = (self.imaginary*no.real-self.real *
                       no.imaginary)/(no.imaginary**2+no.real**2)
        return c

    def mod(self):
        c = Complex(None, None)

        c.real = (self.real**2+self.imaginary**2)**(1/2)
        c.imaginary = 0
        return c


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')


"""

The real and imaginary precision part should be correct up to two decimal places.

Input Format

One line of input: The real and imaginary part of a number separated by a space.

Output Format

For two complex numbers  and , the output should be in the following sequence on separate lines:


For complex numbers with non-zero real and complex part, the output should be in the following format:

Replace the plus symbol  with a minus symbol  when .

For complex numbers with a zero complex part i.e. real numbers, the output should be:

For complex numbers where the real part is zero and the complex part is non-zero, the output should be:

Sample Input

"""
