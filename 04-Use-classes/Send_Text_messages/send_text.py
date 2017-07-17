#!~/envs/udacity-python-env

from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
# Your Auth Token from twilio.com/console
auth_token = "your_auth_token"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+15558675309", # Replace with your phone number
    from_="+15017250604", # Replace with your Twilio number
    body="Hello from Python!")

print(message.sid)
