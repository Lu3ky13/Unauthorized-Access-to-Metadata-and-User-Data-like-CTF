import boto3

# AWS session setup
session = boto3.Session(
    aws_access_key_id="add here",
    aws_secret_access_key="add here",
    aws_session_token="add here"
)

# List of services and actions to test
services_and_actions = [
    ("s3", "list_buckets"),
    ("ec2", "describe_instances"),
    ("logs", "describe_log_groups"),
    ("sts", "get_caller_identity"),
    ("eks", "list_clusters"),
    ("iam", "list_users"),
]

# Open a text file to save the output
with open("aws_permissions_output.txt", "w") as output_file:
    for service_name, action in services_and_actions:
        try:
            # Initialize the client
            service = session.client(service_name)
            # Call the specified action
            method = getattr(service, action)
            response = method()
            output_file.write(f"{service_name}.{action}: Success\n")
            output_file.write(str(response) + "\n\n")
        except Exception as e:
            output_file.write(f"{service_name}.{action}: Failed\n")
            output_file.write(f"Error: {e}\n\n")

print("Output saved to aws_permissions_output.txt")
