from flask import Flask, request, abort, make_response, render_template
import time
import hmac
import base64

encryption = 'utf-8'
key = 'TG91aXMgTGVjbGFpcgo'.encode(encryption)  #the key is Louis Leclair base64

app = Flask(__name__)

cookie_name = "LoginCookie"

def is_tampered(cookie, hashmac):
    real_hash = hmac.new(key, cookie.encode(encryption)).hexdigest()
    return real_hash != hashmac

@app.route("/login",methods=['POST'])
def login():
    usr = request.form['username']
    pwd = request.form['password']
    ts = int(time.time())
    if usr == 'admin' and pwd == '42':
        cookie = '{},{},com402,hw2,ex2,admin'.format(usr, ts)
    else:
        cookie = '{},{},com402,hw2,ex2,user'.format(usr, ts)
    hashmac = hmac.new(key, cookie.encode(encryption)).hexdigest()
    cookie += ',{}'.format(hashmac)
    cookie = base64.b64encode(cookie.encode(encryption)).decode(encryption)
    resp = make_response()
    resp.set_cookie(cookie_name, cookie)
    return resp

@app.route("/auth",methods=['GET'])
def auth():
    cookie = request.cookies.get(cookie_name)
    if cookie:
        cookie = base64.b64decode(cookie.encode(encryption)).decode(encryption)
        cookie = cookie.split(',')

        new_cookie = ','.join(cookie[:-1])
        if is_tampered(new_cookie, cookie[-1]):
            return make_response('Code 403 if the cookie has been tampered.'), 403 
        is_admin = cookie[-2] == 'admin'
        if is_admin:
            return make_response('Code 200 if the user is the administrator.'), 200
        else:
            return make_response('Code 201 if the user is a simple user.'), 201
    else:
        return make_response('Code 403 if no cookie is present.'), 403

if __name__ == '__main__':
    app.run()

