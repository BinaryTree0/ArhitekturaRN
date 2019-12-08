from django.core.validators import RegexValidator

alpha = RegexValidator(r'^[a-zA-Z][a-zA-Z ]+$', 'Only letters and spaces are allowed in the Location Name.')
