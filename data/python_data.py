python_data = {
    "title": "Python Programming",
    "youtube_playlist": "https://www.youtube.com/watch?v=rfscVS0vtbw&list=PL-osiE80TeTskfuRMMT2A5gxXLwZPZp4d (Mosh Hamedani - Python for Beginners, and follow up with his advanced courses)\nhttps://www.youtube.com/playlist?list=PL-osiE80TeTsqsMhL_Yh_mP_eH3kYmK0N (Corey Schafer - Python Tutorials)\nhttps://www.youtube.com/playlist?list=PLGLfVvg_OpP-A_6jXh7E7z4fXQJ3qI9C- (Patrick Loeber - Advanced Python)",
    "topics": [
        {
            "name": "1. Introduction & Setup",
            "explanation": "Python is a high-level, interpreted, general-purpose programming language known for its readability and versatility. It's widely used in web development, data science, AI, machine learning, automation, and more. Setting up your environment involves installing Python (preferably via anaconda for data science or directly from python.org) and a good Integrated Development Environment (IDE) like VS Code or PyCharm.",
            "example_code": "# Simple 'Hello, World!' program\nprint('Hello, Python Learner!')\n\n# Checking Python version from within a script\nimport sys\nprint(f'Python version: {sys.version.split()[0]}')",
            "example_output": "Hello, Python Learner!\nPython version: 3.10.12 (or your installed version)",
            "youtube_link": "https://www.youtube.com/watch?v=rfscVS0vtbw&t=150s" # Mosh Hamedani: Installing Python
        },
        {
            "name": "2. Basic Syntax, Variables & Comments",
            "explanation": "Python's syntax emphasizes readability through significant indentation (no curly braces). Variables are dynamically typed placeholders for values. Comments start with `#` for single-line or are enclosed in `'''docstrings'''` for multi-line.",
            "example_code": "message = 'Welcome to Python!' # This is a single-line comment\nnumber = 100\nis_valid = True\n\n'''\nThis is a multi-line comment\nor a docstring.\nIt's often used for function/class documentation.\n'''\n\nprint(message)\nprint(number)\nprint(is_valid)",
            "example_output": "Welcome to Python!\n100\nTrue",
            "youtube_link": "https://www.youtube.com/watch?v=rfscVS0vtbw&t=783s" # Mosh Hamedani: Variables
        },
        {
            "name": "3. Data Types: Numbers, Strings, Booleans",
            "explanation": "Python has several built-in primitive data types:\n- **Numbers:** Integers (`int`), floating-point numbers (`float`), and complex numbers.\n- **Strings:** Sequences of characters (text), immutable, enclosed in single `''`, double `\"\"`, or triple `''' '''` quotes.\n- **Booleans:** Represents truth values: `True` or `False`.",
            "example_code": "int_var = 42\nfloat_var = 3.14159\nstr_var = \"Hello, World!\"\nbool_var = (int_var > 10)\n\nprint(f'Integer: {int_var} (Type: {type(int_var)})')\nprint(f'Float: {float_var} (Type: {type(float_var)})')\nprint(f'String: {str_var} (Type: {type(str_var)})')\nprint(f'Boolean: {bool_var} (Type: {type(bool_var)})')",
            "example_output": "Integer: 42 (Type: <class 'int'>)\nFloat: 3.14159 (Type: <class 'float'>)\nString: Hello, World! (Type: <class 'str'>)\nBoolean: True (Type: <class 'bool'>)",
            "youtube_link": "https://www.youtube.com/watch?v=rfscVS0vtbw&t=1991s" # Mosh Hamedani: Numbers & Strings
        },
        {
            "name": "4. Data Types: Lists, Tuples, Sets, Dictionaries",
            "explanation": "These are Python's built-in collection types:\n- **Lists:** Ordered, mutable (changeable), allows duplicate members. Defined with square brackets `[]`.\n- **Tuples:** Ordered, immutable (unchangeable), allows duplicate members. Defined with parentheses `()`.\n- **Sets:** Unordered, mutable, does not allow duplicate members. Defined with curly braces `{}`.\n- **Dictionaries:** Unordered, mutable, stores data in key-value pairs. Keys must be unique and immutable. Defined with curly braces `{}`.",
            "example_code": "# List example\nmy_list = [1, 'apple', 3.14]\nmy_list.append(4) # Add element\nprint(f'List: {my_list}')\n\n# Tuple example\nmy_tuple = (10, 'banana')\n# my_tuple.append(3) # This would raise an error (immutable)\nprint(f'Tuple: {my_tuple}')\n\n# Set example\nmy_set = {1, 2, 2, 3, 'hello'}\nprint(f'Set: {my_set}')\n\n# Dictionary example\nmy_dict = {'name': 'Alice', 'age': 30}\nprint(f'Dictionary Name: {my_dict['name']}')\nmy_dict['city'] = 'New York' # Add new key-value pair\nprint(f'Updated Dict: {my_dict}')",
            "example_output": "List: [1, 'apple', 3.14, 4]\nTuple: (10, 'banana')\nSet: {1, 2, 3, 'hello'}\nDictionary Name: Alice\nUpdated Dict: {'name': 'Alice', 'age': 30, 'city': 'New York'}",
            "youtube_link": "https://www.youtube.com/watch?v=W8olR8i4K0k (Corey Schafer - Lists, Tuples, Sets)\nhttps://www.youtube.com/watch?v=dais_d0Mkd0 (Corey Schafer - Dictionaries)"
        },
        {
            "name": "5. Operators & Expressions",
            "explanation": "Python uses various operators to perform operations on values and variables:\n- **Arithmetic:** `+`, `-`, `*`, `/` (float division), `//` (integer division), `%` (modulo), `**` (exponentiation).\n- **Comparison:** `==` (equal), `!=` (not equal), `<`, `>`, `<=`, `>=`.\n- **Logical:** `and`, `or`, `not`.\n- **Assignment:** `=`, `+=`, `-=`, `*=`, `/=`, etc.\n- **Identity:** `is`, `is not` (checks if two variables refer to the *same object* in memory).\n- **Membership:** `in`, `not in` (checks if a value is present in a sequence).",
            "example_code": "x, y = 10, 3\nprint(f'x + y = {x + y}')\nprint(f'x // y = {x // y}') # Floor division\nprint(f'x == y: {x == y}')\nprint(f'x > 5 and y < 5: {x > 5 and y < 5}')\n\nmy_list = [1, 2, 3]\nprint(f'2 in my_list: {2 in my_list}')\n\na = [1, 2]\nb = [1, 2]\nprint(f'a is b: {a is b}') # False, different objects\nprint(f'a == b: {a == b}') # True, same values",
            "example_output": "x + y = 13\nx // y = 3\nx == y: False\nx > 5 and y < 5: True\n2 in my_list: True\na is b: False\na == b: True",
            "youtube_link": "https://www.youtube.com/watch?v=m7Q0_Vsx24c (Mosh Hamedani - Operators)"
        },
        {
            "name": "6. Control Flow: If-Elif-Else Statements",
            "explanation": "Conditional statements allow your program to make decisions. `if` executes a block if a condition is true. `elif` (else if) provides additional conditions. `else` executes if none of the preceding conditions are true.",
            "example_code": "score = 85\nif score >= 90:\n    grade = 'A'\nelif score >= 80:\n    grade = 'B'\nelif score >= 70:\n    grade = 'C'\nelse:\n    grade = 'F'\nprint(f'Student's grade: {grade}')",
            "example_output": "Student's grade: B",
            "youtube_link": "https://www.youtube.com/watch?v=rfscVS0vtbw&t=3497s (Mosh Hamedani - If Statements)"
        },
        {
            "name": "7. Control Flow: For Loops",
            "explanation": "Used for iterating over a sequence (list, tuple, dictionary, set, string) or other iterable objects. The `range()` function is commonly used to generate a sequence of numbers for looping a specific number of times.",
            "example_code": "fruits = ['apple', 'banana', 'cherry']\nfor fruit in fruits:\n    print(f'I like {fruit}')\n\nprint('\\nLooping with range():')\nfor i in range(3):\n    print(f'Iteration {i}')",
            "example_output": "I like apple\nI like banana\nI like cherry\n\nLooping with range():\nIteration 0\nIteration 1\nIteration 2",
            "youtube_link": "https://www.youtube.com/watch?v=rfscVS0vtbw&t=5058s (Mosh Hamedani - For Loops)"
        },
        {
            "name": "8. Control Flow: While Loops",
            "explanation": "Executes a block of code repeatedly as long as a specified condition is true. It's crucial to ensure the condition eventually becomes false to avoid an infinite loop. `break` and `continue` statements control loop flow.",
            "example_code": "count = 0\nwhile count < 3:\n    print(f'Count is {count}')\n    count += 1\n\nprint('\\nUsing break and continue:')\nfor i in range(5):\n    if i == 2:\n        continue # Skips current iteration, goes to next\n    if i == 4:\n        break    # Exits the loop entirely\n    print(i)",
            "example_output": "Count is 0\nCount is 1\nCount is 2\n\nUsing break and continue:\n0\n1\n3",
            "youtube_link": "https://www.youtube.com/watch?v=rfscVS0vtbw&t=5794s (Mosh Hamedani - While Loops)"
        },
        {
            "name": "9. Functions",
            "explanation": "Reusable blocks of code that perform a specific task. They promote code reusability, modularity, and readability. Functions are defined with the `def` keyword, can accept arguments, and can return values using `return`.",
            "example_code": "def greet(name):\n    \"\"\"This function greets the person passed in as a parameter.\"\"\"\n    return f'Hello, {name}!'\n\ndef add_numbers(a, b=0):\n    \"\"\"Adds two numbers. b is optional and defaults to 0.\"\"\"\n    print(f'Adding {a} and {b}')\n    return a + b\n\nmessage = greet('David')\nprint(message)\n\nsum1 = add_numbers(10, 20)\nsum2 = add_numbers(5) # Uses default for b\nprint(f'Sum 1: {sum1}, Sum 2: {sum2}')",
            "example_output": "Hello, David!\nAdding 10 and 20\nAdding 5 and 0\nSum 1: 30, Sum 2: 5",
            "youtube_link": "https://www.youtube.com/watch?v=rfscVS0vtbw&t=6385s (Mosh Hamedani - Functions)"
        },
        {
            "name": "10. Lambda Functions",
            "explanation": "Also known as anonymous functions, lambda functions are small, single-expression functions. They are defined using the `lambda` keyword and are often used for short, throwaway functions, especially with higher-order functions like `map()`, `filter()`, and `sorted()`.",
            "example_code": "multiply = lambda a, b: a * b\nprint(f'Product: {multiply(7, 8)}')\n\n# Using lambda with filter()\nnumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\neven_numbers = list(filter(lambda x: x % 2 == 0, numbers))\nprint(f'Even numbers: {even_numbers}')\n\n# Using lambda with sorted()\nstudents = [('Alice', 20), ('Bob', 25), ('Charlie', 18)]\nsorted_students = sorted(students, key=lambda student: student[1])\nprint(f'Students sorted by age: {sorted_students}')",
            "example_output": "Product: 56\nEven numbers: [2, 4, 6, 8, 10]\nStudents sorted by age: [('Charlie', 18), ('Alice', 20), ('Bob', 25)]",
            "youtube_link": "https://www.youtube.com/watch?v=h0U240yE6yQ (Corey Schafer - Lambda Functions)"
        },
        {
            "name": "11. Object-Oriented Programming (OOP) Basics",
            "explanation": "OOP is a programming paradigm based on the concept of 'objects', which can contain data (attributes) and code (methods). Key concepts:\n- **Class:** A blueprint for creating objects.\n- **Object:** An instance of a class.\n- **Attributes:** Variables that belong to an object.\n- **Methods:** Functions defined inside a class that operate on the object's attributes.\n- `__init__`: A special method (constructor) called when an object is created.",
            "example_code": "class Dog:\n    species = \"Canis familiaris\" # Class attribute\n\n    def __init__(self, name, age):\n        self.name = name # Instance attribute\n        self.age = age   # Instance attribute\n\n    def bark(self):\n        return f'{self.name} says Woof! ({self.age} years old).'\n\n    def description(self):\n        return f'{self.name} is {self.age} years old.'\n\nmy_dog = Dog('Buddy', 3)\nyour_dog = Dog('Lucy', 5)\n\nprint(my_dog.bark())\nprint(f'Dog species: {Dog.species}')\nprint(your_dog.description())",
            "example_output": "Buddy says Woof! (3 years old).\nDog species: Canis familiaris\nLucy is 5 years old.",
            "youtube_link": "https://www.youtube.com/watch?v=rfscVS0vtbw&t=7572s (Mosh Hamedani - Classes)\nhttps://www.youtube.com/watch?v=ZfK_xQyqR-I (Corey Schafer - OOP)"
        },
        {
            "name": "12. OOP: Inheritance & Polymorphism",
            "explanation": "Continuing OOP principles:\n- **Inheritance:** A mechanism where a new class (subclass/child) inherits attributes and methods from an existing class (superclass/parent), promoting code reuse.\n- **Polymorphism:** 'Many forms'. Allows objects of different classes to be treated as objects of a common superclass. It's often achieved through method overriding (subclasses provide specific implementations for methods defined in their parent).",
            "example_code": "class Animal:\n    def __init__(self, name):\n        self.name = name\n\n    def speak(self):\n        return f'{self.name} makes a sound.'\n\nclass Dog(Animal):\n    def __init__(self, name, breed):\n        super().__init__(name) # Call parent constructor\n        self.breed = breed\n\n    def speak(self):\n        # Method Overriding\n        return f'{self.name} ({self.breed}) says Woof!'\n\nclass Cat(Animal):\n    def speak(self):\n        # Another Method Overriding\n        return f'{self.name} says Meow!'\n\ndef make_animal_speak(animal):\n    # Polymorphism in action\n    print(animal.speak())\n\nmy_dog = Dog('Buddy', 'Golden Retriever')\nmy_cat = Cat('Whiskers')\n\nmake_animal_speak(my_dog)\nmake_animal_speak(my_cat)\nprint(Animal('Generic').speak())",
            "example_output": "Buddy (Golden Retriever) says Woof!\nWhiskers says Meow!\nGeneric makes a sound.",
            "youtube_link": "https://www.youtube.com/watch?v=RSl87lqOXDE (Corey Schafer - Inheritance)\nhttps://www.youtube.com/watch?v=F3FONi1bPPA (Corey Schafer - Polymorphism)"
        },
        {
            "name": "13. Error Handling (Try-Except-Else-Finally)",
            "explanation": "Python uses exceptions to handle errors. `try` block contains code that might raise an error. `except` catches specific errors. `else` runs if no error occurs. `finally` always runs, regardless of errors, typically for cleanup.",
            "example_code": "def safe_divide(numerator, denominator):\n    try:\n        result = numerator / denominator\n    except ZeroDivisionError:\n        print('Error: Cannot divide by zero!')\n        return None\n    except TypeError:\n        print('Error: Invalid input types!')\n        return None\n    else:\n        print(f'Division successful. Result: {result}')\n        return result\n    finally:\n        print('Division attempt completed.')\n\nsafe_divide(10, 2)\nsafe_divide(10, 0)\nsafe_divide(10, 'a')",
            "example_output": "Division successful. Result: 5.0\nDivision attempt completed.\nError: Cannot divide by zero!\nDivision attempt completed.\nError: Invalid input types!\nDivision attempt completed.",
            "youtube_link": "https://www.youtube.com/watch?v=NI_j-tK6w2E (Corey Schafer - Error Handling)"
        },
        {
            "name": "14. File I/O (Input/Output)",
            "explanation": "Interacting with files on your system. `open()` function is used to open files in different modes ('r' for read, 'w' for write, 'a' for append, 'b' for binary). The `with open(...)` statement is highly recommended as it ensures the file is automatically closed, even if errors occur.",
            "example_code": "# Writing to a file\nfile_name = 'my_notes.txt'\nwith open(file_name, 'w') as f:\n    f.write('Line 1: This is my first line.\\n')\n    f.write('Line 2: And this is the second line.')\nprint(f'Content written to {file_name}')\n\n# Reading from a file line by line\nprint(f'\\nReading content from {file_name}:')\nwith open(file_name, 'r') as f:\n    for line in f:\n        print(line.strip()) # .strip() removes newline characters\n\n# Appending to a file\nwith open(file_name, 'a') as f:\n    f.write('\\nLine 3: Appended from script.')\nprint(f'\\nContent appended to {file_name}.')",
            "example_output": "Content written to my_notes.txt\n\nReading content from my_notes.txt:\nLine 1: This is my first line.\nLine 2: And this is the second line.\n\nContent appended to my_notes.txt.",
            "youtube_link": "https://www.youtube.com/watch?v=Uh2ebFW8OLM (Corey Schafer - File Objects)"
        },
        {
            "name": "15. Modules & Packages",
            "explanation": "Modules are simply Python files (`.py`) containing code (functions, classes, variables). Packages are collections of modules organized in directories, indicated by an `__init__.py` file (which can be empty). They help in organizing code into reusable and manageable units.",
            "example_code": "# Example of importing a built-in module\nimport math\nprint(f'Square root of 81: {math.sqrt(81)}')\nprint(f'Value of Pi: {math.pi}')\n\n# Example of importing specific items from a module\nfrom datetime import date, timedelta\ntoday = date.today()\ntomorrow = today + timedelta(days=1)\nprint(f'Today: {today}, Tomorrow: {tomorrow}')\n\n# Example of importing from a custom package/module (assuming 'my_package/my_module.py')\n# from my_package import my_module\n# my_module.my_function()",
            "example_output": "Square root of 81: 9.0\nValue of Pi: 3.141592653589793\nToday: 2025-08-03, Tomorrow: 2025-08-04 (Dates will vary)",
            "youtube_link": "https://www.youtube.com/watch?v=s_ht4AKnWZg (Corey Schafer - Modules and Pip)"
        },
        {
            "name": "16. Virtual Environments",
            "explanation": "Isolated Python environments that allow you to manage dependencies (libraries/packages) for different projects independently. This prevents conflicts where Project A requires `library_X v1.0` and Project B requires `library_X v2.0`. Tools like `venv` (built-in) or `conda` (for Anaconda users) are common.",
            "example_code": "# Steps in your terminal:\n\n# 1. Create a virtual environment (in your project's root folder):\n#    python -m venv my_project_venv\n\n# 2. Activate the virtual environment:\n#    On Windows: .\\my_project_venv\\Scripts\\activate\n#    On macOS/Linux: source my_project_venv/bin/activate\n\n# 3. Install packages within the active venv:\n#    pip install requests pandas\n\n# 4. Deactivate the virtual environment:\n#    deactivate",
            "example_output": "Outputs are terminal commands. When activated, your terminal prompt changes to include `(my_project_venv)`. Pip installs packages only for that environment."
        },
        {
            "name": "17. Regular Expressions (RegEx)",
            "explanation": "A powerful mini-language for defining search patterns for string matching and manipulation. The `re` module in Python provides functions for working with regular expressions. Used for validation (e.g., email format), parsing text, and complex search-and-replace operations.",
            "example_code": "import re\n\ntext = 'My email is test@example.com, and phone is 123-456-7890.'\n\n# Find an email address\nemail_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}'\nemail_match = re.search(email_pattern, text)\nif email_match:\n    print(f'Found email: {email_match.group()}')\n\n# Replace numbers with 'X'\nnew_text = re.sub(r'\\d', 'X', text)\nprint(f'Text with numbers replaced: {new_text}')\n\n# Find all words starting with 'e'\nwords = re.findall(r'\\b[eE]\\w*', text)\nprint(f'Words starting with e: {words}')",
            "example_output": "Found email: test@example.com\nText with numbers replaced: My email is test@example.com, and phone is XXX-XXX-XXXX.\nWords starting with e: ['email', 'example']",
            "youtube_link": "https://www.youtube.com/watch?v=K8L6LvLhSj8 (Corey Schafer - Regular Expressions)"
        },
        {
            "name": "18. Generators & Iterators",
            "explanation": "Iterators are objects that can be iterated upon (e.g., lists, strings, file objects). They have `__iter__()` and `__next__()` methods. Generators are a simple and memory-efficient way to create iterators. They are defined like functions but use the `yield` keyword instead of `return`, producing a sequence of values one at a time, pausing execution until the next value is requested.",
            "example_code": "def even_numbers_generator(limit):\n    n = 0\n    while n < limit:\n        yield n\n        n += 2\n\nprint('Generated even numbers:')\nfor num in even_numbers_generator(10):\n    print(num)\n\n# Using a generator expression (similar to list comprehension)\nsquares_gen = (x**2 for x in range(5))\nprint(f'\\nSquares from generator: {list(squares_gen)}') # Convert to list to see all values",
            "example_output": "Generated even numbers:\n0\n2\n4\n6\n8\n\nSquares from generator: [0, 1, 4, 9, 16]",
            "youtube_link": "https://www.youtube.com/watch?v=nMf83nI2h0Q (Corey Schafer - Generators)\nhttps://www.youtube.com/watch?v=jW_nK6A0HBg (Patrick Loeber - Generators in Python - Advanced Python 14)"
        },
        {
            "name": "19. Decorators",
            "explanation": "Decorators are a powerful and flexible way to wrap functions or methods, modifying their behavior without permanently altering their original code. They are syntactic sugar that allows you to execute code before and after a function call, making them useful for logging, authentication, memoization, etc.",
            "example_code": "def timing_decorator(func):\n    import time\n    def wrapper(*args, **kwargs):\n        start_time = time.time()\n        result = func(*args, **kwargs)\n        end_time = time.time()\n        print(f'{func.__name__} ran in {end_time - start_time:.4f} seconds')\n        return result\n    return wrapper\n\n@timing_decorator\ndef calculate_sum(n):\n    total = 0\n    for i in range(n):\n        total += i\n    return total\n\n@timing_decorator\ndef greet_person(name):\n    print(f'Hello, {name}!')\n\ncalculate_sum(1000000)\ngreet_person('Grace')",
            "example_output": "calculate_sum ran in 0.0381 seconds (or similar)\nHello, Grace!\ngreet_person ran in 0.0000 seconds (or similar)",
            "youtube_link": "https://www.youtube.com/watch?v=FsAPt_CQdDQ (Corey Schafer - Decorators)\nhttps://www.youtube.com/watch?v=KXdJ3T9q-mQ (Patrick Loeber - Decorators in Python - Advanced Python 13)"
        },
        {
            "name": "20. Advanced Data Structures: Collections Module",
            "explanation": "Python's `collections` module provides specialized container datatypes beyond the built-in ones. Key types include `Counter` (for counting hashable objects), `defaultdict` (for dicts with default values), `namedtuple` (for creating tuple-like objects with named fields), and `deque` (double-ended queue).",
            "example_code": "from collections import Counter, defaultdict, namedtuple, deque\n\n# Counter\nmy_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']\ncounts = Counter(my_list)\nprint(f'Fruit counts: {counts}')\n\n# defaultdict\nd_dict = defaultdict(list)\nd_dict['a'].append(1)\nd_dict['a'].append(2)\nprint(f'Defaultdict: {d_dict}')\n\n# namedtuple\nPoint = namedtuple('Point', ['x', 'y'])\np = Point(10, 20)\nprint(f'Namedtuple Point: {p.x}, {p.y}')\n\n# deque\nd = deque(['a', 'b', 'c'])\nd.appendleft('z')\nd.append('d')\nprint(f'Deque: {list(d)}')",
            "example_output": "Fruit counts: Counter({'apple': 3, 'banana': 2, 'orange': 1})\nDefaultdict: defaultdict(<class 'list'>, {'a': [1, 2]})\nNamedtuple Point: 10, 20\nDeque: ['z', 'a', 'b', 'c', 'd']",
            "youtube_link": "https://www.youtube.com/watch?v=OSGv2VnC0go (Corey Schafer - Collections Module)"
        },
        {
            "name": "21. Context Managers (with statement)",
            "explanation": "Context managers allow you to allocate and release resources precisely when you want to. The `with` statement is used to define a context manager. It simplifies common resource management patterns (like opening/closing files, locking/releasing locks) by ensuring cleanup code is executed automatically.",
            "example_code": "# File handling (common use case)\nwith open('log.txt', 'w') as f:\n    f.write('Log entry 1\\n')\n    print('Inside with block')\nprint('Outside with block. File is automatically closed.')\n\n# Custom context manager (conceptual)\n# class MyContext:\n#     def __enter__(self):\n#         print('Entering context')\n#         return self\n#     def __exit__(self, exc_type, exc_val, exc_tb):\n#         print('Exiting context')\n#\n# with MyContext():\n#     print('Doing something')\n",
            "example_output": "Inside with block\nOutside with block. File is automatically closed.\n(log.txt will contain 'Log entry 1')"
        },
        {
            "name": "22. Web Frameworks: Flask (Advanced Concepts)",
            "explanation": "Beyond basics, explore Flask's blueprints (for modular apps), custom error handlers, request contexts, session management, and integrating with databases using extensions like Flask-SQLAlchemy.",
            "example_code": "# Flask Blueprints (Conceptual in app.py and a new blueprint_folder/routes.py)\n# # app.py\n# from flask import Flask\n# from blueprint_folder.routes import my_blueprint\n# app = Flask(__name__)\n# app.register_blueprint(my_blueprint, url_prefix='/my-feature')\n\n# # blueprint_folder/routes.py\n# from flask import Blueprint, render_template\n# my_blueprint = Blueprint('my_blueprint', __name__)\n# @my_blueprint.route('/')\n# def feature_home():\n#     return 'Welcome to my feature!'",
            "example_output": "Accessing /my-feature/ will show 'Welcome to my feature!'"
        },
        {
            "name": "23. Asynchronous Programming (asyncio)",
            "explanation": "Python's `asyncio` module is used for writing concurrent code using the `async`/`await` syntax. It's ideal for I/O-bound and high-level structured network code (e.g., web servers, database connections) where you don't want to block program execution while waiting for an operation to complete.",
            "example_code": "import asyncio\nimport time\n\nasync def fetch_url(url, delay):\n    print(f'Starting fetch for {url}...')\n    await asyncio.sleep(delay) # Simulate I/O bound task\n    print(f'Finished fetch for {url} after {delay}s')\n    return f'Content from {url}'\n\nasync def main_async():\n    start_time = time.time()\n    # Create tasks that run concurrently\n    task1 = asyncio.create_task(fetch_url('http://site1.com', 3))\n    task2 = asyncio.create_task(fetch_url('http://site2.com', 1))\n\n    # Await results of tasks (they run in parallel)\n    result1 = await task1\n    result2 = await task2\n\n    print(f'\\nAll fetches complete. Total time: {time.time() - start_time:.2f}s')\n    print(f'Result 1: {result1}')\n    print(f'Result 2: {result2}')\n\n# To run an async function (usually only call once at top level)\n# if __name__ == '__main__':\n#     asyncio.run(main_async())",
            "example_output": "Starting fetch for http://site1.com...\nStarting fetch for http://site2.com...\nFinished fetch for http://site2.com after 1s\nFinished fetch for http://site1.com after 3s\n\nAll fetches complete. Total time: 3.00s (approx)\nResult 1: Content from http://site1.com\nResult 2: Content from http://site2.com"
        },
        {
            "name": "24. Testing with Pytest",
            "explanation": "Pytest is a popular, powerful, and easy-to-use Python testing framework. It simplifies writing simple unit tests and scales to complex functional tests. It uses `assert` statements directly and has a rich plugin ecosystem.",
            "example_code": "# Save as: test_calculator.py\n\ndef add(a, b):\n    return a + b\n\ndef subtract(a, b):\n    return a - b\n\ndef test_add():\n    assert add(2, 3) == 5\n    assert add(-1, 1) == 0\n    assert add(0, 0) == 0\n\ndef test_subtract():\n    assert subtract(5, 2) == 3\n    assert subtract(2, 5) == -3\n\n# Run from terminal: pytest",
            "example_output": "============================= test session starts =============================\nplatform linux -- Python 3.9.7, pytest-6.2.5, pluggy-0.13.1\nrootdir: /path/to/your/project\ncollected 2 items\n\ntest_calculator.py ..                                                 [100%]\n\n============================== 2 passed in ...s ==============================",
            "youtube_link": "https://www.youtube.com/watch?v=riF7_2xJz0Q (Corey Schafer - Pytest)"
        },
        {
            "name": "25. Concurrency: Threading vs. Multiprocessing",
            "explanation": "Exploring ways to run multiple operations concurrently. **Threading** runs multiple threads within the *same process*, sharing memory but limited by Python's Global Interpreter Lock (GIL) for CPU-bound tasks. **Multiprocessing** runs multiple *separate processes*, each with its own interpreter and memory, overcoming GIL for CPU-bound tasks but with higher overhead.",
            "example_code": "import time\nimport threading\nimport multiprocessing\n\ndef cpu_bound_task(n):\n    result = 0\n    for i in range(n):\n        result += i*i\n    return result\n\n# Threading example (demonstrates GIL effect for CPU-bound)\ndef run_threading():\n    start = time.time()\n    t1 = threading.Thread(target=cpu_bound_task, args=(5_000_000,))\n    t2 = threading.Thread(target=cpu_bound_task, args=(5_000_000,))\n    t1.start()\n    t2.start()\n    t1.join()\n    t2.join()\n    print(f'Threading took: {time.time() - start:.2f}s')\n\n# Multiprocessing example\ndef run_multiprocessing():\n    start = time.time()\n    p1 = multiprocessing.Process(target=cpu_bound_task, args=(5_000_000,))\n    p2 = multiprocessing.Process(target=cpu_bound_task, args=(5_000_000,))\n    p1.start()\n    p2.start()\n    p1.join()\n    p2.join()\n    print(f'Multiprocessing took: {time.time() - start:.2f}s')\n\n# if __name__ == '__main__':\n#     print(\"Running threading example...\")\n#     run_threading()\n#     print(\"\\nRunning multiprocessing example...\")\n#     run_multiprocessing()",
            "example_output": "Running threading example...\nThreading took: 0.75s (approx, single core time for two tasks)\n\nRunning multiprocessing example...\nMultiprocessing took: 0.40s (approx, if two cores are available)",
            "youtube_link": "https://www.youtube.com/watch?v=elzQpP-6tX8 (Corey Schafer - Multiprocessing)\nhttps://www.youtube.com/watch?v=E_P0D287Yc0 (Corey Schafer - Threading)"
        },
        {
            "name": "26. Metaclasses",
            "explanation": "A metaclass is the class of a class. It defines how a class itself is created. In Python, `type` is the default metaclass. Metaclasses allow you to hook into the class creation process to modify class behavior (e.g., automatically add methods, enforce API consistency). This is an advanced topic typically not needed for everyday programming.",
            "example_code": "def custom_init(self, value):\n    self.value = value.upper() # Force uppercase\n\n# Define a metaclass\nclass UpperCaseAttrs(type):\n    def __new__(mcs, name, bases, namespace):\n        # Modify the __init__ method for all classes using this metaclass\n        if '__init__' not in namespace:\n            namespace['__init__'] = custom_init\n        return super().__new__(mcs, name, bases, namespace)\n\n# Use the metaclass\nclass MyClass(metaclass=UpperCaseAttrs):\n    def display(self):\n        return self.value\n\n# class AnotherClass(metaclass=UpperCaseAttrs):\n#     def __init__(self, item):\n#         self.item = item + '_PROCESSED'\n#     def get_item(self):\n#         return self.item\n\nobj1 = MyClass('hello')\nprint(f'MyClass value: {obj1.display()}')\n\n# obj2 = AnotherClass('world')\n# print(f'AnotherClass item: {obj2.get_item()}')",
            "example_output": "MyClass value: HELLO"
        },
        {
            "name": "27. Descriptors",
            "explanation": "Descriptors are objects that implement at least one of the descriptor protocol methods (`__get__`, `__set__`, `__delete__`). They are used to customize attribute access (getting, setting, or deleting an attribute) on an object. Properties (`@property`) are a common high-level use case of descriptors.",
            "example_code": "class MyDescriptor:\n    def __init__(self, default_value):\n        self.default_value = default_value\n        self.name = None # To store attribute name\n\n    def __set_name__(self, owner, name):\n        self.name = name\n\n    def __get__(self, obj, objtype=None):\n        if obj is None:\n            return self\n        return obj.__dict__.get(self.name, self.default_value)\n\n    def __set__(self, obj, value):\n        if not isinstance(value, str):\n            raise ValueError(f'{self.name} must be a string')\n        obj.__dict__[self.name] = value.upper() # Force uppercase on set\n\nclass User:\n    username = MyDescriptor('Guest')\n    email = MyDescriptor('no_email@example.com')\n\nuser = User()\nprint(f'Default username: {user.username}')\nuser.username = 'john_doe'\nprint(f'New username: {user.username}')\n\ntry:\n    user.username = 123 # This will raise ValueError\nexcept ValueError as e:\n    print(f'Error: {e}')",
            "example_output": "Default username: Guest\nNew username: JOHN_DOE\nError: username must be a string"
        },
        {
            "name": "28. C Extensions (Conceptual)",
            "explanation": "For extreme performance optimization of CPU-bound tasks, Python allows writing extensions in C (or C++). This involves using the Python C API or libraries like Cython or CFFI to create modules that can be imported into Python. This is complex and typically reserved for highly performance-critical parts of libraries.",
            "example_code": "# Conceptual C code snippet for an extension module:\n/*\n#include <Python.h>\n\nstatic PyObject* my_c_function(PyObject* self, PyObject* args) {\n    long num;\n    if (!PyArg_ParseTuple(args, \"l\", &num)) {\n        return NULL;\n    }\n    long result = num * 2; // Simple operation\n    return Py_BuildValue(\"l\", result);\n}\n\nstatic PyMethodDef MyModuleMethods[] = {\n    {\"my_c_function\", my_c_function, METH_VARARGS, \"Doubles a number.\"},\n    {NULL, NULL, 0, NULL}  // Sentinel\n};\n\nstatic struct PyModuleDef mymodule = {\n    PyModuleDef_HEAD_INIT,\n    \"mymodule\",   // name of module\n    NULL,         // module documentation, may be NULL\n    -1,           // size of per-interpreter state of the module, or -1 if the module keeps state in global variables.\n    MyModuleMethods\n};\n\nPyMODINIT_FUNC PyInit_mymodule(void) {\n    return PyModule_Create(&mymodule);\n}\n*/",
            "example_output": "Building and importing this C code would allow Python to call `mymodule.my_c_function(5)` and get `10` very fast."
        }
    ]
}