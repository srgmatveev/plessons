import importlib
import re


def check_var_is_none(var=None):
    if var is None:
        return True
    return False


def check_favicon_like(strVal=None):
    arr = ['/favicon.ico']
    if strVal.lower() in arr:
        return True
    return False


def strip_first_slash(strVal=None):
    return re.sub(r'^(/*?)', '', strVal, flags=re.IGNORECASE)


def replace_slashes_by_dots(strVal=None):
    return strVal.replace('/', '.')


def prepare_path(strVal=None):
    strVal = replace_slashes_by_dots(strip_first_slash(strVal))
    if not strVal:
        strVal = 'root'
    return strVal


def full_check_path_info(requsetMethod=None, pathInfo=None):
    if check_var_is_none(var=requsetMethod) is True:
        return True
    if check_var_is_none(var=pathInfo) is True:
        return True
    if check_favicon_like(strVal=pathInfo) is True:
        return True


def handle_request_action(requsetMethod=None, pathInfo=None, queryString=None):
    if full_check_path_info(requsetMethod=requsetMethod, pathInfo=pathInfo) is True:
        return
    try:
        i = importlib.import_module(f'wsgi.views.{prepare_path(pathInfo)}')
        return i.view_function()
    except ModuleNotFoundError:
        return {'status': '404 PAGE_NOT_FOUND', 'text': b'Page not found!'}


def wsgi_app(environ, start_response):
    '''
    (dict, callable( status: str,
                     headers: list[(header_name: str, header_value: str)]))
                  -> body: iterable of strings
    '''
    resp = handle_request_action(requsetMethod=environ['REQUEST_METHOD'],
                                 pathInfo=environ['PATH_INFO'], queryString=environ['QUERY_STRING'])
    response_headers = [('Content-type', 'text/plain')]
    if resp is None:
        status = '200 OK'
        text = b''
    else:
        status = resp.get('status')
        text = resp.get('text')
    start_response(status, response_headers)
    return [text]
