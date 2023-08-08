import calendar

year = 2023
month = 8

cal = calendar.monthcalendar(year, month)

days = ["月", "火", "水", "木", "金", "土", "日"]

print(f"{year}年{month}月")
print("月  火  水  木  金  土  日")

for week in cal:
    for day in week:
        if day == 0:
            print("   ", end=" ")
        else:
            print(f"{day:2} ", end=" ")
    print()
