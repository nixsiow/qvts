import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

# ===================================
#  Password validators rules include:

#     At least 12 characters in length;
#     At least 1 digit;
#     At least 1 uppercase character;
#     At least 1 lowercase character;
#     At least 1 special character;
# ===================================


class NumberValidator:
    """
    Validate whether the password contains at least 1 digit.
    """

    def validate(self, password, user=None):
        if not re.findall(r"\d", password):
            raise ValidationError(
                _("The password must contain at least 1 digit, 0-9."),
                code="password_no_number",
            )

    def get_help_text(self):
        return _("Your password must contain at least 1 digit, 0-9.")


class UppercaseValidator:
    """
    Validate whether the password contains at least 1 uppercase letter.
    """

    def validate(self, password, user=None):
        if not re.findall("[A-Z]", password):
            raise ValidationError(
                _("The password must contain at least 1 uppercase letter, A-Z."),
                code="password_no_upper",
            )

    def get_help_text(self):
        return _("Your password must contain at least 1 uppercase letter, A-Z.")


class LowercaseValidator:
    """
    Validate whether the password contains at least 1 lowercase letter.
    """

    def validate(self, password, user=None):
        if not re.findall("[a-z]", password):
            raise ValidationError(
                _("The password must contain at least 1 lowercase letter, a-z."),
                code="password_no_lower",
            )

    def get_help_text(self):
        return _("Your password must contain at least 1 lowercase letter, a-z.")


class SymbolValidator:
    """
    Validate whether the password contains at least 1 special character.
    """

    def validate(self, password, user=None):
        if not re.findall("[!@#$%^&*]", password):
            raise ValidationError(
                _("The password must contain at least 1 special character: " + "!@#$%^&*"),
                code="password_no_symbol",
            )

    def get_help_text(self):
        return _("Your password must contain at least 1 special character: " + "!@#$%^&*")
