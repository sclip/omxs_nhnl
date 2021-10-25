from src import new_peaks
from typing import List
import yahooquery as yq


def get_new_lows(stocks: List[str], period: str) -> int:
	"""Get the new low count for the selected stocks in the selected period

	Args:
		stocks (List[str]): The list of stocks to analyze
		period (str): The period to analyze
	"""

	new_lows = 0

	for stock in stocks:
		ticker = yq.Ticker(stock)
		if new_peaks.on_new_low(ticker.history(period=period, interval="1d")):
			new_lows += 1

	return new_lows


def get_new_highs(stocks: List[str], period: str) -> int:
	"""Get the new high count for the selected stocks in the selected period

	Args:
		stocks (List[str]): The list of stocks to analyze
		period (str): The period to analyze
	"""

	new_lows = 0

	for stock in stocks:
		ticker = yq.Ticker(stock)
		if new_peaks.on_new_high(ticker.history(period=period, interval="1d")):
			new_lows += 1

	return new_lows


def get_nh_nl(stocks: List[str], period: str) -> int:
	""" Gets the NH - NL for the selected list of stocks, for the selected period"""
	return get_new_highs(stocks, period) - get_new_lows(stocks, period)
