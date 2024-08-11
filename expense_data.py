import csv, sys
from datetime import datetime 

class ExpenseData():
	def __init__(self, csv_file):
		self.expenses = []
		self.expenses_by_type = {}
		self.expenses_by_day = {}
		self.expenses_total = 0
		self.start_date = None
		self.end_date = None
		self.csv_file = csv_file

		self.generate_expenses()
		self.set_dates()
		self.group_expenses()
		self.total_per_day()
		self.get_total()

	def set_dates(self):
		self.start_date = self.expenses[0].date
		self.end_date = self.expenses[-1].date

	def get_total(self):
		if self.expenses_total == 0:
			for expense in self.expenses:
				self.expenses_total += expense.amount
		else:
			print("Thre is already a total")

	def group_expenses(self):
		for expense in self.expenses:
			if expense.type in self.expenses_by_type.keys():
				self.expenses_by_type[expense.type] += expense.amount
			else:
				self.expenses_by_type[expense.type] = expense.amount

	def total_per_day(self):
		for expense in self.expenses:
			if expense.date in self.expenses_by_day.keys():
				self.expenses_by_day[expense.date] += expense.amount
			else:
				self.expenses_by_day[expense.date] = expense.amount
		
	def generate_expenses(self):
		with open(self.csv_file, newline='') as cf:
			reader = csv.DictReader(cf)
			try:
				for line in reader:
					if float(line['Amount']) > 0:
						self.expenses.insert(0, Expense(datetime.strptime(line['Date'], '%m/%d/%Y'), float(line['Amount']), line['Category']))
				cf.close()
			except csv.Error as err:
				cf.close()
				sys.exit('file {}, line{}: {}'.format(cf, reader.line_num, err))

class Expense():
	def __init__(self, date, amount, type):
		self.date = date
		self.amount = amount
		self.type = type