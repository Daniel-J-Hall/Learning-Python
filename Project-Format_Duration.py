def format_duration(seconds):
    Seconds = int(seconds)

    Minutes = int(Seconds / 60)
    m_Seconds = int(Seconds % 60)

    Hours = int(Minutes / 60)
    m_Minutes = int(Minutes % 60)

    Days = int(Hours / 24)
    m_Hours = int(Hours % 24)

    Years = int(Days / 365)
    m_Days = int(Days % 365)

    sec = "second" if m_Seconds == 1 else "seconds"
    min = "minute" if m_Minutes == 1 else "minutes"
    hou = "hour" if m_Hours == 1 else "hours"
    day = "day" if m_Days == 1 else "days"
    yea = "year" if Years == 1 else "years"

    temp = {}

    if Years >= 1:
        temp[yea] = Years
    if m_Days >= 1:
        temp[day] = m_Days
    if m_Hours >= 1:
        temp[hou] = m_Hours
    if m_Minutes >= 1:
        temp[min] = m_Minutes
    if m_Seconds >= 1:
        temp[sec] = m_Seconds

    if len(temp) == 0:
        return "now"
    if len(temp) == 1:
        return "{} {}".format(*temp.values(), *temp.keys())
    if len(temp) == 2:
        return "{0} {2} and {1} {3}".format(*temp.values(), *temp.keys())
    if len(temp) == 3:
        return "{0} {3}, {1} {4} and {2} {5}".format(*temp.values(), *temp.keys())
    if len(temp) == 4:
        return "{0} {4}, {1} {5}, {2} {6} and {3} {7}".format(*temp.values(), *temp.keys())
    if len(temp) == 5:
        return "{0} {5}, {1} {6}, {2} {7}, {3} {8} and {4} {9}".format(*temp.values(), *temp.keys())


format_duration(1)#, "1 second")
format_duration(62)  # , "1 minute and 2 seconds")
format_duration(120)#, "2 minutes")
format_duration(3600)#, "1 hour")
format_duration(1307758473.484 )