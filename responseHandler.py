import os
import mysql.connector
from mysql.connector import Error
from twilio.rest import Client
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from datetime import datetime

account_sid = os.environ["TWILIO_ACCESS_SID"]
auth_token = os.environ["TWILIO_ACCESS_TOKEN"]

client = Client(account_sid, auth_token) 
now = datetime.now()
messageSentTime = now.strftime("%Y-%m-%d %H:%M:%S")

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])

def sms_reply():
  
    resp = MessagingResponse()
    print(request.form['From'])

    if request.form['Body'] == 'Yes' or request.form['Body'] == 'yes' :
        resp.message("Thank You, we will wait for You")

    elif request.form['Body'] == 'No' or request.form['Body'] == 'no':
        try:
            connection = mysql.connector.connect(host='localhost',
                                    port='8889',
                                    unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock',
                                    database='ClientsDB',
                                    user='root',
                                    password='root')
            cursor = connection.cursor()
            cursor.execute("UPDATE Clients SET appointment_date = NULL, message_sent = '{}' WHERE phone_number = '{}'".format(messageSentTime, request.form['From']))
            resp.message("Than You, we cancelled Your appointment.")

        except Error as e:
            print("Error on query execution", e)

        finally:
            if (connection.is_connected()):
                connection.commit()
                connection.close()
                cursor.close()

    else :
        resp.message("Please contact with us to clarify the details about Your appointment")
    
    return str(resp)


print("------------------------------------")
print("Response handler running...")
print("------------------------------------")

if __name__ == "__main__":
    app.run(debug = True)