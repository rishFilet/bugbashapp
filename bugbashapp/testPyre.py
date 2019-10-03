import pyrebase

config = {
        'apiKey': "AIzaSyBprp7rJwq64GaMhbX-5ST2wb7PS43IVZw",
        'authDomain': "bugbash-b4d18.firebaseapp.com",
        'databaseURL': "https://bugbash-b4d18.firebaseio.com",
        'projectId': "bugbash-b4d18",
        'storageBucket': "",
        'messagingSenderId': "356090318351",
        'appId': "1:356090318351:web:e865ba40d674301fe59d7a",
        'measurementId': "G-FQR855D0DY"
    }

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database= firebase.database()

user = authe.create_user_with_email_and_password("random@gmail.com", "crazy_password")
print(user)