def check_status(req):
    if req.status_code == 200:
        status = "passed"
    else:
        status = "failed"

    return {"name": "Проверка статуса на запрос данных", "status": f"{status}"}

def check_object(req):
    if len(req.json()) > 0 :
        status = "passed"
    else:
        status = "failed"

    return {"name": "Проверка на наличие объектов", "status": f"{status}"}