import pyrebase
from flask import Flask

config = {
    "apiKey": "AIzaSyBHJa2wPkBpklLoSnPM_l_hYgw7NcY5XA0",
  "authDomain": "bintween-e0b79.firebaseapp.com",
  "databaseURL": "https://bintween-e0b79.firebaseio.com",
  "projectId": "bintween-e0b79",
  "storageBucket": "bintween-e0b79.appspot.com",

}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

app = Flask(__name__)


@app.route('/')
def hello_world():
    ids = db.child("ID")
    print(ids.child("2").child("adress").get().val())
    return ids.child("2").val()



if __name__ == '__main__':
    app.run()
