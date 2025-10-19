import smtplib
import random
import pandas as pd
import datetime

with open("birthdays.csv") as df:
    df = pd.read_csv(df)
    names = df.name
    years = df.year
    months = df.month
    days = df.day
    emails = df.email

with (open("letter_templates/letter_1.txt") as letter_1 , open("letter_templates/letter_2.txt") as letter_2 ,
                                            open("letter_templates/letter_3.txt") as letter_3):
    letter_1 = letter_1.read()
    letter_2 = letter_2.read()
    letter_3 = letter_3.read()
    all_letter = letter_1, letter_2, letter_3
    random_letter = random.choice(all_letter)

today = datetime.datetime.today()
birthday_day = today.day
birthday_month = today.month

for day in days:
    for month in months:
        if birthday_day == day and birthday_month == month:
            index = df[(df["day"] == day) & (df["month"] == month)].index[0]
            birthday_name = df.at[index,"name"]
            birthday_email = df.at[index,"email"]

random_letter = random_letter.replace("[NAME]", birthday_name)

my_email = "testingcode@gmail.com"
password = "abcd efgh ijkl mnon"

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(my_email, password)
    connection.sendmail(from_addr=my_email,to_addrs= birthday_email,
                        msg=f"Subject:Happy Birthday!\n\n{random_letter}")



