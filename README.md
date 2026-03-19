# SalesStar-AI
**Real-Time Sales Automation**

--> An Agentic AI Sales Assistant that can:

* Generate leads (from input or CRM)

* Qualify leads using LLM (Bedrock)

* Generate personalized outreach emails/messages

* Act autonomously via tools (agent behavior)

**🧠 Architecture : Core Components**

AWS Bedrock → LLM (Claude, Titan, etc.)

FastAPI Backend → Orchestration layer

DynamoDB → Lead storage

Step Functions / simple loop → Agent workflow

SES → Send emails

Lambda (optional) → Serverless execution

**⚙️ Install Dependencies**

pip install fastapi uvicorn boto3 pydantic

**🔑 AWS Setup**

Make sure you configure:

aws configure

**▶️ Run the App**

uvicorn app:app --reload

**🔁 Example Flow**

POST /lead

Run /run-agent/{lead_id}

Agent:

Qualifies lead

Writes email

Sends via SES

Updates status
