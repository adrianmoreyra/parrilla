from django import template

register = template.Library()

@register.filter(name='multiply')
def multiply(value, arg):
    """Multiplica el valor por el argumento."""
    return value * arg
