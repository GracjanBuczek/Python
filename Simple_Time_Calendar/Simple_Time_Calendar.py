import time
import calendar

sec = time.time()
print("The UNIX exist",sec,"seconds.")	
local_time = time.ctime(sec)
print("Now it is ",local_time)

yy = int(input("\nChoose year: "))
mm = int(input("Choose month: "))
print(calendar.month(yy,mm))

calendar.setfirstweekday(calendar.SUNDAY)
print('\n',calendar.month(yy,mm))

year=(int(input('Choose the year to find out if it is leap: ')))
print('\nIt is',calendar.isleap(year),'that',year,'is leap')

input("\nPress any key to finish...")
