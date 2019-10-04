import pyrebase

#Firebase databse information and setup
config = {
  "apiKey": "AIzaSyBprp7rJwq64GaMhbX-5ST2wb7PS43IVZw",
  "authDomain": "bugbash-b4d18.firebaseapp.com",
  "databaseURL": "https://bugbash-b4d18.firebaseio.com/",
  "storageBucket": "bugbash-b4d18.appspot.com",
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()
user = authe.create_user_with_email_and_password("rishi.rkhan@gmail.com", "mutant")
print(user)
database.child("users").child(user['localId']).set(user['localId'],user['idToken'])
all_users = database.child("users").get()
for user in all_users.each():
    print(user.key())  # Morty
    print(user.val())