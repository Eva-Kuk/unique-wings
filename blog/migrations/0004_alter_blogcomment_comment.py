# Generated by Django 3.2.7 on 2021-11-14 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blogcomment_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='comment',
            field=models.TextField(max_length=1024, null=True),
        ),
    ]
