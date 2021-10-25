import json
import pathlib


defines = {

}


def load() -> None:
	with open(pathlib.Path("res/config.json"), "r") as df:
		stocks_list = json.load(df)

	for li in stocks_list:
		defines[li] = stocks_list[li]
