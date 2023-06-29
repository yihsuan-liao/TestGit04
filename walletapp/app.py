def sum1(num):
    sum = 0
    #[1, 2, 3, 4 ... 9]
    for x in range(1, num+1):
        sum += x
    return sum

def sum2(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return num + sum2(num - 1)
    # 5 + 4 + 3 + 2 + 1
def run():
    print(sum2(5))

def factorial(num):
    if num == 0:
        return 1
    elif num == 1:
        return 1
    else:
        return num * factorial(num - 1)
    # 5 + 4 + 3 + 2 + 1
def run():
    print(factorial(5))

    score1 = 87
    score2 = 45
    score3 = 61
    average = (score1+score2+score3)/3

    mylist = [3, 7, 6, 9, 8, 3]
