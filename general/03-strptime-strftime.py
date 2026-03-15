from datetime import datetime

# strptime: parse a string to datetime
dttm_str = "01-31-2020 14:45:37"
format_str = "%m-%d-%Y %H:%M:%S"
dttm = datetime.strptime(dttm_str, format_str)
dttm

# strftime: fstring a datetime
dttm.isoformat()
dttm.isoformat(sep=" ")
dttm.strftime("%d %B %Y")
dttm.strftime("%A, %B %d, %Y")
f"{dttm:%A, %B %d}"

# cheatsheet: https://strftime.org/
# ref: https://realpython.com/python-get-current-time
#      https://realpython.com/python-datetime/
