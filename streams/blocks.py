
from django import forms
from django.forms.utils import ErrorList
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.core.blocks.struct_block import StructBlockValidationError

class TitleBlock(blocks.StructBlock):
    text = blocks.CharBlock(
        required=True, 
        help_text="Text to display",
    )

    class Meta:
        template = "streams/title_block.html"
        icon = "edit"
        label = "Title"
        help_text = "Centered text to display on page"


class LinkValue(blocks.StructValue):
    """Additional logic for our links"""
   
    def url(self) -> str:
        internal_page = self.get("internal_page")
        external_link = self.get("external_link")
        if internal_page:
            return internal_page.url
        elif external_link:
            return external_link
        return ""


class Link(blocks.StructBlock):
    link_text = blocks.CharBlock(
        max_length=50, 
        default='More details'
    )
    internal_page = blocks.PageChooserBlock(
        required=False,
    )
    external_link = blocks.URLBlock(
        required=False
    )

    class Meta:
        value_class = LinkValue

    def clean(self, value):
        internal_page = value.get("internal_page")
        external_link = value.get("external_link")
        errors = {}
        if internal_page and external_link:
            errors["internal_page"] = ErrorList(["Both of these fields cannot be filled. Please select or enter only one option."])
            errors["external_link"] = ErrorList(["Both of these fields cannot be filled. Please select or enter only one option."])
        elif not internal_page and not external_link:
            errors["internal_page"] = ErrorList(["Please select a page or enter a URL for one of these options."])
            errors["external_link"] = ErrorList(["Please select a page or enter a URL for one of these options."])

        if errors:
            raise StructBlockValidationError(errors)

        return super().clean(value)   


class Card(blocks.StructBlock):
    title = blocks.CharBlock(
        max_length=100,
        help_text='Bold title text for this card. Max length 100',
    )
    text = blocks.TextBlock(
        max_length=255, 
        help_text="Optional text for this card. Max length 255", 
        required=False
    )
    image = ImageChooserBlock(
        help_text="Image for this card cropped 570 x 370px",
    )
    link = Link(help_text='Enter a link or select a page to link to')


class CardsBlock(blocks.StructBlock):
    cards = blocks.ListBlock(
      Card(),
    )

    class Meta:
        template = "streams/cards_block.html"
        icon = "image"
        label = "Standard cards"

class RadioSelectBlock(blocks.ChoiceBlock):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.field.widget = forms.RadioSelect(
            choices = self.field.widget.choices,
        )
class ImageAndTextBlock(blocks.StructBlock):
    image = ImageChooserBlock(help_text='Image cropped to 786 x 552px')
    image_alignment = RadioSelectBlock(
        choices=(
            ('left', 'Left image'),
            ('right', 'Right image'),
        ), 
        default='left',
        help_text='Image alignment left or right'   
    )
    title = blocks.CharBlock(max_length=60, help_text='Max length of 60 chars')
    text = blocks.CharBlock(max_length=140, help_text='Max length of 140 chars', required=False)
    link = Link()

    class Meta:
        template = "streams/image_and_text_block.html"
        icon = "image"
        label = "Image & text"


class CallToActionBlock(blocks.StructBlock):
    
    title = blocks.CharBlock(
        max_length=200,
        help_text='Max length 200',
    )
    link = Link()

    class Meta:
        template = "streams/call_to_action_block.html"
        icon = "plus"
        label = "Call to action"


class PricingTableBlock(TableBlock):
    """Pricing Table Block"""

    class Meta:
        template = "streams/pricing_table_block.html"
        label = "Pricing Table"
        icon = "table"
        help_text = "Pricing tables always have 4 columns"