import random

#Different probabilities and Time-in Time-out Threshold
def my_scenario():
    # scenario_a = 15%
    # scenario_b = 25%
    # scenario_c = 40%
    # scenario_d = 30%

    condition = random.randint(1,20) #random any number from 1-20

    if condition in [1,2,3]:
        return 'a'
    elif condition in [4,5,6,7,8]:
        return 'b'
    elif condition in [9,10,11,12,13,14,15,16]:
        return 'c'
    else:
        return 'd'

def random_with_prob():
    #generate result 10,000 time and count
    count_a = 0
    count_b = 0
    count_c = 0
    count_d = 0

    for x in range(0,10000):
        result = my_scenario()
        if result == 'a':
            count_a += 1
        elif result == 'b':
            count_b += 1
        elif result == 'c':
            count_c += 1
        else:
            count_d += 1

    print('a: ' + str(count_a))
    print('b: ' + str(count_b))
    print('c: ' + str(count_c))
    print('d: ' + str(count_d))

def working_hour(time_in, time_out):
    #  Format xx:xx
    #1 Time-in cut-off 15-minute after
    #2 Time-out cut-off 15-minute before
    #3 Error if time-out before or equal time-in

    in_hour = int(time_in[0:2])
    in_minute = int(time_in[3:5])

    # Take in 2 index 0 and exclude 2
    # Take in index 3 and 4,exclude 5

    if in_minute <= 15:
        in_minute = 15
    elif in_minute <= 30:
        in_minute = 30
    elif in_minute <= 45:
        in_minute = 45
    else:
        in_minute = 0
        in_hour += 1

    print(in_hour)
    print(in_minute)

    out_hour = int(time_out[0:2]) #Take value 0 and 1; exclude 2
    out_minute = int(time_out[3:5])
    if out_minute <= 15:
        out_minute = 0
    elif out_minute <= 30:
        out_minute = 15
    elif out_minute <= 45:
        out_minute = 30
    else:
        out_minute = 45

    print(out_hour)
    print(out_minute)

    duration_minute = ((out_hour * 60) + out_minute) - ((in_hour * 60) + in_minute)
    #60 as in minutes

    if duration_minute <= 0:
        return 'Error!!'

    str_hour = str(duration_minute // 60) + ' hour(s)'
    if duration_minute < 60:
        str_hour = ''

    str_minute = str(duration_minute - (duration_minute // 60)*60) + ' minute(s)'
    if duration_minute - (duration_minute // 60) == 0:
        str_minute = ''

    return str_hour + ' ' + str_minute

def timein_timeout():
    print(working_hour('09:55','17:46'))

    #1 is index 0, 7 is index 1; ":" is index 3.

#Range ane Date

from datetime import datetime

def test_date():
    x = datetime.now() #datetime is a function, you import it on top. To get real datetime from computer

    print(x.year)
    print(x.strftime("%A")) #%A is used to print the day of the week
    print(x)

    #Assign date
    x2 = datetime(2023, 8, 25)
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
    print('\n') #create a big space before the next line

    data3 = range(1100, 1125, 5) #increment by 5(Jump by 5)
    for n in data3:
        print(n)



def run():
    #timein_timeout()
    #random_with_prob()
    #test_date()
    test_range()





# See PyCharm help at https://www.jetbrains.com/help/pycharm/