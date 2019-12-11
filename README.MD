# Fork this project

## Do the following

```cmd
mkdir djangoproject
git clone --this project url
cd djangoproject
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
