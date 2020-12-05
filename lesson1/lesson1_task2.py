n = int(input("Enter number: "))
import time

# hours = n // 3600
# seconds = n % 60
# minutes = (n - hours * 3600 - seconds) // 60
# print(hours, minutes, seconds)
print(time.strftime("%H:%M:%S", time.gmtime(n)))
