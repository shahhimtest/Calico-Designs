# Generated by Django 3.1 on 2020-12-14 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('petname', models.CharField(max_length=50)),
                ('cat_img', models.ImageField(upload_to='image')),
                ('cat_drawing', models.ImageField(default='no_image.jpg', upload_to='drawings')),
                ('addr1', models.CharField(max_length=50)),
                ('addr2', models.CharField(max_length=50)),
                ('itn', models.CharField(blank=True, max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('postcode', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('venmo', models.CharField(max_length=50)),
                ('show', models.BooleanField(default=True)),
            ],
        ),
    ]