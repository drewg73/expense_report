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
		self.expense_data = ExpenseData(self.csv_file)
		self.gsa_rates = GsaRate(self.state).rates_by_city

	def get_gsa_rate(self):
		if self.city not in self.gsa_rates:
			return self.gsa_rates['Standard Rate']
		else:
			return self.gsa_rates[self.city]

	def get_total_per_diem(self):
		trip_duration = len(self.expense_data.expenses_by_day)
		per_diem = self.get_gsa_rate()
		return int(per_diem) * trip_duration
	
	def print_report(self):
		per_diem = self.get_gsa_rate()
		total_per_diem = self.get_total_per_diem()
		total_expenses = self.expense_data.expenses_total
		net_gain = total_per_diem - total_expenses
		print('Expense Report')
		print(f'Per Diem Rate: ${per_diem:.2f}')
		print(f'Total Per Diem: ${total_per_diem:.2f}')
		print(f'Total Expenses: ${total_expenses:.2f}')
		print(f'Net Gain/Loss: ${net_gain:.2f}')