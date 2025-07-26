import json
import boto3

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('StudentData')

def lambda_handler(event, context):
    try:
        # Extract data using correct key names
        student_id = event.get('StudentID')
        name = event.get('name')
        student_class = event.get('class')
        age = event.get('age')

        # Basic validation
        if not all([student_id, name, student_class, age]):
            return {
                'statusCode': 400,
                'body': json.dumps('Missing one or more required fields.')
            }

        # Optional: Convert age to int
        age = int(age)

        # Insert item into DynamoDB
        table.put_item(
            Item={
                'StudentID': student_id,
                'name': name,
                'class': student_class,
                'age': age
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps('Student data saved successfully!')
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error: {str(e)}")
        }
