from datetime import datetime, timedelta
from collections import defaultdict

users = [
    {
        "name": "Bill",
        "birthday": datetime(2000, 5, 27)
    },
    {
        "name": "Alex",
        "birthday": datetime(2000, 5, 29)
    },
    {
        "name": "Kim",
        "birthday": datetime(2000, 5, 30)
    },
    {
        "name": "Anna",
        "birthday": datetime(2000, 5, 30)
    },
    {
        "name": "Kate",
        "birthday": datetime(2000, 6, 2)
    },
]


def get_birthdays_per_week(users):
    current_date = datetime.now() + timedelta(days=1)
    while current_date.weekday():
        current_date += timedelta(days=1)
    birthday_dict = defaultdict(list)
    monday = current_date.date()
    previous_saturday = monday - timedelta(days=2)
    friday = (current_date + timedelta(days=4)).date()
    for user in users:
        user_birthday = user["birthday"].replace(year=current_date.year).date()
        if previous_saturday <= user_birthday <= friday:
            if previous_saturday <= user_birthday <= monday:
                birthday_dict[monday].append(user["name"])
            elif user_birthday <= friday:
                birthday_dict[user_birthday].append(user["name"])
    for birthday in birthday_dict:
        print(
            f"{birthday.strftime('%A')}: {', '.join(birthday_dict[birthday])}")


get_birthdays_per_week(users)
