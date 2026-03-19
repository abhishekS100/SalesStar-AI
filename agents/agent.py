from services.bedrock import invoke_llm
from agent.prompts import QUALIFY_PROMPT, EMAIL_PROMPT
from agent.tools import send_outreach_email, mark_contacted

class SalesAgent:

    def qualify_lead(self, lead):
        prompt = QUALIFY_PROMPT.format(**lead)
        return invoke_llm(prompt)

    def generate_email(self, lead):
        prompt = EMAIL_PROMPT.format(**lead)
        return invoke_llm(prompt)

    def run(self, lead):
        print("🔍 Qualifying lead...")
        qualification = self.qualify_lead(lead)

        print("✉️ Generating email...")
        email = self.generate_email(lead)

        print("📤 Sending email...")
        send_outreach_email(lead, email)

        mark_contacted(lead["id"])

        return {
            "qualification": qualification,
            "email": email
        }