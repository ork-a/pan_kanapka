del orders\migrations\*.* /Q
del clients\migrations\*.* /Q
del sandwiches\migrations\*.* /Q
del db.sqlite3
python manage.py makemigrations clients
python manage.py makemigrations sandwiches
python manage.py makemigrations orders
python manage.py migrate
python manage.py filldb