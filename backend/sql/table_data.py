import json
from uuid import uuid4
from datetime import datetime, timedelta
from decimal import Decimal

# Генерация данных для таблиц

# Users
users_data = [
    {
        "id": str(uuid4()),
        "firstname": f"Firstname{i}",
        "surname": f"Surname{i}",
        "lastname": f"Lastname{i}",
    }
    for i in range(1, 16)
]

# Passwords
passwords_data = [
    {
        "id": user["id"],
        "login": f"user{i}@example.com",
        "hash_pass": f"hashpass{i:02d}"
    }
    for i, user in enumerate(users_data, 1)
]

# Balance
balance_data = [
    {
        "id": user["id"],
        "money": str(Decimal("1000.00") + Decimal(i * 50))
    }
    for i, user in enumerate(users_data, 1)
]

# Deals
start_date = datetime.now()
deals_data = [
    {
        "id": str(uuid4()),
        "id_user": user["id"],
        "sum": str(Decimal("500.00") + Decimal(i * 25)),
        "percent": str(Decimal("5.00") + Decimal(i * 0.1)),
        "date_deal_start": (start_date - timedelta(days=i * 10)).isoformat(),
        "date_deal_end": (start_date + timedelta(days=i * 10)).isoformat(),
        "selled": f"Product{i}",
        "count": i
    }
    for i, user in enumerate(users_data, 1)
]

# Формируем JSON-данные
data = {
    "users": users_data,
    "passwords": passwords_data,
    "balance": balance_data,
    "deals": deals_data
}

# # Сохраняем в файл
# file_path = "table_data.json"
# with open(file_path, "w") as json_file:
#     json.dump(data, json_file, indent=4)

# file_path
