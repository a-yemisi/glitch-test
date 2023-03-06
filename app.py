from flask import Flask, request
app = Flask(__name__)
 
@app.route('/')
def webhook():
   return "Hello world", 200
 
if __name__ == "__main__":
   app.run(debug=True)
