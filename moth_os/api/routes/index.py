from bottle import route


@route('/')
def handle_index():
    return "Welcome to mothOS"
