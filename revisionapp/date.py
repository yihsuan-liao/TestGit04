from datetime import datetime



def test_date():
    x = datetime.now()

    print(x.year)
    print(x.strftime("%A")) #%A is used to print the day of the week
    print(x)

    #Assign date
    x2 = datetime(2002, 9, 5)
    print(x2.strftime("%A %d %b %Y"))

    #Date length
    print(x2 - x)

def test_range():
    data = range(10)
    for n in data:
        print(n)
    print('\n')

    data2 = range(110,115)
    for n in data2:
        print(n)
    print('\n')

    data3 = range(1100, 1125, 5) #increment by 5(Jump by 5)
    for n in data3:
        print(n)

def helloworld():
    print("hello world")
    print('\n') #this is for spacing
    print('hi')


def run():
    #test_date()
    #test_range()
    helloworld()

