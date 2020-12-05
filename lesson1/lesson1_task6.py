a = int(input("Enter achieved distance: "))
b = int(input("Enter desired distance: "))
n = 1
while True:
    if a >= b:
        break
    else:
        a = a * 1.1
        n += 1
print(f"You will achieve your goal within {n} days!")
