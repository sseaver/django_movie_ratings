# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-05 18:13
from __future__ import unicode_literals
import csv
from django.db import migrations


def add_info(apps, schema_editor):
    Rater = apps.get_model("movie_app", "Rater")
    Movie = apps.get_model("movie_app", "Movie")
    Data = apps.get_model("movie_app", "Data")

    with open("u.user.csv", encoding="latin1") as open_file:
        reader = csv.reader(open_file, delimiter="|")
        for row in reader:
            Rater.objects.create(id=row[0], age=row[1], gender=row[2], occupation=row[3], zipcode=row[4])
        print (row)

    # raise Exception("BOOMSHAKALAKA")

    with open("u.item.csv", encoding="latin1") as open_file:
        reader = csv.reader(open_file, delimiter="|")
        for row in reader:
            Movie.objects.create(id=row[0], name=row[1], date=row[2], video_release=row[3], imdb_url=row[4],
                                 unknown=row[5], action=row[6], adventure=row[7], animation=row[8], childrens=row[9],
                                 comedy=row[10], crime=row[11], documentary=row[12], drama=row[13], fantasy=row[14],
                                 filmnoir=row[15], horror=row[16], musical=row[17], mystery=row[18], romance=row[19],
                                 scifi=row[20], thriller=row[21], war=row[22], western=row[23])
        print (row)
    # raise Exception("BOOMSHAKALAKA")

    with open("u.data.csv", encoding="latin1") as open_file:
        reader = csv.reader(open_file, delimiter="\t")
        for row in reader:
            userid = Rater.objects.get(id=row[0])
            itemid = Movie.objects.get(id=row[1])
            Data.objects.create(userid=userid, itemid=itemid, rating=row[2], timestamp=row[3])
        print (row)
    # raise Exception("BOOMSHAKALAKA")


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_info)
    ]
