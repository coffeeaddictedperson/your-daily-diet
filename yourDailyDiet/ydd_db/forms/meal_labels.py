from django.utils.translation import gettext

LABELS = {
    'name': gettext('Meal'),
    'description': gettext('Short description'),
    'type': gettext('Better for...'),
    'is_vegetarian': gettext('Vegetarian?')
}

WARNINGS = {
    'name': {
        'max_length': "This meal's name is too long."
    }
}