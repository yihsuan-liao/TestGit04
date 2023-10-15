import math
import re
def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def q01():
    distance = euclidean_distance(1,1,5,4)
    print(distance)

def q02(course_code):
    regex = r'\b[A-Za-z][A-Za-z][A-Za-z]+[0-9][0-9][0-9][0-9]\b'

    if(re.fullmatch(regex, course_code)):
        print("true")
    else:
        print("false")

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

def q03():
    print(working_hour('09:55','17:46'))

def quick_sorting(list):
    if len(list) <= 1:
        return list

    pivot = list[-1]
    left = []
    right = []

    for x in list[:-1]:
        if x < pivot:
            left.append(x)
        else:
            right.append(x)

    return quick_sorting(left) + [pivot] + quick_sorting(right)


def q04():
    my_list = [3, 6, 8, 10, 1, 2, 1, 10, 12]
    sorted_list = quick_sorting(my_list)
    print(sorted_list)

def run():
    #q01()
    #q02(course_code="DDD1111")
    #q03()
    q04()