from datetime import datetime, timedelta

current_date = datetime.now()

new_date = current_date - timedelta(days=5)

print("Current date:", current_date.strftime("%Y-%m-%d"))
print("New date after subtracting five days:", new_date.strftime("%Y-%m-%d"))

#example 2
from datetime import datetime, timedelta

current_date = datetime.now()

yesterday = current_date - timedelta(days=1)

tomorrow = current_date + timedelta(days=1)

print("Yesterday:", yesterday.strftime("%Y-%m-%d"))
print("Today:", current_date.strftime("%Y-%m-%d"))
print("Tomorrow:", tomorrow.strftime("%Y-%m-%d"))

#example 3
from datetime import datetime

current_datetime = datetime.now()

datetime_without_microseconds = current_datetime.replace(microsecond=0)

print("Original datetime:", current_datetime)
print("Datetime without microseconds:", datetime_without_microseconds)

#example 4
from datetime import datetime

date1 = datetime(2024, 1, 31, 12, 0, 0)  # First date
date2 = datetime(2024, 2, 5, 12, 0, 0)   # Second date

difference_seconds = abs((date2 - date1).total_seconds())

print("Difference between the two dates in seconds:", difference_seconds)
