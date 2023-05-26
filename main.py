from datetime import datetime, timedelta

days_week = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
}

def get_birthdays_per_week(users):

    # визначення інтервалу, в якому потрібно вітати
    current_time = datetime.now()
    one_week_interval = timedelta(weeks=1)
    max_date = current_time + one_week_interval

    # приведення дати народження до поточного року
    for user in users:
        user['birthday'] = user['birthday'].replace(year=current_time.year)

    # створення нового словнику, де в якості ключа буде імʼя
    dict_user = {}
    for i in users:
        if current_time < i['birthday'] <= max_date:
            if (i['birthday']).weekday() == 5 or (i['birthday']).weekday() == 6:
                dict_user[i['name']] = days_week[0]
            else:
                dict_user[i['name']] = days_week[(i['birthday']).weekday()]

    # cтворення словника, значення це список імениників
    result = {}
    for name, day in dict_user.items():
        if day not in result:
            result[day] = []
        result[day].append(name)

    # роздрук по дням тиждня
    for v in days_week.values():
        for k, j in result.items():
            if v == k:
                print(f'{v}:', ', '.join(j))

users = [
    {'name': 'Bill', 'birthday': datetime(year=1873, month=4, day=30)},
    {'name': 'Jill', 'birthday': datetime(year=2398, month=5, day=31)},
    {'name': 'Jan', 'birthday': datetime(year=1987, month=6, day=1)},
    {'name': 'Sam', 'birthday': datetime(year=1956, month=5, day=27)},
    {'name': 'Kiril', 'birthday': datetime(year=2023, month=5, day=27)},
    {'name': 'Kim', 'birthday': datetime(year=2000, month=4, day=28)}
]

if __name__ == '__main__':
    get_birthdays_per_week(users)