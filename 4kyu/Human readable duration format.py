def format_duration(seconds):
    if seconds ==  0:
        result = "now"
        
    else:
        
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)
        years, days = divmod(days, 365)

        noun_s = "second" if seconds == 1 else "seconds"
        noun_m = "minute" if minutes == 1 else "minutes"
        noun_h = "hour" if hours == 1 else "hours"
        noun_d = "day" if days == 1 else "days"
        noun_y = "year" if years == 1 else "years"
        result_list = []


        if years:
            result_list.append(f"{years} {noun_y}")
        if days:
            result_list.append(f"{days} {noun_d}")
        if hours:
            result_list.append(f"{hours} {noun_h}")
        if minutes:
            result_list.append(f"{minutes} {noun_m}")
        if seconds:
            result_list.append(f"{seconds} {noun_s}")


        if len(result_list) == 1:
            result = result_list[0]
        elif len(result_list) == 2:
            result = " and ".join(result_list)
        else:
            result = ", ".join(result_list[:-1]) + " and " + result_list[-1]
    return result
