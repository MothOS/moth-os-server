from bottle import route
from moth_os import __version__


@route('/version')
def handle_version():
    return f"{__version__}"
