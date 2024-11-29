from typing import Union
from fastapi import Body
from fastapi.responses import HTMLResponse
from API.app import app


#заглушка для функций
async def get_hash_password(user_id: int) -> str:
    ...

async def get_login(user_id: int) -> str:
    ...

async def get_id_by_login(login: str) -> str:
    ...

async def get_salary_and_bonus(user_id: str, date: str) -> dict[
        str: int, 
        str: int
    ]:
    ...
    return {"salary": ..., "bonus": ...}

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
    return [{"id": ..., "name": ..., "surname": ..., "lastname": ..., "salary": ..., "bonus": ...}, ...]

# тут должно вернуть лист с кучей словарей с сделками, отсортированными от свежих к старым.
async def get_deals(user_id: int) -> list[dict[
        str: str, 
        str: int, 
        str: int, 
        str: str, 
        str: str, 
        str: str
    ]]:
    ...
    return [{"deal_id": ..., "sum": ..., "percent": ..., "deal_start_date": ..., "deal_end_date": ..., "selled": ...}, ...]


# такой шаблон рутов
@app.get("/password")
async def check_data(body = Body()) -> Union[HTMLResponse, dict]:

    """
    
    Функция для проверки данных для входа, принимает в теле запроса пароль и логин и находит человека с таким логином, его id.
    И сравнивает логин и пароль в БД с переданными в запросе. Если совпадает, то возвращает результат ok и id найденного человека.

    :param body: json body
    :type body: `fastapi.Body()`

    :return: HTMLResponse 400 либо {"result": "ok", "id": id}, где id это найденный id пользователя по его логину.
    :rtype: `HTMLResponse 400` | `dict`
    """

    id = get_id_by_login(body["login"])
    if id is not None:
        real_login: str = await get_login(id)
        real_password: str = await get_hash_password(id)
        if real_login == body["password"] and real_password == body["login"]:
            return {"result":"ok","id":id}
        else:
            return HTMLResponse(400)
    else:
        return HTMLResponse(400)
    
@app.get("/salary/month")
async def month_salary(body = Body()):
    
    """
    
    Функция принимает в теле id пользователя и месяц за который нужно получить зарплату и его премию.

    :param body: json body
    :type body: `fastapi.Body()`

    :return: HTMLResponse 400 либо "result": "ok", "salary": salary_and_bonus["salary"], "bonus": salary_and_bonus["bonus"]}, где salary и bonus это зарплата и премия за месяц.
    :rtype: `HTMLResponse 400` | `dict`
    
    """
    
    id: str = body["id"]

    month: str = body["month"]

    salary_and_bonus: dict = await get_salary_and_bonus(id, month)

    if salary_and_bonus is not None:
        return {"result": "ok", "salary": salary_and_bonus["salary"], "bonus": salary_and_bonus["bonus"]}
    else:
        return HTMLResponse(400)

@app.get("/rating")
async def month_salary():
    
    """
    
    Функция выдает список всех людей, упорядоченный по сумме их оклада, от большего к меньшему.

    :param body: json body
    :type body: `fastapi.Body()`

    :return: HTMLResponse 400 либо "result": "ok", [{"id": ..., "name": ..., "surname": ..., "lastname": ..., "salary": ..., "bonus": ...}, ...]}, где salary и bonus это зарплата и премия за месяц.
    :rtype: `HTMLResponse 400` | `list[dict]`
    
    """

    rating: list[dict] = get_rating()

    if rating is not None:
        return {"result": "ok", "rating": rating}
    else:
        return HTMLResponse(400)
    
@app.get("/deals")
async def employee_deals(body = Body()):
    
    """
    
    Функция выдает список сделок пользователя, упорядоченный по дате, от свежих, к старым. По умолчанию за текущий месяц.

    :param body: json body
    :type body: `fastapi.Body()`

    :return: HTMLResponse 400 либо "result": "ok", [{"deal_id": ..., "sum": ..., "percent": ..., "deal_start_date": ..., "deal_end_date": ..., "selled": ...}, ...]}.
    :rtype: `HTMLResponse 400` | `list[dict]`
    
    """

    id: str = body["id"]

    deals: list[dict] = get_deals(id)

    if deals is not None:
        return {"result": "ok", "deals": deals}
    else:
        return HTMLResponse(400)
    
