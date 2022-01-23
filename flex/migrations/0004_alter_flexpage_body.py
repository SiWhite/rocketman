# Generated by Django 3.2.11 on 2022-01-19 23:00

from django.db import migrations
import streams.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0003_alter_flexpage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='body',
            field=wagtail.core.fields.StreamField([('title', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Text to display', required=True))])), ('cards', wagtail.core.blocks.StructBlock([('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Bold title text for this card. Max length 100', max_length=100)), ('text', wagtail.core.blocks.TextBlock(help_text='Optional text for this card. Max length 255', max_length=255, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Image for this card cropped 570 x 370px')), ('link', wagtail.core.blocks.StructBlock([('link_text', wagtail.core.blocks.CharBlock(default='More details', max_length=50)), ('internal_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False))], help_text='Enter a link or select a page to link to'))])))])), ('image_and_text', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='Image cropped to 786 x 552px')), ('image_alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left image'), ('right', 'Right image')], help_text='Image alignment left or right')), ('title', wagtail.core.blocks.CharBlock(help_text='Max length of 60 chars', max_length=60)), ('text', wagtail.core.blocks.CharBlock(help_text='Max length of 140 chars', max_length=140, required=False)), ('link', wagtail.core.blocks.StructBlock([('link_text', wagtail.core.blocks.CharBlock(default='More details', max_length=50)), ('internal_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False))]))])), ('cta', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Max length 200', max_length=200)), ('link', wagtail.core.blocks.StructBlock([('link_text', wagtail.core.blocks.CharBlock(default='More details', max_length=50)), ('internal_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False))]))])), ('testimonial', wagtail.snippets.blocks.SnippetChooserBlock(target_model='testimonials.Testimonial', template='streams/testimonial_block.html')), ('pricing_table', streams.blocks.PricingTableBlock(table_options={'colHeaders': False, 'rowHeaders': True})), ('richtext', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'ol', 'ul'], template='streams/simple_richtext_block.html')), ('large_image', wagtail.images.blocks.ImageChooserBlock(help_text='Image cropped to 1200 x 775px', template='streams/large_image_block.html'))], blank=True, null=True),
        ),
    ]
