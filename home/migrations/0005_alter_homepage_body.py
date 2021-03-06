# Generated by Django 3.2.11 on 2022-01-17 20:33

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_homepage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('title', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Text to display', required=True))])), ('cards', wagtail.core.blocks.StructBlock([('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Bold title text for this card. Max length 100', max_length=100)), ('text', wagtail.core.blocks.TextBlock(help_text='Optional text for this card. Max length 255', max_length=255, required=False))])))]))], blank=True, null=True),
        ),
    ]
