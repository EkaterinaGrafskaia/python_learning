n = int(input("Enter number: "))
last_number = 0
while True:
    number = n % 10
    n = n // 10
    if number >= last_number:
        last_number = number
    if n == 0 or number == 9:
        break
print(last_number)
