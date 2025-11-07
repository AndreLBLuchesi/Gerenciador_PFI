from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def primeira_palavra(value):
    """Retorna a primeira palavra de uma string."""
    if not isinstance(value, str):
        return value
    words = value.split()
    if words:
        return words[0]
    return ''

@register.filter
def ultima_palavra(value):
    """Retorna a última palavra de uma string."""
    if not isinstance(value, str):
        return value
    words = value.split()
    if words:
        return words[-1]
    return ''

@register.filter
def primeira_ultima_palavra(value):
    return primeira_palavra(value) + ' ' + ultima_palavra(value)

@register.filter
def get_value_index(lista, index):
    print('funcao filter')
    print(lista)
    print(index)
    return lista[index]
