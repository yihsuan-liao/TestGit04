def working_hour(time_in, time_out, lunch_start, lunch_end):
    # Format xx:xx
    # 1 Time-in cut-off 15-minute after
    # 2 Time-out cut-off 15-minute before
    # 3 Error if time-out before or equal time-in

    # Parse time_in, time_out, lunch_start, and lunch_end
    in_hour = int(time_in[0:2])
    in_minute = int(time_in[3:5])

    lunch_start_hour = int(lunch_start[0:2])
    lunch_start_minute = int(lunch_start[3:5])

    lunch_end_hour = int(lunch_end[0:2])
    lunch_end_minute = int(lunch_end[3:5])

    out_hour = int(time_out[0:2])
    out_minute = int(time_out[3:5])

    # Check if there's a lunch break
    if in_hour * 60 + in_minute < lunch_start_hour * 60 + lunch_start_minute:
        # Time-in is before the lunch break
        duration_minute = (out_hour * 60 + out_minute) - (in_hour * 60 + in_minute)
    elif in_hour * 60 + in_minute >= lunch_end_hour * 60 + lunch_end_minute:
        # Time-in is after the lunch break
        duration_minute = (out_hour * 60 + out_minute) - (in_hour * 60 + in_minute)
    else:
        # Time-in and Time-out overlap with lunch break
        before_lunch_duration = (lunch_start_hour * 60 + lunch_start_minute) - (in_hour * 60 + in_minute)
        after_lunch_duration = (out_hour * 60 + out_minute) - (lunch_end_hour * 60 + lunch_end_minute)
        duration_minute = before_lunch_duration + after_lunch_duration

    # Handle errors and format the duration
    if duration_minute <= 0:
        return 'Error!!'

    str_hour = str(duration_minute // 60) + ' hour(s)'
    if duration_minute < 60:
        str_hour = ''

    str_minute = str(duration_minute - (duration_minute // 60) * 60) + ' minute(s)'
    if duration_minute - (duration_minute // 60) == 0:
        str_minute = ''

    return str_hour + ' ' + str_minute

def timein_timeout():
    # Example usage with a lunch break from 12:00 to 13:00
    print(working_hour('09:55', '17:46', '12:00', '13:00'))



