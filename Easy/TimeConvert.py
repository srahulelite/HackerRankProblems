#
# Given a time in -hour AM/PM format, convert it to military (24-hour) time.
# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Checking for AM, and converting next day to 00
    if(s[-2:] == "AM") and (s[:2] == "12"):
        return "00" + s[2:-2]
    # removing AM
    elif(s[-2:] == "AM"):
        return s[:-2]
    # Checking for PM, and restricting it to go beyond 24:00:00
    elif(s[-2:] == "PM") and (s[:2] == "12"):
        return s[:-2]
    else:
    # add 12 to current time in hours in PM case
        return str(int(s[:2]) + 12) + s[2:-2]


#Driver code
if __name__ == '__main__':
    result = timeConversion("12:10:00PM")
    print(result)
