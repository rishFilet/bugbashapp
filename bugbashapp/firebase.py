import pyrebase

class FirebaseDB:
    # Firebase databse information and setup
    config = {
        "apiKey": "AIzaSyBprp7rJwq64GaMhbX-5ST2wb7PS43IVZw",
        "authDomain": "bugbash-b4d18.firebaseapp.com",
        "databaseURL": "https://bugbash-b4d18.firebaseio.com/",
        "storageBucket": "bugbash-b4d18.appspot.com",
    }

    firebase = pyrebase.initialize_app(config)
    authe = firebase.auth()
    database = firebase.database()
