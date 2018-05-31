# -*- coding: utf-8 -*-
"""Main Test module"""

from translator import Translator


def base(data):
    print("\n--- BASE METHOD ---")
    t = Translator()
    for item in data:
        result = t.translate(item)
        print("{}\t==>>\t{}".format(item, result))


def context(data):
    print("\n --- USING CONTEXT ---")
    for item in data:
        with Translator() as tran:
            result = tran.translate(item)
            print("{} ==> {}".format(item, result))


if __name__ == "__main__":
    BASE_DATA = (
        "123.545/6464]54[]54",
        "320two23",
        ""
    )
    CONTEXT_DATA = (
        221901234554,
        32434343,
        0,
        32132432
    )

    base(BASE_DATA)
    context(CONTEXT_DATA)
