from JudgerBase import *
from Gcc import *

def create(submit):
	if submit['language'] == 'g++ 4.6':
		return Gcc()
	else:
		return None
