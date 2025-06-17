user_input = int(input("Enter a number between 0 and 8640000: "))

if user_input < 0 or user_input > 8640000:
    print("Error")

convertor = {"seconds": user_input % 60, "minutes": (user_input // 60) % 60, "hours": (user_input // 3600) % 24,
             "days": user_input // 86400}

days = convertor["days"]
if days % 10 == 1 and days % 100 != 11:
    print(f"{days} день, {convertor["hours"]:02d}:{convertor["minutes"]:02d}:{convertor["seconds"]:02d}")
elif 2 <= days % 10 <= 4 and (days % 100 < 10 or days % 100 >= 20):
    print(f"{days} дні, {convertor["hours"]:02d}:{convertor["minutes"]:02d}:{convertor["seconds"]:02d}")
else:
    print(f"{days} днів, {convertor["hours"]:02d}:{convertor["minutes"]:02d}:{convertor["seconds"]:02d}")