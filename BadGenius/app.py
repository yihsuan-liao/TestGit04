swapping = {
        'aa': 'A','ab': 'B','ac': 'C',
        'ad': 'D','ba': 'E','bb': 'F',
        'bc': 'G','bd': 'H','ca': 'I',
        'cb': 'J','cc': 'K','cd': 'M',
        'da': 'L','db': 'N','dc': 'O',
        'dd': 'P'
        }

def reduce_char(input):
    reduced_answer = ""
    for i in range(0, len(input), 2):
        pair = input[i:i + 2]
        if pair in swapping:
            reduced_answer += swapping[pair]

    return reduced_answer

swapping_back = {
    'A': 'aa', 'B': 'ab', 'C': 'ac', 'D': 'ad',
    'E': 'ba', 'F': 'bb', 'G': 'bc', 'H': 'bd',
    'I': 'ca', 'J': 'cb', 'K': 'cc', 'L': 'cd',
    'M': 'da', 'N': 'db', 'O': 'dc', 'P': 'dd'
        }

def convert_char(reduced_answer):
    converted_answer = ''
    for x in reduced_answer:
        if x in swapping_back:
            converted_answer += swapping_back[x]

    return converted_answer

def run():
    answer = "abccdcdccabdbcadbacb"
    reduced_ans = reduce_char(answer)
    converted_ans = convert_char(reduced_ans)

    print("Reduced Text:", reduced_ans)
    print("Converted Text:", converted_ans)


