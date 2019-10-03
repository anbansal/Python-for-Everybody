print("Score\tGrade")
print(">=0.9\tA")
print(">=0.8\tB")
print(">=0.7\tC")
print(">=0.6\tD")
print("<0.6\tF")

prompt="Enter score: "
score=input(prompt)
try:
    scoreNum = float(score)
except:
    print("Bad score")
    quit(0)
if scoreNum >= 0.9:
    print("A")
elif scoreNum >= 0.8:
    print("B")
elif scoreNum >= 0.7:
    print("C")
elif scoreNum >= 0.6:
    print("D")
elif scoreNum < 0.6:
    print("F")
