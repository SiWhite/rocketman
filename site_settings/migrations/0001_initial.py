# Generated by Django 3.2.11 on 2022-01-21 00:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(blank=True, help_text='FB url', null=True)),
                ('twitter', models.URLField(blank=True, help_text='TW url', null=True)),
                ('youtube', models.URLField(blank=True, help_text='YT url', null=True)),
                ('instagram', models.URLField(blank=True, help_text='IG url', null=True)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
