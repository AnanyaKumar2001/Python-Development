# *****************----------------- Sending Text Messages
from twilio.rest import Client

account_sid = "AC97cd261f56c0749fb9163f98cdf91cf7"

auth_token = "d8c7e7ae660282005c124870010e6b6f"

client = Client(account_sid, auth_token)

client.messages.create(
    to="...",
    from_="+12132619743",
    body="Hey There This is sent from AFG-PY"
)
