
def parse_input(text):
    temp = text.split(",")
    date1 = temp[0].lstrip().strip()
    date2 = temp[1].lstrip().strip()

    date1 = date1.split()
    date2 = date2.split()
    date1 = list(map(int, date1))
    date2 = list(map(int, date2))
    return date1,date2

def total_days_since1900(date):
    # 31/12/1899
    # 00/01/1900

    # parse date
    d,m,y = date
    y -= 1900

    # day
    num_of_days = 0
    num_of_days += d

    # month
    # without consider leap year
    monthDays = [31, 28, 31, 30, 31, 30,
                 31, 31, 30, 31, 30, 31]
    for i in range(m-1):
        num_of_days += monthDays[i]

    # year
    def isleap(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    num_of_days += 365*y
    for i in range(1900,1901+y,1):
        if isleap(i):
            num_of_days += 1

    return num_of_days

def calculate_difference(date1,date2):
    # avoid compare directly - complex logic - day higher, month lower, year lower
    # input range of dates from 1900 to 2010
    total_day1 = total_days_since1900(date1)
    total_day2 = total_days_since1900(date2)


    return abs(total_day1-total_day2)

def process(daytext):
    # date1,date2 = [d,m,y],[d,m,y]
    date1, date2 = parse_input(daytext)
    diff = calculate_difference(date1, date2)
    print(diff, 'days')

if __name__ == '__main__':
    daytext = "01 12 1990, 20 02 2000"
    daytext = "20 03 2000, 20 02 2000"
    process(daytext)

'''
why choose this code challenge?
Simply pick the first one!

why you chose the code you chose?
Python 3 
- using it for 6 academic years
- high-level programming - data structures and algorithms        

'''