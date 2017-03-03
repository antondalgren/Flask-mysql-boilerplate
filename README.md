# Flask mysql boilerplate
Simple python3 flask boilerplate with connection to mysql.

## Requirements
To use this you need python3, flask and mysql-connector plugin.
***

## Installation
Clone or download the files and run the following commands

`pip3 install flask mysql-connector`

To be able to connect to your database you will need to change the database configuration on line 8.

`app.config.update(dict(
    DATABASE="Database",
    USERNAME="username",
    HOST="host",
    PASSWORD="password"
))`

Make sure you have a table in your database called 'users' or just copy the database schema supplied for you.

Now it's time to run the application.

`python3 main.py` and head to localhost:5000 or localhost:5000/users in the browser.
***

## Contribution
If you want to contribute and change something just make a pull request.
***

## Contact
If you want to come in contact with me just send me a mail on anton.dalgren@gmail.com
***
