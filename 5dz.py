n = int(input())
hour = n//60//60
minuts = (hour*60)-(n//60)
print(hour,"час(а/ов)","и",abs(minuts),"минут(а/ы)")