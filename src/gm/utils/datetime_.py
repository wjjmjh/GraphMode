import datetime

chars = ["-", " ", ":"]


def now(precision=False):
    got = str(datetime.datetime.now())
    for it in chars:
        got = got.replace(it, "_")
    if precision:
        return got
    return "_".join(got.split("_")[:3])
