import requests
from datetime import datetime
from config import api_key

class GsaRate():
	def __init__(self, state):
		self._host = 'https://api.gsa.gov/travel/perdiem/v2/rates/'
		self._x_api_key = api_key
		self._year = datetime.now().year
		self.state = state
		self.rates_by_city = {}

		self.get_per_diem_rates()

	def get_per_diem_rates(self):
		url = f'{self._host}/state/{self.state}/year/{self._year}'
		headers = {
			'X-API-Key': self._x_api_key,
			'Content-Type': 'application/json'
		}
		
		r = requests.get(url, headers=headers)
		try:
			rates = r.json()['rates'][0]['rate']
			for rate in rates:
				if rate['city'] not in self.rates_by_city:
					self.rates_by_city[rate['city']] = rate['meals']
			r.close()
		except IndexError:
			print(f'No GSA data for {self.state}')
			r.close()
