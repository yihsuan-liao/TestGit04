#Bad Genius Solution, Compression

pair_dict = {
    "aa": "A",
    "ab": "B",
    "ac": "C",
    "ad": "D",

    "ba": "E",
    "bb": "F",
    "bc": "G",
    "bd": "H",

    "ca": "I",
    "cb": "J",
    "cc": "K",
    "cd": "L",

    "da": "M",
    "db": "N",
    "dc": "O",
    "dd": "P",
}

def compress(str):
    result = ''
    for x in range(0,40,2):
        pair = '' + str[x] + str[x+1]
        result += pair_dict[pair]
    return result


pair_dict2 = {
    "A":"aa",
    "B":"ab",
    "C":"ac",
    "D":"ad",

    "E":"ba",
    "F":"bb",
    "G":"bc",
    "H":"bd",

    "I":"ca",
    "J":"cb",
    "K":"cc",
    "L":"cd",

    "M":"da",
    "N":"db",
    "O":"dc",
    "P":"dd",
}


def decompress(str):
    result = ''
    for x in range(0,20):
        pair = '' + str[x]
        result += pair_dict2[pair]
    return result

def compression():
    answers = "acbdacbcbadcbbadcbdbcbbadcadcbcabdcbadcb"
    print(len(answers))
    print("Answer: " + answers)
    code = compress(answers)
    print("Compressed: " + code)
    print("Decompressed: " + decompress(code))


def run():
    compression()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/