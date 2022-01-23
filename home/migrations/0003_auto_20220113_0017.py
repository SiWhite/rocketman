# Generated by Django 3.2.11 on 2022-01-13 00:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
        ('wagtailimages', '0023_add_choose_permissions'),
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='banner_background_image',
            field=models.ForeignKey(help_text='Banner background image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='button',
            field=models.ForeignKey(blank=True, help_text='Select an optional page to link to', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='button_text',
            field=models.CharField(default='Read More', help_text='Button text', max_length=50),
        ),
        migrations.AddField(
            model_name='homepage',
            name='lead_text',
            field=models.CharField(blank=True, help_text='Subheading text under banner title', max_length=140),
        ),
    ]
