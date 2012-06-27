from tornado import web
import greenlet
from functools import wraps

def greenletify(function):
    @wraps(function)
    def wrapped(*args, **kwargs):
        gr = greenlet.greenlet(function)
        return gr.switch(*args, **kwargs)
    return wrapped


class RequestHandler(web.RequestHandler):
    """Tornado's request handler, with all user code executed inside a greenlet

    See Tornado's documentation for RequestHandler.
    """

    _execute = greenletify(web.RequestHandler._execute)
