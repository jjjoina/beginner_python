import datetime

currdate_input = input()

currdate = datetime.datetime.strptime(currdate_input, "%Y %m %d")
print(currdate.strftime("%m/%d/%Y"))

nextdate = currdate + datetime.timedelta(1)
print(nextdate.strftime("%m/%d/%Y"))
