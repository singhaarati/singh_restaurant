# Generated by Django 3.0.2 on 2022-07-21 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=200)),
                ('address', models.CharField(default='', max_length=200)),
                ('image', models.FileField(default='default.jpg', upload_to='static/images/customer')),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.DeleteModel(
            name='Billboard',
        ),
    ]
