# data/cybersecurity_data.py

cybersecurity_data = {
    "title": "Cybersecurity Roadmap",
    "youtube_playlist": "http://googleusercontent.com/cybersecurity_full_course_placeholder", # Placeholder: Replace with a full course playlist
    "topics": [
        {
            "name": "Introduction to Cybersecurity & CIA Triad (Scratch)",
            "explanation": "Understanding the fundamental concepts of cybersecurity, its importance, common threats (malware, phishing), and the CIA Triad (Confidentiality, Integrity, Availability).",
            "example_code": None,
            "example_output": None,
            "youtube_link": "http://googleusercontent.com/cybersecurity_intro_video_placeholder" # Placeholder
        },
        {
            "name": "Network Security Basics: Firewalls & VPNs (Intermediate)",
            "explanation": "Exploring foundational network security measures. Covers types of firewalls (packet-filtering, stateful, application-layer), their rules, and the role of Virtual Private Networks (VPNs) for secure communication.",
            "example_code": "# Conceptual Firewall Rule:\n# Block incoming traffic from a specific IP\n# iptables -A INPUT -s 192.168.1.10 -j DROP",
            "example_output": "Traffic from 192.168.1.10 is discarded.",
            "youtube_link": "http://googleusercontent.com/network_security_video_placeholder" # Placeholder
        },
        {
            "name": "Web Application Security: OWASP Top 10 (Intermediate)",
            "explanation": "Understanding the most critical web application security risks identified by OWASP. Focus on Injection (SQL, XSS), Broken Authentication, Sensitive Data Exposure, and Security Misconfiguration.",
            "example_code": "# Preventing SQL Injection (Python/Flask conceptual):\n# Instead of: sql = f'SELECT * FROM users WHERE username = '{username}''\n# Use: cursor.execute('SELECT * FROM users WHERE username = ?', (username,))",
            "example_output": "Secure database queries preventing malicious input.",
            "youtube_link": "http://googleusercontent.com/owasp_top10_video_placeholder" # Placeholder
        },
        {
            "name": "Security Information and Event Management (SIEM) (Advanced)",
            "explanation": "Introduction to SIEM systems. Learn how SIEM collects, aggregates, and analyzes security logs and event data from various sources to detect and respond to security threats in real-time. Covers correlation rules and threat intelligence integration.",
            "example_code": None,
            "example_output": None,
            "youtube_link": "http://googleusercontent.com/siem_explanation_placeholder" # Placeholder
        },
        {
            "name": "Cloud Security & Compliance (AWS/Azure/GCP) (Advanced)",
            "explanation": "Securing cloud environments. Covers shared responsibility model, identity and access management (IAM) in the cloud, network security in cloud (VPCs, Security Groups), data encryption, and compliance frameworks (NIST, ISO 27001).",
            "example_code": "# AWS IAM Policy (conceptual JSON):\n# {\n#   'Version': '2012-10-17',\n#   'Statement': [{\n#     'Effect': 'Allow',\n#     'Action': 's3:GetObject',\n#     'Resource': 'arn:aws:s3:::my-secure-bucket/*'\n#   }]\n# }",
            "example_output": "Grants read-only access to a specific S3 bucket.",
            "youtube_link": "http://googleusercontent.com/cloud_security_video_placeholder" # Placeholder
        },
    ]
}