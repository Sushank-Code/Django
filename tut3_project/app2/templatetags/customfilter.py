from django import template
register = template.Library()

# def myreplace(value , arg):
#     return value.replace(arg,"we are")

# register.filter('iam2weare',myreplace)

# with decorator

@register.filter(name = "iam2weare")
def myreplace(value , arg):
    return value.replace(arg,"we are")