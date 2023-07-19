def number_to_day(num=0):
    day = ["月曜日", "火曜日", "水曜日", "木曜日", "金曜日", "土曜日", "日曜日"]
    if num in range(-2, 5):
        return day[num + 2]
    elif num >= 5:
        return "来週"
    else:
        return "先週"


print(number_to_day())
print(number_to_day(1))
print(number_to_day(2))
print(number_to_day(3))
print(number_to_day(4))
print(number_to_day(-1))
print(number_to_day(-2))
print(number_to_day(5))
print(number_to_day(-3))
