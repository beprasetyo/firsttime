#months

months = ["Januari","Februari","March","April","May","June","July","August","September","October","November","December"]
endings = ["st","nd","rd"]+17*["th"]+["st","nd","rd"]+\
    7*["th"]+["st"]

year = input("Enter year: ")
month = int(input("Enter month: "))
day = int(input("Enter day: "))

month_no = months[month-1]
days = str(day)+endings[day-1]
print("The date you have entered is ",days," ",month_no," ",year)