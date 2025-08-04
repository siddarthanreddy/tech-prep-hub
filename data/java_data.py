# data/java_data.py

java_data = {
    "title": "Java Developer Roadmap",
    "youtube_playlist": "http://googleusercontent.com/java_full_course_placeholder", # Placeholder
    "topics": [
        {
            "name": "Java Basics: Syntax, Variables & Control Flow (Scratch)",
            "explanation": "Understanding fundamental Java syntax, data types (primitive and non-primitive), operators, and control flow statements (if-else, loops, switch).",
            "example_code": "public class HelloWorld {\n    public static void main(String[] args) {\n        String message = \"Hello, Java!\";\n        System.out.println(message);\n    }\n}",
            "example_output": "Hello, Java!",
            "youtube_link": "http://googleusercontent.com/java_basics_video_placeholder" # Placeholder
        },
        {
            "name": "Object-Oriented Programming (OOP) in Java (Intermediate)",
            "explanation": "Deep dive into OOP concepts: Encapsulation, Inheritance, Polymorphism, and Abstraction, with practical examples of classes, objects, interfaces, and abstract classes.",
            "example_code": "public class Animal {\n    void makeSound() { System.out.println(\"Animal makes a sound\"); }\n}\nclass Dog extends Animal {\n    void makeSound() { System.out.println(\"Woof\"); }\n}",
            "example_output": "Woof (if Dog object calls makeSound)",
            "youtube_link": "http://googleusercontent.com/java_oop_video_placeholder" # Placeholder
        },
        {
            "name": "Collections Framework & Generics (Intermediate)",
            "explanation": "Learning Java's powerful Collections Framework (List, Set, Map interfaces and their implementations like ArrayList, HashMap) and the importance of Generics for type safety.",
            "example_code": "import java.util.ArrayList;\nList<String> names = new ArrayList<>();\nnames.add(\"Alice\");\nnames.add(\"Bob\");",
            "example_output": "ArrayList containing Alice and Bob.",
            "youtube_link": "http://googleusercontent.com/java_collections_video_placeholder" # Placeholder
        },
        {
            "name": "Spring Boot Framework & REST APIs (Advanced)",
            "explanation": "Building robust web applications and RESTful APIs using Spring Boot. Covers dependency injection, MVC pattern, data access with Spring Data JPA, and creating controller endpoints.",
            "example_code": "@RestController\n@RequestMapping(\"/api/v1/users\")\npublic class UserController {\n    @GetMapping\n    public String getUsers() { return \"List of users\"; }\n}",
            "example_output": "GET /api/v1/users would return 'List of users'.",
            "youtube_link": "http://googleusercontent.com/springboot_rest_video_placeholder" # Placeholder
        },
        {
            "name": "Multithreading & Concurrency in Java (Advanced)",
            "explanation": "Understanding how to write concurrent programs in Java using Threads, Runnables, Executors, synchronization mechanisms (synchronized keyword, locks), and concurrent collections for high-performance applications.",
            "example_code": "public class MyRunnable implements Runnable {\n    public void run() { System.out.println(\"Thread running\"); }\n}\nThread t = new Thread(new MyRunnable());\nt.start();",
            "example_output": "Thread running",
            "youtube_link": "http://googleusercontent.com/java_multithreading_video_placeholder" # Placeholder
        },
    ]
}