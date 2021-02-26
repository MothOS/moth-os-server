from bottle import route
from moth_os import __version__


@route('/version')
def handle():
    return f"{__version__}"
