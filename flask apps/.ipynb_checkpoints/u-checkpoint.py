from flask import Flask
app = Flask(__name__)
app.debug = True
@app.route("/hello")
def hello_world():
   return 'my name is willson'

@app.route()
)
def newf():
   return "this is new function"

@app.route("/user/<username>/")## this is canonical url. also can be used as user/willson or user/willson/ both are same
def user(username):
   return f'Hello {username}'
@app.route("/post/<float:id>")
def post(id):
   return f'you are in post {id}'


if __name__ == '__main__':
   app.run( host="0.0.0.0")