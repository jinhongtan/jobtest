# Generated by Django 4.0.1 on 2022-01-29 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ResumeSearch', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='job',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ResumeSearch.job'),
        ),
    ]
