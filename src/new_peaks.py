import pandas as pd


def on_new_low(stock_history: pd.DataFrame) -> bool:
	"""
	Returns True if the price for a stock is at the lowest point in a period

	Args:
		stock_history (pd.DataFrame): The stock to analyze

	Returns:
		bool: Returns True/False depending on whether or not the stock is at a period-ATL
	"""

	if stock_history["close"][-1] <= stock_history["close"].min():
		return True

	return False


def on_new_high(stock_history: pd.DataFrame) -> bool:
	"""
	Returns True if the price for a stock is at the highest point in a period

	Args:
		stock_history (pd.DataFrame): The stock to analyze

	Returns:
		bool: Returns True/False depending on whether or not the stock is at a period-ATH
	"""

	if stock_history["close"][-1] >= stock_history["close"].max():
		return True

	return False
