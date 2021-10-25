import json


lists = {

}


def load(path="res/lists.json") -> None:
	with open(path, "r") as df:
		stocks_list = json.load(df)

	for li in stocks_list:
		lists[li] = stocks_list[li]


if __name__ == '__main__':
	load("../res/lists.json")
