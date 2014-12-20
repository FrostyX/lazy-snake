import random
import string


def make(length=6):
	simple_chars = string.ascii_letters + string.digits
	return ''.join(random.choice(simple_chars) for i in xrange(length))