from datetime import date, time, datetime, timedelta

print(datetime.now())
print(datetime(2020, 10, 10))
print(datetime(2020, 10, 10).strftime("%Y %B %d."))
print(datetime(2020, 10, 10).isoformat())
print(datetime.strptime("2022-10-10", "%Y-%m-%d"))
print(datetime.now() + timedelta(minutes=10))
print((datetime(2020, 10, 10) - datetime(2020, 5, 10)).days)

d = date(2005, 7, 14)
t = time(12, 30)
print(datetime.combine(d, t))

# i = 09