# Generated by Django 4.2.7 on 2023-12-21 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rename_user_vote_profile_alter_vote_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.question'),
        ),
    ]