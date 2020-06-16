
def february(year):
	if year % 4 == 0:
		return 29
	else:
		return 28

year = 1
currentDayCount = -2
result = 0

months = [
  31, 
  february(year),
  31,
  30,
  31,
  30,
  31,
  31,
  30,
  31,
  30,
  31
]

while year <= 100:
  for month in months:
  	currentDayCount += month
  	if (currentDayCount + 1) % 7 == 0:
  		result += 1
  year += 1

print result
