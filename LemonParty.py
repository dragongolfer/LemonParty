#Lemonade Stand
import system
import random

class Ingredient:
	def __init__(self, item_name, item_stock, item_cost):
		self.name = item_name
		self.stock = item_stock
		self.cost = item_cost

	def get_stock(self):
		return self.stock

	def increase_stock(self, item_stock):
		self.stock += item_stock

	def decrease_stock(self, item_stock):
		self.stock -= item_stock

	def get_name(self):
		return self.name

	def set_item_name(self, item_name):
		self.name 


class Player:
	def __init__(self, player_name, starting_money, todays_price):
		self.name = player_name
		self.starting_money = 10
		self.todays_price = 5
		self.temperature = random.randrange(40,100)
		self.day = 0#increment this to keep track of turns
		self.amount_sold = 0
		self.current_weather = random.choice("Tundra", "Coronasphere", "Tsunami", "Cyclonic")

	def set_name(self, player_name):
		self.name = 