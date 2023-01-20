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
            tempden = self.den
            self.num *= otherfraction.den
            self.den *= otherfraction.den
            otherfraction.num *= tempden

            answer = self.num - otherfraction.num
            den = self.den

        answerfraction = (fraction(answer, den))
        answerfraction.__simplify()
        answerfraction.print()

    def add(self, otherfraction):
        if self.den == otherfraction.den:
            answer = self.num + otherfraction.num
            den = self.den
        else:
            tempden = self.den
            self.num *= otherfraction.den
            self.den *= otherfraction.den
            otherfraction.num *= tempden

            answer = self.num + otherfraction.num
            den = self.den

        answerfraction = (fraction(answer, den))
        answerfraction.__simplify()
        answerfraction.print()


    def multi(self, otherfraction):
        den = self.den * otherfraction.den
        answer = self.num * otherfraction.num
        answerfraction = (fraction(answer, den))
        answerfraction.__simplify()
        answerfraction.print()


    def div(self, otherfraction):
        tempnum = otherfraction.num
        otherfraction.num = otherfraction.den
        otherfraction.den = tempnum

        den = self.den * otherfraction.den
        answer = self.num * otherfraction.num
        answerfraction = (fraction(answer, den))
        answerfraction.__simplify()
        answerfraction.print()


    def __simplify(self):
        fact = math.gcd(self.num, self.den)
        self.num = int(self.num / fact)
        self.den = int(self.den / fact)
        
        
        
    def print(self):
        if int(den) == 1:
            print(str(self.num))
        else:
            print(str(self.num) + "/" + str(self.den))
        


num, den = input("Enter fraction (a/b): ").split("/")
num2, den2 = input("Enter fraction (a/b): ").split("/")

fract1 = fraction(num, den)
fract2 = fraction(num2, den2)

option = input("Enter operation(+, -, * or /): ")
if option == "+":
    fract1.add(fract2)
elif option == "/":
    fract1.div(fract2)
elif option == "*":
    fract1.multi(fract2)
elif option == "-":
    fract1.sub(fract2)
else:
    print("Error, Invalid operation.")
