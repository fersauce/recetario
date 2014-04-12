from django.contrib.auth.hashers import PBKDF2PasswordHasher

__author__ = 'sauce'


class SSHasher(PBKDF2PasswordHasher):
    """
    Es una subclase heredada de PBKDF2PasswordHasher para la
    encriptacion del password de Usuario
    """

    iterations = PBKDF2PasswordHasher.iterations*100