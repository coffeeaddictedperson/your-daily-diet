from django.utils.translation import gettext

MEAL_TYPES = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
    ('S', 'Snack'),
    ('O', 'Other'),
)

MEAL_TYPES_DICT = {
    'B': gettext('Breakfast'),
    'L': gettext('Lunch'),
    'D': gettext('Dinner'),
    'S': gettext('Snack'),
    'O': gettext('Other'),
}