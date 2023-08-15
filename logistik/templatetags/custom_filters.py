from django import template

register = template.Library()

@register.filter
def calculate_counter(index, page_number):
    items_per_page = 15  # Change this to your items per page value
    return (index - 1) + (page_number - 1) * items_per_page + 1
