def oddsum():
    odd_sum = 0

    for num in range(1, 11):
        if num % 2 != 0:
            odd_sum += num

    print('Sum of odd numbers: ', odd_sum)

def primesum():
    prime_sum = 0

    for num in range(1, 11):
        if num > 1:
            for i in range(2, num):
                if(num % i) == 0:
                    break
            else:
                prime_sum += num

    non_prime_sum = (10 * (10 + 1)) // 2 - prime_sum
    print('Sum of non-prime number: ', non_prime_sum)





def run():
    #oddsum()
    primesum()
