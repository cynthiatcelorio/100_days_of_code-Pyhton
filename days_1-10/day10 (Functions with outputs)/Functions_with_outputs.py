def format_name(f_name, l_name):
    f_name = f_name.title()
    l_name = l_name.title()
    return f"{f_name} {l_name}"

print(format_name("CynTHIa", "TORReS"))


# Return days in month 
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    isLeap = is_leap(year)
    if isLeap:
        month_days[1] = 29
    return month_days[month - 1]  


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

# Doctrings (Video 102)