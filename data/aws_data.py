# data/aws_data.py

aws_data = {
    "title": "AWS Cloud Computing Roadmap",
    "youtube_playlist": "http://googleusercontent.com/aws_full_course_placeholder", # Placeholder
    "topics": [
        {
            "name": "Introduction to Cloud Computing & AWS Services (Scratch)",
            "explanation": "Understanding cloud computing concepts (IaaS, PaaS, SaaS), benefits, and an overview of core AWS services like EC2, S3, VPC, IAM, and their use cases.",
            "example_code": None,
            "example_output": None,
            "youtube_link": "http://googleusercontent.com/aws_intro_video_placeholder" # Placeholder
        },
        {
            "name": "Compute Services: EC2 & Lambda (Intermediate)",
            "explanation": "Deep dive into Elastic Compute Cloud (EC2) for virtual servers (instances, AMIs, security groups) and AWS Lambda for serverless computing (functions, triggers, API Gateway integration).",
            "example_code": "# AWS CLI command to launch an EC2 instance (conceptual):\n# aws ec2 run-instances --image-id ami-0abcdef1234567890 --count 1 --instance-type t2.micro --key-name MyKeyPair",
            "example_output": "A new t2.micro EC2 instance starts running.",
            "youtube_link": "http://googleusercontent.com/aws_compute_video_placeholder" # Placeholder
        },
        {
            "name": "Storage Services: S3, EBS, EFS (Intermediate)",
            "explanation": "Exploring AWS storage options: S3 for object storage (buckets, objects, access control), EBS for block storage (volumes, snapshots), and EFS for shared file systems.",
            "example_code": "# AWS CLI command to create an S3 bucket:\n# aws s3 mb s3://my-unique-bucket-name",
            "example_output": "S3 bucket 'my-unique-bucket-name' created.",
            "youtube_link": "http://googleusercontent.com/aws_storage_video_placeholder" # Placeholder
        },
        {
            "name": "Networking: VPC, Subnets & Security Groups (Advanced)",
            "explanation": "Designing and securing your network in AWS. Covers Virtual Private Cloud (VPC), public and private subnets, routing tables, Network Access Control Lists (NACLs), and Security Groups for instance-level firewalling.",
            "example_code": "# Conceptual AWS CLI for Security Group rule:\n# aws ec2 authorize-security-group-ingress --group-id sg-0123456789abcdef0 --protocol tcp --port 80 --cidr 0.0.0.0/0",
            "example_output": "Allows HTTP traffic from anywhere to instances in this security group.",
            "youtube_link": "http://googleusercontent.com/aws_networking_video_placeholder" # Placeholder
        },
        {
            "name": "Database Services: RDS, DynamoDB (Advanced)",
            "explanation": "Using managed database services in AWS. Covers Relational Database Service (RDS) for SQL databases (MySQL, PostgreSQL, Aurora) and DynamoDB for NoSQL (key-value, document) databases.",
            "example_code": "# Conceptual AWS CLI for creating a DynamoDB table:\n# aws dynamodb create-table --table-name MyTable --attribute-definitions AttributeName=Id,AttributeType=S --key-schema AttributeName=Id,KeyType=HASH --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5",
            "example_output": "A new DynamoDB table 'MyTable' is created.",
            "youtube_link": "http://googleusercontent.com/aws_databases_video_placeholder" # Placeholder
        },
    ]
}