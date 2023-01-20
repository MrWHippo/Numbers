import math



class fraction:
    def __init__(self, num, den):
        self.num = int(num)
        self.den = int(den)
    
    def sub(self, otherfraction):
        if self.den == otherfraction.den:
            answer = self.num - otherfraction.num
            den = self.den
        else:
            self.num *= otherfraction.den
            otherfraction.num *= self.num
            den = self.den * otherfraction.den
            answer = self.num - otherfraction.num

        answerfraction = fraction(answer, den)
        answerfraction._simplify()
        answerfraction.print()

    def add(self, otherfraction):
        if self.den == otherfraction.den:
            answer = self.num + otherfraction.num
            den = self.den
        else:
            self.num *= otherfraction.den
            otherfraction.num *= self.num
            den = self.den * otherfraction.den
            answer = self.num + otherfraction.num

        answerfraction = (fraction(answer, den))
        answerfraction._simplify()
        answerfraction.print()

    def _simplify(self):
        fact = math.gcd(self.num, self.den)
        self.num /= fact
        self.den /= fact
        
    def print(self):
        print(str(self.num) + "/" + str(self.den))
        


num, den = input("Enter fraction (a/b): ").split("/")
num2, den2 = input("Enter fraction (a/b): ").split("/")

fract1 = fraction(num, den)
fract2 = fraction(num, den)

fract1.add(fract2)

