"""
birthday.py
Author: Alice Frederick
Credit: Tutorials, and then my friend Emma S. 
Assignment: Birthday Quiz

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todaydate = datetime.today().day

name = input('Hello, what is your name? ')
month = input('Hi {0}, what was the name of the month you were born in? '.format(name))
year = int(input('And what year were you born in, {0}? '.format(name)))
day = int(input('And the day? '))

if month is 'October' and day == 31:
    print('You were born on Halloween!')
elif month == todaymonth and todaydate == day:
    print("Happy birthday!")
    
    
elif month == "December" or month == "January" or month == "February":
    season = 'you are a winter baby'
elif month == "March" or month == "April" or month == "May":
    season = 'you are a spring baby'
elif month == "June" or month == "July" or month == "August":
    season = 'you are a summer baby'
elif month == "September" or month == "October" or month == "November":
    season = 'you are a fall baby'
    
if year < 1980:
    era = 'of the Stone Age'
if year in [1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989]:
    era = 'of the eighties'
if year in [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999]:
    era = 'of the nineties'
if year >= 2000:
    era = 'of the two thousands'
    
print('{0}, {1} {2}.'.format(name, season, era))







