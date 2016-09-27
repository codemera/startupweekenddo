from django.template.defaulttags import register

@register.inclusion_tag('includes/mailchimp-form.html', takes_context=True)
def mailchimp_form(context, form_class='form-inline', labels=False, dropdowns=False):

    return {
        'form_class': form_class,
        'labels': labels,
        'dropdowns': dropdowns,
    }
