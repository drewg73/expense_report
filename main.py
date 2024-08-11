from gsa_rate import GsaRate
from expense_data import ExpenseData

def main():
	expense_report = ExpenseData('activity.csv')

	print(expense_report.start_date, expense_report.end_date)

	for date in expense_report.expenses_by_day:
		print(f'{date}: {expense_report.expenses_by_day[date]:.2f}')

	print(f'Total: {expense_report.expenses_total:.2f}')	

if __name__ == "__main__":
	main()