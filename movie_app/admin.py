from django.contrib import admin
from movie_app.models import Rater, Data, Movie
# Register your models here.
admin.site.register([Rater, Data, Movie])
