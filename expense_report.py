from expense_data import ExpenseData
from gsa_rate import GsaRate

class ExpenseReport():
	def __init__(self, csv_file, state, city=None):
		self.csv_file = csv_file
		self.state = state
		if city is None:
			self.city = "Standard Rate"
		else:
			self.city = city
