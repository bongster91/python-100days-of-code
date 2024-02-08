import smtplib
from datetime import datetime
import pandas
import random

my_email = "testing@gmail.com"
password = ""

# with smtplib.SMTP('smtp.gmail.com') as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email, 
#         to_addrs="park_bongg@yahoo.com", 
#         msg='Subject:Hello world\n\nThis is the body of my email'
#     )

# now = dt.datetime.now()
# weekday = now.weekday()
# if weekday == 0:
#     with open('quotes.txt') as quote_file:
#         all_quotes = quote_file.readlines()
#         quote = random.choice(all_quotes)
    
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(from_addr=my_email, password=password)
#         connection.sendmail(
#             from_addr=my_email,
#             to_addrs='1232@yahoo.com',
#             msg=f"Subject: quote\n\n{quote}"
#         )
        
today = (datetime.now().month, datetime.now().day)
data = pandas.read_csv('birthdays.csv')
birthdays_dict = {(data_row.month, data_row.day):data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person['name'])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person['email'],
            msg=f"Subject: Hello\n\n{contents}"
        )