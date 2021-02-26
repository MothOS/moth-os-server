from bottle import route


@route('/')
def handle():
    return "Welcome to mothOS"
