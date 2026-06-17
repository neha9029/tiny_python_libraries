from math import gcd

class Fraction:
   
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")

        g = gcd(numerator,denominator)

        numerator = numerator // g
        denominator = denominator // g

        if denominator < 0:
            numerator = -numerator
            denominator = -denominator
        
        self.numerator = numerator 
        self.denominator = denominator
        
    def __repr__(self):
        return f"{self.numerator}/{self.denominator}"
    
    def __add__(self, other):
        num = (self.numerator * other.denominator + self.denominator * other.numerator)
        den = self.denominator * other.denominator

        return Fraction(num,den)

    def __sub__(self, other):
        num = (self.numerator * other.denominator - self.denominator * other.numerator)
        den = self.denominator * other.denominator

        return Fraction(num, den)

    def __mul__(self, other):
        num = self.numerator * other.numerator
        den = self.denominator * other.denominator

        return Fraction(num, den)

    def __truediv__(self, other):
        if other.numerator == 0:
            raise ValueError("Cannot divide by zero")

        num = self.numerator * other.denominator
        den = self.denominator * other.numerator

        return Fraction(num, den)
    
    def __eq__(self, other):
        return (
            self.numerator == other.numerator 
            and 
            self.denominator == other.denominator
        )

    def __lt__(self, other):

        return self.numerator * other.denominator < self.denominator * other.numerator

    def __gt__(self, other):
        return self.numerator * other.denominator > self.denominator * other.numerator


    def __le__(self, other):
        return self == other or self < other

    def __ge__(self, other):
        return self == other or self > other

    
    def __float__(self):
        return self.numerator / self.denominator