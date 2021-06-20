import datetime as dt
import pandas
import random
import smtplib

BIRTHDAY_DF = pandas.read_csv('birthdays.csv')

now = dt.datetime.now()
current_month = now.month
current_date = now.day

val = BIRTHDAY_DF.values
print(val[0])

#
# for person in list_of_dob['month']:
#     if current_month == list_of_dob['month'][person]:
#         for day in list_of_dob['day']:
#             if current_date = list_of_dob['month'][month]: