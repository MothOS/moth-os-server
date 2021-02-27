from bottle import route, request
import json

@route('/monitor', method='POST')
def handle_monitor():
    print(request.json)


