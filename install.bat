set email="admin@amdin.ru"
python -m venv env && ^
.\env\Scripts\activate && ^
pip install -r req.txt && ^
python manage.py makemigrations && ^
python manage.py migrate && ^
python manage.py createsuperuser --email %email% && ^
python manage.py runserver