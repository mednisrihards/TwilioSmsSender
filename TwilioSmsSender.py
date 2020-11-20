import os
import mysql.connector
from mysql.connector import Error
from twilio.rest import Client
from datetime import datetime
from time import time, sleep

account_sid = os.environ["TWILIO_ACCESS_SID"]
auth_token = os.environ["TWILIO_ACCESS_TOKEN"]
sendersPhoneNr = os.environ["TWILIO_PHONE_NR"]
 
client = Client(account_sid, auth_token) 
minutes_to_sleep = 10

while True:
    now = datetime.now()
    messageSentTime = now.strftime("%Y-%m-%d %H:%M:%S")

    try:
        connection = mysql.connector.connect(host='localhost',
                                            port='8889',
                                            unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock',
                                            database='ClientsDB',
                                            user='root',
                                            password='root')

        sql_select_Query = "select * from Clients"
        sql_message_sent_Query = "UPDATE Clients SET message_sent = '{}' WHERE id = {}"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        
        for row in records:
            # print(row[0])   # Id
            # print(row[2])   # Name
            # print(row[3])   # Last name
            # print(row[4])   # Appointment date
            # print(row[1])   # Phone number
            if row[4] > now :
                cursor.execute(sql_message_sent_Query.format(messageSentTime, row[0]))
                message = client.messages.create( 
                                from_=sendersPhoneNr,  
                                body='{}, You have an apointment on {}'.format(row[2], row[4]),      
                                to=row[1] 
                            )

    except Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if (connection.is_connected()):
            connection.commit()
            connection.close()
            cursor.close()
    
    sleep(minutes_to_sleep * 60)