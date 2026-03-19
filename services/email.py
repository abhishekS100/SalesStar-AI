import boto3

ses = boto3.client("ses", region_name="us-east-1")

SENDER = "verified@email.com"

def send_email(to, subject, body):
    response = ses.send_email(
        Source=SENDER,
        Destination={"ToAddresses": [to]},
        Message={
            "Subject": {"Data": subject},
            "Body": {"Text": {"Data": body}},
        },
    )
    return response