from src import listings, defines, nh_nl, bot


def main(event, context):
    event = event
    context = context
    listings.load()
    defines.load()
    data = {
        "OMXS30 NH-NL 1M": nh_nl.get_nh_nl(listings.lists["OMXS30"], "1mo"),
        "OMXS30 NH-NL 3M": nh_nl.get_nh_nl(listings.lists["OMXS30"], "60mo"),
        "OMXS30 NH-NL 1Y": nh_nl.get_nh_nl(listings.lists["OMXS30"], "1y")
    }

    text = "".join([f"{x}   : {data[x]} \n" for x in data])
    bot.init(text)


if __name__ == '__main__':
    main(None, None)
