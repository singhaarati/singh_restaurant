# Generated by Django 3.0.2 on 2022-07-21 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('itemname', models.CharField(default='', max_length=100)),
                ('itemprice', models.CharField(default='', max_length=100)),
                ('image', models.FileField(default='default.jpg', upload_to='static/images/item')),
            ],
            options={
                'db_table': 'owner',
            },
        ),
    ]
