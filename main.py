from expense_report import ExpenseReport

def main():
	expense_report = ExpenseReport('activity.csv', 'VA')
	expense_report.print_report()

if __name__ == "__main__":
	main()