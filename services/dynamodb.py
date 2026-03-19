import boto3
import uuid

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Leads")

def save_lead(lead):
    lead["id"] = str(uuid.uuid4())
    table.put_item(Item=lead)
    return lead

def get_all_leads():
    return table.scan()["Items"]

def update_lead(lead_id, updates):
    update_expr = "SET " + ", ".join(f"{k}=:{k}" for k in updates)
    expr_values = {f":{k}": v for k, v in updates.items()}

    table.update_item(
        Key={"id": lead_id},
        UpdateExpression=update_expr,
        ExpressionAttributeValues=expr_values
    )