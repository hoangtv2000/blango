from django.contrib.auth import get_user_model
from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe
from django.utils.html import format_html


user_model = get_user_model()
register = template.Library()



@register.filter(name="author_details") # Further being used in index.html as author_details!
def author_details(author, current_user=None):
    """
    + Using mark_safe means that Django will not escape the text. If you have user-generated text, this could be way to inject malicious code into the website.
    + Using format_html will automatically escape the text. Malicious code would not be executed.
    + A simple f-string provides no protection from malicious code.
    """
    if not isinstance(author, user_model):
        # return empty string as safe default
        return ""
    
    if author == current_user:
      return format_html("<strong>me</strong>")

    if author.first_name and author.last_name:
        name = f"{author.first_name} {author.last_name}"
    else:
        name = f"{author.username}"

    if author.email:
        prefix = format_html('<a href="mailto:{}">', author.email)
        suffix = format_html("</a>")
    else:
        prefix = ""
        suffix = ""

    return format_html('{}{}{}', prefix, name, suffix)
