# Generated by Django 3.2 on 2021-04-11 18:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('order_id', models.IntegerField(default=1)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique ID for this Category.', primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(default='', help_text="Enter the Category's Name", max_length=500)),
                ('type', models.CharField(default='', help_text="Enter the Category's Type", max_length=500)),
            ],
            options={
                'ordering': ['order_id'],
            },
        ),
    ]
