from wsgiref.simple_server import make_server
import wsgi.wsgi_app as w_app

def main():
    httpd = make_server('', 8000, w_app.wsgi_app)
    print("Started app serving on port 8000...")
    httpd.serve_forever()


if __name__ == "__main__":
    main()
