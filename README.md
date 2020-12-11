# Proccessing Data

In order to insert data into SQLite database, needed to clean/process data and this came in two main forms.

## Booleans

Since SQLite handles booleans using integers (0 = False, 1 = True) all booleans were converted to binary integers

## Datetime

Originally the datetime format was 
m/d/yyyy h:mm:ss 
using PM/AM

Whereas SQLite takes datetime by storing it in either TEXT, REAL, OR INT.
I chose to use TEXT, thereby needing to convert it to
yyyy/mm/dd hh:mm:ss.000

SQLite necessitates that miliseconds are added so I added 0's to fill it as it wouldnt change the data in any signficant way.

