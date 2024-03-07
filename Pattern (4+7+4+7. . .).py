n = int(input("Please enter the number of numbers: "))
term = 4
total = 0
for i in range(n):
    total = total + term
    print (f"For i = {i} term = {term}...")
    # term = ???   assignment statement
    term = 7 if (i%2 == 0) else 4
print (f"So for n = {n} total = {total}...")
