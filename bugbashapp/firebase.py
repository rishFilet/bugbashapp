import pyrebase

class FirebaseDB:
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

    def __init__(self):
        self.firebase = pyrebase.initialize_app(self.config)
        self.authe = self.firebase.auth()
        self.database=self.firebase.database()
