'''

class Var:
		...


t = Var(10)


graph = Graph()

impl1 = Implication(
	('xtsgnd', (t, s, g, n, d)),
	('xtsgnd', (t + 1, s, g, n, d))
)

def impl1(*args, **kwargs):
	[t, s, g, n, d] = args
	return Implication(
		('xtsgnd', (t, s, g, n, d)),
		('xtsgnd', (t + 1, s, g, n, d))
	)


def impl(t, s, g, n, d):
	if (True):
		return Implication(
			('xtsgnd', (t, s, g, n, d)),
			('xtsgnd', (t + 1, s, g, n, d))
		)
	else:
		return None

or()



'''

import copy

class OverloadOperators:
	"""docstring for OverloadOperators"""
	def __init__(self):
		self.operations = []

	def deepcopy(self):
		return copy.deepcopy(self)

	def gen_op(self, op, num):
		new_obj = self.deepcopy()
		new_obj.operations.append((op, num))
		return new_obj

	def __add__(self, num):
		return self.gen_op('+', num)

	def __sub__(self, num):
		return self.gen_op('-', num)

	def __mul__(self, num):
		return self.gen_op('*', num)

	def __pow__(self, num):
		return self.gen_op('^', num)

	def __mod__(self, num):
		return self.gen_op('%', num)

	def __truediv__(self, num):
		return self.gen_op('/', num)



class MVar(OverloadOperators):
	"""docstring for Var"""
	def __init__(self, var_id, num_range):
		OverloadOperators.__init__(self)
		self.num_range = num_range
		self.var_id = var_id
		self.type = 'state'

	def extend_list(self):
		new_obj = self.deepcopy()
		new_obj.type = 'extend-list'
		return new_obj

	def extend_state(self):
		new_obj = self.deepcopy()
		new_obj.type = 'extend-state'
		return new_obj


class CVar:
	"""docstring for CompleteVar"""
	def __init__(self, var_id, m_vars):
		self.var_id = var_id
		self.m_vars = m_vars

class BoolOpCVar:
	"""docstring for BoolOpCVar"""
	def __init__(self, op_type, var_list):
		self.op_type = op_type
		self.var_list = var_list


class Implication:
	""" a => b """
	def __init__(self, a, b, constraint_function):
		self.a = a
		self.b = b
		self.constraint_function = constraint_function


t = MVar('t', [1, 20])
s = MVar('s', [1, 20])
g = MVar('g', [1, 20])
n = MVar('n', [1, 4])
_ = MVar('_', None)

xtsgn = lambda t, s, g, n: CVar('xtsgn', (t, s, g, n))


p = BoolOpCVar('and', [xtsgn(t, s.extend_list(), g, n), xtsgn(t, s, g, n + 1)])


i = Implication(xtsgn(t, s, g, n), p, lambda curr_vars: True)




