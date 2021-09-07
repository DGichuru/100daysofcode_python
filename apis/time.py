import smtplib
import datetime as dt
import random

MY_EMAIL = "dangichuru77@gmail.com"
TO_ADD = "dangichuru54@students.uonbi.ac.ke"
MY_PASSWORD = "11230313009"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 1:
    with open("d:/Python/python/apis/quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)


    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg = f"Subject: Monday Motivation\n\n {quote}"
        )