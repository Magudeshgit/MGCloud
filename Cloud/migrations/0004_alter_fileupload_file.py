# Generated by Django 4.2.1 on 2023-05-24 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cloud', '0003_alter_fileupload_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='file',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
