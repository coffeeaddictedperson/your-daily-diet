from django.utils.translation import gettext

LABELS = {
    'name': gettext('Meal type'),
    'description': gettext('Description'),
}

WARNINGS = {
    'name': {
        'max_length': "This meal's type is too long."
    }
}