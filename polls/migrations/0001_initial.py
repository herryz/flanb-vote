# Generated by Django 2.0.6 on 2018-07-06 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(verbose_name='user_id')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('status', models.SmallIntegerField(choices=[(0, 'enabled'), (1, 'disabled')], default=0, verbose_name='status')),
                ('detail', models.TextField(blank=True, verbose_name='detail')),
                ('public', models.SmallIntegerField(choices=[(0, 'True'), (1, 'False')], default=0, verbose_name='public')),
                ('multi', models.SmallIntegerField(choices=[(0, 'True'), (1, 'False')], default=0, verbose_name='multi')),
                ('max', models.IntegerField(default=1, verbose_name='max')),
                ('min', models.IntegerField(default=1, verbose_name='min')),
                ('start_dt', models.DateTimeField(verbose_name='start_dt')),
                ('end_dt', models.DateTimeField(verbose_name='start_dt')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='start_dt')),
                ('update_dt', models.DateTimeField(auto_now=True, verbose_name='end_dt')),
            ],
            options={
                'verbose_name': 'vote',
                'verbose_name_plural': 'votes',
                'db_table': 'flanb_vote',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='VoteOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_id', models.IntegerField(verbose_name='vote_id')),
                ('option_name', models.CharField(max_length=100, verbose_name='option_name')),
                ('count', models.IntegerField(default=0, verbose_name='count')),
            ],
            options={
                'verbose_name': 'vote_option',
                'verbose_name_plural': 'vote_options',
                'db_table': 'flanb_vote_option',
                'ordering': ('id',),
            },
        ),
    ]
