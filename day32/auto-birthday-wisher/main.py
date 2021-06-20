import datetime as dt
import pandas
import random
import smtplib

BIRTHDAY_DF = pandas.read_csv('birthdays.csv')
LETTER_PLACEHOLDER = "[NAME]"
SENDER_EMAIL = ""

now = dt.datetime.now()
current_month = now.month
current_day = now.day


def check_birthdays():
    for i, row in BIRTHDAY_DF.iterrows():
        if row['month'] == current_month and row['day'] == current_day:
            name = row['name']
            email = row['email']
            send_email(name, email)


def generate_template(name):
    number = random.randint(1, 3)
    with open(f'letter_templates/letter_{number}.txt') as template:
        template_str = template.read()
        final_template = template_str.replace(LETTER_PLACEHOLDER, name)
        return final_template


def send_email(name, email):
    message = generate_template(name)

    if len(message) > 0 and len(name) > 0:
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user='', password='')
            connection.sendmail(
                from_addr=SENDER_EMAIL,
                to_addrs=email,
                msg=f"Subject: Happy Birthday!\n\n{message}"
            )


check_birthdays()
