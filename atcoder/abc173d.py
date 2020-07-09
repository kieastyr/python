n = int(input())
result = {"AC": 0, "WA": 0, "TLE": 0, "RE": 0}
for i in range(n):
    result[input()] += 1

for l in ["AC", "WA", "TLE", "RE"]:
    print(f"{l} x {result[l]}")