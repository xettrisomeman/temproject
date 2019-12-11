from django.db import models


class Home_carousel_one(models.Model):
    img  = models.ImageField(upload_to="static/img/carosuel/Home")
    date = models.DateTimeField(auto_now_add=True, auto_now=False)


