from twilio.rest import Client

account_sid = 'AC1a0b800ac0ec767155c6548a06e0cdbb'
auth_token = '3a0bf5857ef131ed31f05f80a87cc3d3'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+18664815387',
  body='Helllooooooooo',
  to='+14086671735'
)

print(message.sid)