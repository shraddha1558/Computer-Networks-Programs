from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    # Check if the cookie exists
    username = request.cookies.get('username')
    
    if username:
        return f'Hello, {username}!'
    else:
        return 'Hello, guest!'

@app.route('/set_cookie/<username>')
def set_cookie(username):
    # Set a cookie on the client
    resp = make_response(f'Cookie has been set for {username}!')
    resp.set_cookie('username', username)  # Set the 'username' cookie
    return resp

@app.route('/delete_cookie')
def delete_cookie():
    resp = make_response('Cookie has been deleted!')
    resp.delete_cookie('username')  # Delete the 'username' cookie
    return resp

if __name__ == '__main__':
    app.run(debug=True)
