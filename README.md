# bugbashapp
A web app for running the different bug bashes remotely and independently

## FIRST TIME SETUP FOR DEVELOPMENT:
- Clone the repo
- Navigate to the repo and activate the environment (you will need to have virtual env installed before doing this step)

`source venv/bin/activate`

- Install the dependencies

`pip install -r requirements.txt`

- Recommend to use pycharm as its easier to work with. Open the project folder with pycharm
- When the project is open, edit configuration for the project
- Hit the + button and select Python from the list
- You will need to create 2 configurations
  1. Run Server - this will be used to run the local server to see your changes to the website
    - Name the configuration 'Run Server'
    - Under script path, point to where `manage.py` is hosted on your git repo
    - Under parameters, enter `runserver`
  2. Migrate - When there are changes made to settings, views or models in the django files, this need to be run if any migrations need to be applied before running the server
    - Name the configuration 'Migrate'
    - Under script path, point to where `manage.py` is hosted on your git repo
    - Under parameters, enter `migrate`
- Now hit play for `runserver` and then open the browser with the address `127.0.0.1:8888`
