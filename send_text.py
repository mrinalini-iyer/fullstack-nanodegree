from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC58930cf3320c925198af67c3fec54f2a"
# Your Auth Token from twilio.com/console
auth_token  = "6a2911dcbb24b3cc58eda54735dec6df"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+19496103089", 
    from_="+15626081073",
    body="I love you !")

print(message.sid)
