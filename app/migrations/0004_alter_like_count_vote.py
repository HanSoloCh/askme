# Generated by Django 4.2.7 on 2023-12-21 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_question_dislike_alter_question_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='count',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_type', models.CharField(choices=[('like', 'Like'), ('dislike', 'Dislike')], max_length=7)),
                ('answer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.answer')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.profile')),
            ],
            options={
                'unique_together': {('user', 'question', 'answer')},
            },
        ),
    ]
