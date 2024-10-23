from twilio.rest import Client
account_sid = ''
auth_token = '[token]'
client = Client(account_sid, auth_token)

message = client.message.create(
    from_='+1',
    body='test, test',
    to_='+'
)

print(message.sid)

