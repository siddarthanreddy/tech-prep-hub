# data/devops_data.py

devops_data = {
    "title": "DevOps Roadmap",
    "youtube_playlist": "http://googleusercontent.com/devops_full_course_placeholder", # Placeholder
    "topics": [
        {
            "name": "Introduction to DevOps & Principles (Scratch)",
            "explanation": "Understanding the philosophy, principles (CALMS), and culture of DevOps. Covers the 'why' behind practices like CI/CD, Infrastructure as Code, and continuous monitoring.",
            "example_code": None,
            "example_output": None,
            "youtube_link": "http://googleusercontent.com/devops_intro_video_placeholder" # Placeholder
        },
        {
            "name": "Version Control with Git & GitHub (Intermediate)",
            "explanation": "Mastering distributed version control with Git (commands like clone, add, commit, push, pull, branch, merge) and collaborating using platforms like GitHub (pull requests, branching strategies).",
            "example_code": "# Git commands:\n# git clone <repo_url>\n# git add .\n# git commit -m 'Initial commit'\n# git push origin main",
            "example_output": "Code changes tracked and pushed to remote repository.",
            "youtube_link": "http://googleusercontent.com/git_github_video_placeholder" # Placeholder
        },
        {
            "name": "CI/CD Pipelines: Jenkins/GitHub Actions (Intermediate)",
            "explanation": "Implementing Continuous Integration and Continuous Delivery/Deployment. Covers building automated pipelines to compile, test, package, and deploy code changes quickly and reliably using tools like Jenkins or GitHub Actions.",
            "example_code": "# Conceptual GitHub Actions YAML snippet:\n# name: CI/CD Pipeline\n# on: [push]\n# jobs:\n#   build-and-deploy:\n#     runs-on: ubuntu-latest\n#     steps:\n#       - uses: actions/checkout@v2\n#       - run: npm install\n#       - run: npm test\n#       - run: npm run build",
            "example_output": "Automated build, test, and package on code push.",
            "youtube_link": "http://googleusercontent.com/cicd_pipeline_video_placeholder" # Placeholder
        },
        {
            "name": "Containerization with Docker (Advanced)",
            "explanation": "Understanding containerization principles and mastering Docker. Covers Dockerfiles, building images, running containers, Docker Compose for multi-container applications, and container networking.",
            "example_code": "# Basic Dockerfile:\n# FROM node:14\n# WORKDIR /app\n# COPY . .\n# RUN npm install\n# CMD [\"node\", \"server.js\"]",
            "example_output": "Creates a Docker image for a Node.js application.",
            "youtube_link": "http://googleusercontent.com/docker_basics_video_placeholder" # Placeholder
        },
        {
            "name": "Orchestration with Kubernetes (Advanced)",
            "explanation": "Managing containerized applications at scale using Kubernetes. Covers concepts like Pods, Deployments, Services, Namespaces, ReplicaSets, and basic kubectl commands for cluster management.",
            "example_code": "# Basic Kubernetes Deployment YAML:\n# apiVersion: apps/v1\n# kind: Deployment\n# metadata:\n#   name: my-app-deployment\n# spec:\n#   replicas: 3\n#   selector: { matchLabels: { app: my-app } }\n#   template:\n#     metadata: { labels: { app: my-app } }\n#     spec:\n#       containers: [{ name: my-app, image: my-app-image }]",
            "example_output": "Deploys 3 replicas of 'my-app-image' container.",
            "youtube_link": "http://googleusercontent.com/kubernetes_basics_video_placeholder" # Placeholder
        },
    ]
}