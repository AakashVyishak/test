# Generated by Django 3.2 on 2021-04-09 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museumapp', '0003_item_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('im', models.ImageField(upload_to='picture')),
            ],
        ),
    ]
