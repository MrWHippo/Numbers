
i = int(input("1. Convert denary to Roman numerials \n2. Conver Roman numerials to denary :"))

if i == 1:
    InNum = int(input("Enter a Number: "))

    RomanNums = {1: "I",4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C",400: "CD", 500: "D", 900: "CM", 1000: "M"}

    left = True
    answer = []

    for x in reversed(RomanNums):
        while (InNum - x) >= 0:
            answer.append(RomanNums[x])
            InNum -= x

    print("".join(answer))

else:

    Roman = input("Enter Roman Numerials: ").upper()

    RomanNums = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    RomanBNums = { "IV": 4,"IX": 9,"XL": 40,"XC": 90,"CD": 400,"CM": 900}

    left = True
    answer = 0

    

    for x in reversed(RomanBNums):
        if x in Roman:
            answer += RomanBNums[x]
            Roman = Roman.replace(x, "")

    
    Romanlist = list(Roman)

    for x in reversed(RomanNums):
        count = Romanlist.count(x)
        answer += (RomanNums[x] * count)

    print(answer)

