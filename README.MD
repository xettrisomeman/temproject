# Fork this project

## CLone and download

## Do the following

```cmd
cd djdemo
python -m venv newvenv
cd newvenv
cd scripts
activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
