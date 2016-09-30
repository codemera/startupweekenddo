from django.template.defaulttags import register
from django import template


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.simple_tag(takes_context=True)
def social_links(context, extra_class=None):
    template_name = 'widgets/social-links.html'

    context = {
        'extra_class': extra_class,
    }
    return template.loader.get_template(template_name).render(template.Context(context))
