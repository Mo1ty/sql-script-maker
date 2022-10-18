import random
import string


def email_generator(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


def number_generator(length):
    return ''.join(random.choice(string.digits) for _ in range(length))
