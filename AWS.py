import boto3

# Initialize a session using the provided credentials
session = boto3.Session(
    aws_access_key_id='',
    aws_secret_access_key='',
    aws_session_token='',
    region_name='us-east-1'
)

# Create an IAM client
iam_client = session.client('iam')

# Get the details of the current role
try:
    role_name = 'GetMyFilesHandler-role-9lvbosrl'
    role_details = iam_client.get_role(RoleName=role_name)
    print(role_details)
except iam_client.exceptions.AccessDenied as e:
    print("Access Denied:", e)
