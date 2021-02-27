from bottle import route, Response


@route('/ping')
def handle_ping():
    print("Ping...")
