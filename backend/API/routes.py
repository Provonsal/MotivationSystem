from typing import Union
from fastapi import Body
from fastapi.responses import HTMLResponse
from API.app import app
import uuid

#заглушка для функций
async def get_hash_password(user_id: uuid.UUID) -> str:
    ...

async def get_login(user_id: uuid.UUID) -> str:
    ...

async def get_FIO_by_id(user_id: uuid.UUID) -> dict:
    ...
    return {"firstname": ..., "lastname": ..., "surname": ...}

async def get_id_by_login(login: str) -> str:
    
    return ""

async def get_salary_and_bonus(user_id: uuid.UUID, date: str) -> dict[
        str: int, 
        str: int
    ]:
    ...
    return {"salary": ...,
            "bonus": ...}

# тут должно вернуть лист с кучей словарей с данными людей, отсортированными по уменьшению.
async def get_rating() -> list[dict[
        str: str, 
        str: str, 
        str: str, 
        str: str, 
        str: int, 
        str: int
    ]]:
    ...
    return [{
             "id": ..., 
             "name": ..., 
             "surname": ..., 
             "lastname": ..., 
             "salary": ..., 
             "bonus": ...
             },
             ...]

# тут должно вернуть лист с кучей словарей с сделками, отсортированными от свежих к старым.
async def get_deals(user_id: uuid.UUID) -> list[dict[
        str: str, 
        str: int, 
        str: int, 
        str: str, 
        str: str, 
        str: str
    ]]:
    ...
    return [{
             "deal_id": ..., 
             "sum": ..., 
             "percent": ..., 
             "deal_start_date": ..., 
             "deal_end_date": ..., 
             "selled": ...
             }, 
             ...]

async def set_new_user(name: str, surname: str, lastname: str) -> dict[str:str]:
    # вставить фио юзера в БД и сгенерировать пароль и логин и вернуть их
    ...
    return {"login": ..., "password": ...}

# такой шаблон рутов
@app.post("/password")
async def check_data(login: str = Body(embed=True), 
                     password: str = Body(embed=True)):

    """
    Функция для проверки данных для входа, принимает в теле запроса пароль и логин и находит человека с таким логином, его id.
    И сравнивает логин и пароль в БД с переданными в запросе. Если совпадает, то возвращает результат ok и id найденного человека, и его фио.

    :param body: json `{\"login\": ...}`
    :type body: `fastapi.Body()`

    :return: HTMLResponse 400 либо {"result": "ok", "id": id, "firstname": ..., "lastname": ..., "surname": ...}, где id это найденный id пользователя по его логину.
    :rtype: `HTMLResponse 400` | `dict`
    """

    id: uuid.UUID = await get_id_by_login(login)
    
    fio: dict = await get_FIO_by_id(id)

    if id is not None:
        real_login: str = await get_login(id)
        real_password: str = await get_hash_password(id)
        if real_login == login and real_password == password:
            return {"result":"ok",
                    "id":id,
                    "firstname": fio["firstname"],
                    "lastname": fio["lastname"],
                    "surname": fio["surname"]}
        else:
            return HTMLResponse(status_code=400)
    else:
        return HTMLResponse(status_code=404)
    
@app.post("/salary/month")
async def month_salary(id: uuid.UUID = Body(embed=True), 
                       month: str = Body(embed=True)):
    
    """
    Функция принимает в теле id пользователя и месяц за который нужно получить зарплату и его премию.

    :param body: json `{\"id\": ..., \"month\": ...}`
    :type body: `fastapi.Body()`

    :return: HTMLResponse 400 либо "result": "ok", "salary": salary_and_bonus["salary"], "bonus": salary_and_bonus["bonus"]}, где salary и bonus это зарплата и премия за месяц.
    :rtype: `HTMLResponse 400` | `dict`
    """

    salary_and_bonus: dict = await get_salary_and_bonus(id, month)

    if salary_and_bonus is not None:
        return {"result": "ok", 
                "month": month,
                "salary": salary_and_bonus["salary"], 
                "bonus": salary_and_bonus["bonus"]}
    else:
        return HTMLResponse(status_code=404)

@app.post("/rating")
async def month_salary():
    
    """
    Функция выдает список всех людей, упорядоченный по сумме их оклада, от большего к меньшему.

    :return: HTMLResponse 400 либо "result": "ok", [{"id": ..., "name": ..., "surname": ..., "lastname": ..., "salary": ..., "bonus": ...}, ...]}, где salary и bonus это зарплата и премия за месяц.
    :rtype: `HTMLResponse 400` | `list[dict]`
    """

    rating: list[dict] = await get_rating()

    if rating is not None:
        return {"result": "ok", 
                "rating": rating}
    else:
        return HTMLResponse(status_code=404)
    
@app.post("/deals")
async def employee_deals(id: uuid.UUID = Body(embed=True)):
    
    """
    Функция выдает список сделок пользователя, упорядоченный по дате, от свежих, к старым. По умолчанию за текущий месяц.

    :param body: json `{\"id\": ...}`
    :type body: `fastapi.Body()`

    :return: HTMLResponse 400 либо "result": "ok", [{"deal_id": ..., "sum": ..., "percent": ..., "deal_start_date": ..., "deal_end_date": ..., "selled": ...}, ...]}.
    :rtype: `HTMLResponse 400` | `list[dict]`
    """

    deals: list[dict] = await get_deals(id)

    if deals is not None:
        return {"result": "ok", 
                "deals": deals}
    else:
        return HTMLResponse(status_code=404)
    
@app.post("/register")
async def register(name: str = Body(embed=True), 
                   surname: str = Body(embed=True), 
                   lastname: str = Body(embed=True)):
    
    """
    Функция для регистрации пользователя в системе. Принимает в теле запроса имя, фамилию и отчество.

    :param body: json `{\"name\": ..., \"surname\": ..., \"lastname\": ...}`
    :type body: `fastapi.Body()`

    :return: HTMLResponse 400 либо "result": "ok", "login": ..., "password": ...}.
    :rtype: `HTMLResponse 400` | `list[dict]`
    """

    if name is not None and surname is not None and lastname is not None:
        pass_and_log: dict = await set_new_user(name, surname, lastname)
        return {"result": "ok", 
                "login": pass_and_log["login"], 
                "password": pass_and_log["password"]}
    else:
        return HTMLResponse(status_code=400)