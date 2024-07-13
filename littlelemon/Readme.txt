I used  pipenv to manage my dependencies so use pipenv install when you are on the project directory to install all dependencies
then use pipenv shell to start the virtual environment


Endpoints to test

for user registeration
http://127.0.0.1:8000/auth/users/

for token creation
http://127.0.0.1:8000/auth/token/login/

for viewing and adding menus to the menu model
http://127.0.0.1:8000/restaurant/menu/

for deleting and updating a menu
http://127.0.0.1:8000/restaurant/menu/1

for viewing and adding booking to the book model
http://127.0.0.1:8000/restaurant/booking/
