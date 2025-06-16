user_input = int(input("Enter a number between 0 and 8640000: "))

if user_input < 0 or user_input > 8640000:
    print("Error")

convertor = {"days", "hours", "minutes", "seconds"}

seconds = user_input % 60
minutes = (user_input // 60) % 60
hours = (user_input // 3600) % 24
days = user_input // 86400

if days == 1:
    print(f"{days} день, {hours:02d}:{minutes:02d}:{seconds:02d}")
elif 2 <= days <= 4:
    print(f"{days} дні, {hours:02d}:{minutes:02d}:{seconds:02d}")
else:
    print(f"{days} днів, {hours:02d}:{minutes:02d}:{seconds:02d}")