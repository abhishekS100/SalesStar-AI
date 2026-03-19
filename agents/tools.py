from services.email import send_email
from services.dynamodb import update_lead

def send_outreach_email(lead, email_text):
    send_email(
        to=lead["email"],
        subject="Let's connect!",
        body=email_text
    )

def mark_contacted(lead_id):
    update_lead(lead_id, {"status": "contacted"})