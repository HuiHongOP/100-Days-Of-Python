import smtplib
import datetime as dt
import random
import pandas as pd


data = pd.read_csv('birthdays.csv')
birthday_data = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}

my_email = 'your_own@gmail.com'
password = 'app_connection_pw'


        
today = dt.datetime.now()
today_tuple = (today.month, today.day)

if today_tuple in birthday_data:
    birthday_person  = birthday_data[today_tuple]
    file_path = f'letter_templates/letter_{random.randint(1, 3)}.txt'
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents.replace("['NAME']", birthday_person['name'])
    
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, 
                            to_addrs=birthday_person['email'], 
                            msg=f'Subject:Happy Birthday!\n\n{contents}'
        )
