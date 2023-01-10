import time
InNum = int(input("Enter Number to convert to roman numerials: "))

RomanNums = {1: "I",4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C",400: "CD", 500: "D", 900: "CM", 1000: "M", 4000: "MV", 5000: "V"}

left = True
answer = []

time1 = time.perf_counter()
for x in reversed(RomanNums):
    while (InNum - x) >= 0:
        answer.append(RomanNums[x])
        InNum -= x
time2 = time.perf_counter()

timetook = time2 - time1

print("".join(answer))
print(timetook, "Seconds")
