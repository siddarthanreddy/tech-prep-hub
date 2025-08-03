# tech-prep-hub/data/problems_data.py

problems_data = [
    {
        "id": 1,
        "title": "Reverse a String",
        "company": "TCS",
        "difficulty": "Easy",
        "link": "#", # Keep as placeholder if no external link
        "solution_explanation": "A common way to reverse a string in Python is to use slicing with a step of -1. Alternatively, you can iterate through the string backwards or use `reversed()` and `join()`.",
        "solution_code": "def reverse_string(s):\n    return s[::-1]\n\n# Example Usage:\nmy_string = \"hello\"\nreversed_str = reverse_string(my_string)\nprint(f\"Original: {my_string}, Reversed: {reversed_str}\")\n\n# Another method:\ndef reverse_with_loop(s):\n    reversed_s = \"\"\n    for char in s:\n        reversed_s = char + reversed_s\n    return reversed_s",
        "solution_output": "Original: hello, Reversed: olleh"
    },
    {
        "id": 2,
        "title": "Check Palindrome",
        "company": "Infosys",
        "difficulty": "Easy",
        "link": "#",
        "solution_explanation": "A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward. To check, simply compare the original string with its reversed version. Make sure to handle case and non-alphanumeric characters if required (though not in this basic example).",
        "solution_code": "def is_palindrome(s):\n    # For basic check, convert to lowercase and remove spaces\n    s = s.lower().replace(' ', '')\n    return s == s[::-1]\n\n# Example Usage:\nprint(f\"'madam' is palindrome: {is_palindrome('madam')}\")\nprint(f\"'hello' is palindrome: {is_palindrome('hello')}\")\nprint(f\"'A man a plan a canal Panama' is palindrome: {is_palindrome('A man a plan a canal Panama')}\")",
        "solution_output": "'madam' is palindrome: True\n'hello' is palindrome: False\n'A man a plan a canal Panama' is palindrome: True"
    },
    {
        "id": 3,
        "title": "Factorial of a Number",
        "company": "Wipro",
        "difficulty": "Easy",
        "link": "#",
        "solution_explanation": "The factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n. Can be solved iteratively or recursively. Base case is 0! = 1 and 1! = 1.",
        "solution_code": "# Iterative solution\ndef factorial_iterative(n):\n    if n < 0: return 'Factorial not defined for negative numbers'\n    if n == 0: return 1\n    res = 1\n    for i in range(1, n + 1):\n        res *= i\n    return res\n\n# Recursive solution\ndef factorial_recursive(n):\n    if n < 0: return 'Factorial not defined for negative numbers'\n    if n == 0 or n == 1: return 1\n    return n * factorial_recursive(n - 1)\n\n# Example Usage:\nprint(f\"Factorial of 5 (iterative): {factorial_iterative(5)}\")\nprint(f\"Factorial of 0 (recursive): {factorial_recursive(0)}\")",
        "solution_output": "Factorial of 5 (iterative): 120\nFactorial of 0 (recursive): 1"
    },
    {
        "id": 4,
        "title": "Fibonacci Series",
        "company": "Accenture",
        "difficulty": "Medium",
        "link": "#",
        "solution_explanation": "The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. (e.g., 0, 1, 1, 2, 3, 5, 8...). Can be generated iteratively or recursively (though recursive is less efficient without memoization).",
        "solution_code": "# Iterative solution\ndef fibonacci_iterative(n):\n    if n <= 0: return []\n    if n == 1: return [0]\n    \n    series = [0, 1]\n    while len(series) < n:\n        next_fib = series[-1] + series[-2]\n        series.append(next_fib)\n    return series\n\n# Recursive solution (with memoization for efficiency)\nmemo = {}\ndef fibonacci_recursive_memo(n):\n    if n <= 0: return 0\n    if n == 1: return 1\n    if n in memo: return memo[n]\n    \n    result = fibonacci_recursive_memo(n-1) + fibonacci_recursive_memo(n-2)\n    memo[n] = result\n    return result\n\n# Example Usage:\nprint(f\"Fibonacci series up to 7 terms (iterative): {fibonacci_iterative(7)}\")\nprint(f\"7th Fibonacci number (recursive): {fibonacci_recursive_memo(6)}\")",
        "solution_output": "Fibonacci series up to 7 terms (iterative): [0, 1, 1, 2, 3, 5, 8]\n7th Fibonacci number (recursive): 8"
    },
    {
        "id": 5,
        "title": "Array Sum",
        "company": "Capgemini",
        "difficulty": "Easy",
        "link": "#",
        "solution_explanation": "To find the sum of elements in an array (or list in Python), you can iterate through the elements and add them to a running total, or simply use Python's built-in `sum()` function for convenience.",
        "solution_code": "# Using built-in sum()\ndef array_sum_builtin(arr):\n    return sum(arr)\n\n# Using a loop\ndef array_sum_loop(arr):\n    total = 0\n    for num in arr:\n        total += num\n    return total\n\n# Example Usage:\nmy_array = [10, 20, 30, 40]\nprint(f\"Sum of array (builtin): {array_sum_builtin(my_array)}\")\nprint(f\"Sum of array (loop): {array_sum_loop([1, 2, 3])}\")",
        "solution_output": "Sum of array (builtin): 100\nSum of array (loop): 6"
    },
    {
        "id": 6,
        "title": "Prime Number Check",
        "company": "TCS",
        "difficulty": "Easy",
        "link": "#",
        "solution_explanation": "A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. To check if a number is prime, iterate from 2 up to the square root of the number. If any number in this range divides it evenly, it's not prime.",
        "solution_code": "import math\n\ndef is_prime(n):\n    if n <= 1: return False\n    if n <= 3: return True\n    if n % 2 == 0 or n % 3 == 0: return False\n    i = 5\n    while i * i <= n:\n        if n % i == 0 or n % (i + 2) == 0: return False\n        i += 6\n    return True\n\nprint(f\"7 is prime: {is_prime(7)}\")\nprint(f\"10 is prime: {is_prime(10)}\")\nprint(f\"2 is prime: {is_prime(2)}\")\nprint(f\"1 is prime: {is_prime(1)}\")",
        "solution_output": "7 is prime: True\n10 is prime: False\n2 is prime: True\n1 is prime: False"
    },
    {
        "id": 7,
        "title": "Anagram Check",
        "company": "Infosys",
        "difficulty": "Medium",
        "link": "#",
        "solution_explanation": "Two strings are anagrams if they contain the same characters with the same frequencies, but in a different order. A common approach is to sort both strings and compare them. Alternatively, use hash maps (dictionaries) to count character frequencies in both strings and then compare the frequency maps.",
        "solution_code": "def are_anagrams(s1, s2):\n    # Normalize strings: lowercase, remove spaces\n    s1 = s1.lower().replace(' ', '')\n    s2 = s2.lower().replace(' ', '')\n    return sorted(list(s1)) == sorted(list(s2))\n\n# Using character counts (more efficient for very long strings or large alphabet)\nfrom collections import Counter\ndef are_anagrams_count(s1, s2):\n    s1 = s1.lower().replace(' ', '')\n    s2 = s2.lower().replace(' ', '')\n    return Counter(s1) == Counter(s2)\n\nprint(f\"'listen' and 'silent' are anagrams: {are_anagrams('listen', 'silent')}\")\nprint(f\"'hello' and 'world' are anagrams: {are_anagrams('hello', 'world')}\")",
        "solution_output": "'listen' and 'silent' are anagrams: True\n'hello' and 'world' are anagrams: False"
    },
    {
        "id": 8,
        "title": "Count Vowels",
        "company": "Wipro",
        "difficulty": "Easy",
        "link": "#",
        "solution_explanation": "Count the number of vowels (a, e, i, o, u) in a given string. Convert the string to lowercase to handle both uppercase and lowercase vowels easily. Then iterate through the string and check if each character is in the set of vowels.",
        "solution_code": "def count_vowels(s):\n    vowels = \"aeiou\"\n    count = 0\n    for char in s.lower():\n        if char in vowels:\n            count += 1\n    return count\n\nprint(f\"Vowels in 'Hello World': {count_vowels('Hello World')}\")\nprint(f\"Vowels in 'Python': {count_vowels('Python')}\")",
        "solution_output": "Vowels in 'Hello World': 3\nVowels in 'Python': 1"
    },
    {
        "id": 9,
        "title": "Remove Duplicates from Array",
        "company": "Accenture",
        "difficulty": "Medium",
        "link": "#",
        "solution_explanation": "To remove duplicate elements from an array (list), you can convert it to a set (which by definition contains only unique elements) and then convert it back to a list. If order needs to be preserved, iterate and use a separate list or a hash set to track seen elements.",
        "solution_code": "def remove_duplicates_set(arr):\n    return list(set(arr))\n\ndef remove_duplicates_preserve_order(arr):\n    seen = set()\n    result = []\n    for item in arr:\n        if item not in seen:\n            seen.add(item)\n            result.append(item)\n    return result\n\nmy_array = [1, 2, 2, 3, 1, 4, 5, 4]\nprint(f\"Original: {my_array}\")\nprint(f\"Duplicates removed (unordered): {remove_duplicates_set(my_array)}\")\nprint(f\"Duplicates removed (ordered): {remove_duplicates_preserve_order(my_array)}\")",
        "solution_output": "Original: [1, 2, 2, 3, 1, 4, 5, 4]\nDuplicates removed (unordered): [1, 2, 3, 4, 5] (order may vary)\nDuplicates removed (ordered): [1, 2, 3, 4, 5]"
    },
    {
        "id": 10,
        "title": "Merge Two Sorted Arrays",
        "company": "Capgemini",
        "difficulty": "Medium",
        "link": "#",
        "solution_explanation": "Merge two sorted arrays into a single sorted array. A common approach is to use two pointers, one for each array, and compare elements, adding the smaller one to the result array. This can be done in O(n+m) time.",
        "solution_code": "def merge_sorted_arrays(arr1, arr2):\n    merged = []\n    ptr1, ptr2 = 0, 0\n    \n    while ptr1 < len(arr1) and ptr2 < len(arr2):\n        if arr1[ptr1] < arr2[ptr2]:\n            merged.append(arr1[ptr1])\n            ptr1 += 1\n        else:\n            merged.append(arr2[ptr2])\n            ptr2 += 1\n            \n    # Add remaining elements from either array\n    merged.extend(arr1[ptr1:])\n    merged.extend(arr2[ptr2:])\n    \n    return merged\n\nprint(f\"Merged: {merge_sorted_arrays([1, 3, 5], [2, 4, 6])}\")\nprint(f\"Merged: {merge_sorted_arrays([10, 20], [5])}\")",
        "solution_output": "Merged: [1, 2, 3, 4, 5, 6]\nMerged: [5, 10, 20]"
    },
    {
        "id": 11,
        "title": "Longest Common Prefix",
        "company": "TCS",
        "difficulty": "Medium",
        "link": "#",
        "solution_explanation": "Find the longest common prefix string amongst an array of strings. One way is to sort the array and compare the first and last strings. Another is to iterate through characters of the first string and compare it with all other strings.",
        "solution_code": "def longest_common_prefix(strs):\n    if not strs: return \"\"\n    \n    strs.sort() # Sorts lexicographically\n    first_str = strs[0]\n    last_str = strs[-1]\n    \n    i = 0\n    while i < len(first_str) and i < len(last_str) and first_str[i] == last_str[i]:\n        i += 1\n        \n    return first_str[:i]\n\nprint(f\"LCP: {longest_common_prefix(['flower', 'flow', 'flight'])}\")\nprint(f\"LCP: {longest_common_prefix(['dog', 'racecar', 'car'])}\")",
        "solution_output": "LCP: fl\nLCP: "
    },
    {
        "id": 12,
        "title": "Find Missing Number",
        "company": "Infosys",
        "difficulty": "Easy",
        "link": "#",
        "solution_explanation": "Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array. Common approaches include using XOR, summing numbers (expected sum vs. actual sum), or sorting and checking for gaps.",
        "solution_code": "def find_missing_number_sum(nums):\n    n = len(nums)\n    expected_sum = n * (n + 1) // 2\n    actual_sum = sum(nums)\n    return expected_sum - actual_sum\n\ndef find_missing_number_xor(nums):\n    n = len(nums)\n    xor_sum = 0\n    for i in range(n + 1):\n        xor_sum ^= i\n    for num in nums:\n        xor_sum ^= num\n    return xor_sum\n\nprint(f\"Missing number (sum): {find_missing_number_sum([3, 0, 1])}\")\nprint(f\"Missing number (xor): {find_missing_number_xor([9, 6, 4, 2, 3, 5, 7, 0, 1])}\")",
        "solution_output": "Missing number (sum): 2\nMissing number (xor): 8"
    },
    {
        "id": 13,
        "title": "Subarray with Given Sum",
        "company": "Wipro",
        "difficulty": "Hard",
        "link": "#",
        "solution_explanation": "Given an unsorted array of non-negative integers, find a continuous subarray which adds to a given sum. Can be solved using a sliding window approach for non-negative numbers, or a hash map for positive/negative numbers.",
        "solution_code": "def subarray_sum(arr, target_sum):\n    current_sum = 0\n    start = 0\n    \n    for i in range(len(arr)):\n        current_sum += arr[i]\n        \n        while current_sum > target_sum and start < i:\n            current_sum -= arr[start]\n            start += 1\n            \n        if current_sum == target_sum:\n            return arr[start:i+1] # Found subarray\n            \n    return [] # No subarray found\n\nprint(f\"Subarray for sum 12: {subarray_sum([1, 4, 20, 3, 10, 5], 33)}\")\nprint(f\"Subarray for sum 12: {subarray_sum([1, 4, 0, 0, 3, 10, 5], 7)}\")",
        "solution_output": "Subarray for sum 12: [20, 3, 10]\nSubarray for sum 12: [4, 0, 0, 3]"
    },
    {
        "id": 14,
        "title": "Rotate Array",
        "company": "Accenture",
        "difficulty": "Medium",
        "link": "#",
        "solution_explanation": "Rotate an array to the right by k steps. This can be done by repeatedly rotating one step at a time (inefficient), by using extra space (copying and shifting), or by using the reverse method three times which is in-place and efficient.",
        "solution_code": "def rotate_array(nums, k):\n    n = len(nums)\n    k %= n # Handle cases where k is larger than n\n    \n    # Using slicing and concatenation (not in-place, but simple)\n    # return nums[n-k:] + nums[:n-k]\n\n    # In-place using reversal\n    def reverse(arr, start, end):\n        while start < end:\n            arr[start], arr[end] = arr[end], arr[start]\n            start += 1\n            end -= 1\n    \n    reverse(nums, 0, n - 1)      # Reverse entire array\n    reverse(nums, 0, k - 1)      # Reverse first k elements\n    reverse(nums, k, n - 1)      # Reverse remaining n-k elements\n    \n    return nums\n\nmy_nums = [1, 2, 3, 4, 5, 6, 7]\nprint(f\"Rotated by 3: {rotate_array(my_nums, 3)}\")\nmy_nums = [-1, -100, 3, 99]\nprint(f\"Rotated by 2: {rotate_array(my_nums, 2)}\")",
        "solution_output": "Rotated by 3: [5, 6, 7, 1, 2, 3, 4]\nRotated by 2: [3, 99, -1, -100]"
    },
    {
        "id": 15,
        "title": "Implement Queue using Stacks",
        "company": "Capgemini",
        "difficulty": "Hard",
        "link": "#",
        "solution_explanation": "Implement a queue (FIFO - First-In, First-Out) using two stacks. One stack is for enqueue (input), and the other is for dequeue (output). For dequeue, if the output stack is empty, transfer all elements from the input stack to the output stack.",
        "solution_code": "class MyQueue:\n    def __init__(self):\n        self.in_stack = []\n        self.out_stack = []\n\n    def push(self, x: int) -> None:\n        self.in_stack.append(x)\n\n    def pop(self) -> int:\n        self._transfer_if_needed()\n        return self.out_stack.pop()\n\n    def peek(self) -> int:\n        self._transfer_if_needed()\n        return self.out_stack[-1]\n\n    def empty(self) -> bool:\n        return not self.in_stack and not self.out_stack\n\n    def _transfer_if_needed(self):\n        if not self.out_stack:\n            while self.in_stack:\n                self.out_stack.append(self.in_stack.pop())\n\n# Example Usage:\nmyQueue = MyQueue()\nmyQueue.push(1) # queue is: [1]\nmyQueue.push(2) # queue is: [1, 2]\nprint(f\"Peek: {myQueue.peek()}\") # return 1\nprint(f\"Pop: {myQueue.pop()}\")   # return 1, queue is [2]\nprint(f\"Empty: {myQueue.empty()}\") # return False",
        "solution_output": "Peek: 1\nPop: 1\nEmpty: False"
    },
    {
        "id": 16,
        "title": "Validate Parentheses",
        "company": "TCS",
        "difficulty": "Medium",
        "link": "#",
        "solution_explanation": "Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. An input string is valid if: Open brackets must be closed by the same type of brackets. Open brackets must be closed in the correct order. Every close bracket has a corresponding open bracket of the same type. Use a stack to track open brackets.",
        "solution_code": "def is_valid_parentheses(s: str) -> bool:\n    stack = []\n    mapping = {\")\": \"(\", \"]\": \"[\", \"}\": \"{\"} # Maps closing to opening brackets\n    \n    for char in s:\n        if char in mapping.values(): # It's an opening bracket\n            stack.append(char)\n        elif char in mapping.keys(): # It's a closing bracket\n            if not stack or mapping[char] != stack.pop():\n                return False # Mismatch or stack empty (no open bracket)\n        else:\n            # Ignore other characters if any, or raise error if only brackets are expected\n            pass\n            \n    return not stack # True if stack is empty (all brackets matched), False otherwise\n\nprint(f\"'()[]{{}}' is valid: {is_valid_parentheses('()[]{}')}\")\nprint(f\"'(]' is valid: {is_valid_parentheses('(]')}\")\nprint(f\"'([{{}}])' is valid: {is_valid_parentheses('([{}])')}\")\nprint(f\"'{{[}}' is valid: {is_valid_parentheses('{[}')}\")",
        "solution_output": "'()[]{}' is valid: True\n'(]' is valid: False\n'([{}])' is valid: True\n'{[}' is valid: False"
    },
    {
        "id": 17,
        "title": "Binary Search",
        "company": "Infosys",
        "difficulty": "Easy",
        "link": "#",
        "solution_explanation": "Binary search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing in half the portion of the list that could contain the item, until you've narrowed down the possible locations to just one. It has a time complexity of O(log n).",
        "solution_code": "def binary_search(arr, target):\n    low = 0\n    high = len(arr) - 1\n\n    while low <= high:\n        mid = (low + high) // 2\n        if arr[mid] == target:\n            return mid # Target found at index mid\n        elif arr[mid] < target:\n            low = mid + 1 # Target is in the right half\n        else:\n            high = mid - 1 # Target is in the left half\n    return -1 # Target not found\n\nmy_sorted_array = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]\nprint(f\"Index of 12: {binary_search(my_sorted_array, 12)}\")\nprint(f\"Index of 30: {binary_search(my_sorted_array, 30)}\")",
        "solution_output": "Index of 12: 3\nIndex of 30: -1"
    },
    {
        "id": 18,
        "title": "Linked List Cycle Detection",
        "company": "Wipro",
        "difficulty": "Medium",
        "link": "#",
        "solution_explanation": "Detect if a singly linked list has a cycle in it. Floyd's Cycle-Finding Algorithm (or Tortoise and Hare algorithm) is a common method: use two pointers, one slow (moves one step at a time) and one fast (moves two steps at a time). If they meet, there's a cycle. If the fast pointer reaches the end, no cycle.",
        "solution_code": "class ListNode:\n    def __init__(self, x):\n        self.val = x\n        self.next = None\n\ndef hasCycle(head: ListNode) -> bool:\n    if not head or not head.next:\n        return False # No cycle if list has 0 or 1 node\n\n    slow = head\n    fast = head.next\n\n    while fast and fast.next:\n        if slow == fast:\n            return True # Cycle detected\n        slow = slow.next\n        fast = fast.next.next\n\n    return False # No cycle found\n\n# Example Usage:\n# 1 -> 2 -> 3 -> 4 -> 2 (cycle)\nl1 = ListNode(1)\nl2 = ListNode(2)\nl3 = ListNode(3)\nl4 = ListNode(4)\nl1.next = l2\nl2.next = l3\nl3.next = l4\nl4.next = l2 # Creates cycle\nprint(f\"Has cycle: {hasCycle(l1)}\")\n\n# 5 -> 6 -> 7 (no cycle)\nl5 = ListNode(5)\nl6 = ListNode(6)\nl7 = ListNode(7)\nl5.next = l6\nl6.next = l7\nprint(f\"Has cycle: {hasCycle(l5)}\")",
        "solution_output": "Has cycle: True\nHas cycle: False"
    },
    {
        "id": 19,
        "title": "Invert Binary Tree",
        "company": "Accenture",
        "difficulty": "Medium",
        "link": "#",
        "solution_explanation": "Invert a binary tree, meaning for every node, swap its left and right children. This can be done recursively (post-order traversal is common) or iteratively using a queue (BFS).",
        "solution_code": "class TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef invertTree(root: TreeNode) -> TreeNode:\n    if not root:\n        return None\n    \n    # Swap the children\n    root.left, root.right = root.right, root.left\n    \n    # Recursively invert children\n    invertTree(root.left)\n    invertTree(root.right)\n    \n    return root\n\n# Helper to print tree (BFS traversal)\ndef print_tree_bfs(root):\n    if not root: return \"[]\"\n    queue = [root]\n    result = []\n    while queue:\n        node = queue.pop(0)\n        if node:\n            result.append(node.val)\n            queue.append(node.left)\n            queue.append(node.right)\n        else:\n            result.append(None)\n    # Trim trailing None\n    while result and result[-1] is None:\n        result.pop()\n    return result\n\n# Example Usage:\n# Original:   4\n#            / \\\n#           2   7\n#          / \\ / \\\n#         1  3 6  9\nroot = TreeNode(4)\nroot.left = TreeNode(2, TreeNode(1), TreeNode(3))\nroot.right = TreeNode(7, TreeNode(6), TreeNode(9))\n\nprint(f\"Original tree (BFS): {print_tree_bfs(root)}\")\ninverted_root = invertTree(root)\nprint(f\"Inverted tree (BFS): {print_tree_bfs(inverted_root)}\")",
        "solution_output": "Original tree (BFS): [4, 2, 7, 1, 3, 6, 9]\nInverted tree (BFS): [4, 7, 2, 9, 6, 3, 1]"
    },
    {
        "id": 20,
        "title": "Find Kth Largest Element",
        "company": "Capgemini",
        "difficulty": "Hard",
        "link": "#",
        "solution_explanation": "Find the k-th largest element in an unsorted array. This is a classic problem that can be solved efficiently using a min-heap (priority queue) of size k, or by applying a modified QuickSelect algorithm (average O(N)). Sorting the array is also an option (O(N log N)).",
        "solution_code": "import heapq\n\ndef findKthLargest_heap(nums, k):\n    # Create a min-heap of the first k elements\n    min_heap = nums[:k]\n    heapq.heapify(min_heap)\n    \n    # Iterate through the rest of the array\n    for i in range(k, len(nums)):\n        if nums[i] > min_heap[0]:\n            heapq.heapreplace(min_heap, nums[i]) # Pop smallest, push new element\n            \n    return min_heap[0]\n\n# Example Usage:\nnums = [3, 2, 1, 5, 6, 4]\nk = 2\nprint(f\"The {k}th largest element is: {findKthLargest_heap(nums, k)}\")\n\nnums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]\nk2 = 4\nprint(f\"The {k2}th largest element is: {findKthLargest_heap(nums2, k2)}\")",
        "solution_output": "The 2th largest element is: 5\nThe 4th largest element is: 4"
    },
    {
        "id": 21,
        "title": "Maximal Square",
        "company": "TCS",
        "difficulty": "Hard",
        "link": "#",
        "solution_explanation": "Given a `m x n` binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area. This is a dynamic programming problem. Create a DP table where `dp[i][j]` represents the side length of the maximum square whose bottom-right corner is `(i, j)`. If `matrix[i][j]` is 1, `dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])`. Otherwise, `dp[i][j] = 0`.",
        "solution_code": "def maximalSquare(matrix) -> int:\n    if not matrix or not matrix[0]:\n        return 0\n        \n    rows = len(matrix)\n    cols = len(matrix[0])\n    \n    # dp[i][j] stores the side length of the largest square \n    # ending at (i-1, j-1) with all ones\n    dp = [[0] * (cols + 1) for _ in range(rows + 1)]\n    max_side = 0\n    \n    for i in range(1, rows + 1):\n        for j in range(1, cols + 1):\n            if matrix[i-1][j-1] == '1':\n                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])\n                max_side = max(max_side, dp[i][j])\n                \n    return max_side * max_side\n\nmatrix1 = [\n  [\"1\",\"0\",\"1\",\"0\",\"0\"],\n  [\"1\",\"0\",\"1\",\"1\",\"1\"],\n  [\"1\",\"1\",\"1\",\"1\",\"1\"],\n  [\"1\",\"0\",\"0\",\"1\",\"0\"]\n]\nprint(f\"Maximal Square Area: {maximalSquare(matrix1)}\")\n\nmatrix2 = [[\"0\",\"1\"],[\"1\",\"0\"]]\nprint(f\"Maximal Square Area: {maximalSquare(matrix2)}\")",
        "solution_output": "Maximal Square Area: 4\nMaximal Square Area: 1"
    },
    {
        "id": 22,
        "title": "Partition List",
        "company": "Infosys",
        "difficulty": "Medium",
        "link": "#",
        "solution_explanation": "Given the `head` of a linked list and an integer `x`, partition the list such that all nodes less than `x` come before all nodes greater than or equal to `x`. You should preserve the original relative order of the nodes in each of the two partitions. This can be done by creating two separate dummy lists, one for smaller elements and one for larger, then concatenating them.",
        "solution_code": "class ListNode:\n    def __init__(self, val=0, next=None):\n        self.val = val\n        self.next = next\n\ndef partition(head: ListNode, x: int) -> ListNode:\n    # Create two dummy nodes for the heads of the two partitions\n    less_head = ListNode(0)\n    greater_head = ListNode(0)\n    \n    less_ptr = less_head\n    greater_ptr = greater_head\n    \n    current = head\n    while current:\n        if current.val < x:\n            less_ptr.next = current\n            less_ptr = current\n        else:\n            greater_ptr.next = current\n            greater_ptr = current\n        current = current.next\n    \n    # Connect the end of the 'less' partition to the head of the 'greater' partition\n    less_ptr.next = greater_head.next\n    # Ensure the 'greater' partition ends properly\n    greater_ptr.next = None\n    \n    return less_head.next\n\n# Helper to convert list to linked list\ndef list_to_linkedlist(arr):\n    head = ListNode(0)\n    current = head\n    for val in arr:\n        current.next = ListNode(val)\n        current = current.next\n    return head.next\n\n# Helper to convert linked list to list\ndef linkedlist_to_list(head):\n    arr = []\n    current = head\n    while current:\n        arr.append(current.val)\n        current = current.next\n    return arr\n\n# Example Usage:\nhead1 = list_to_linkedlist([1,4,3,2,5,2])\nx1 = 3\nresult1 = partition(head1, x1)\nprint(f\"Partitioned List: {linkedlist_to_list(result1)}\")\n\nhead2 = list_to_linkedlist([2,1])\nx2 = 2\nresult2 = partition(head2, x2)\nprint(f\"Partitioned List: {linkedlist_to_list(result2)}\")",
        "solution_output": "Partitioned List: [1, 2, 2, 4, 3, 5]\nPartitioned List: [1, 2]"
    },
    {
        "id": 23,
        "title": "Word Search",
        "company": "Wipro",
        "difficulty": "Hard",
        "link": "#",
        "solution_explanation": "Given an `m x n` `board` of characters and a `word`, return `true` if the `word` exists in the grid. The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once. This is a backtracking (DFS) problem.",
        "solution_code": "def exist(board, word) -> bool:\n    rows, cols = len(board), len(board[0])\n    \n    def dfs(r, c, k): # k is the index in word we are trying to match\n        # Base cases\n        if k == len(word): # Found all characters of word\n            return True\n        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[k]:\n            return False # Out of bounds, or character mismatch\n            \n        original_char = board[r][c]\n        board[r][c] = '# ' # Mark as visited to prevent reuse\n        \n        # Explore neighbors\n        found = (dfs(r + 1, c, k + 1) or\n                 dfs(r - 1, c, k + 1) or\n                 dfs(r, c + 1, k + 1) or\n                 dfs(r, c - 1, k + 1))\n                 \n        board[r][c] = original_char # Backtrack: unmark the cell\n        return found\n\n    # Iterate through each cell as a potential starting point\n    for r in range(rows):\n        for c in range(cols):\n            if board[r][c] == word[0]:\n                if dfs(r, c, 0):\n                    return True\n    return False\n\nboard1 = [\n  [\"A\",\"B\",\"C\",\"E\"],\n  [\"S\",\"F\",\"C\",\"S\"],\n  [\"A\",\"D\",\"E\",\"E\"]\n]\nword1 = \"ABCCED\"\nprint(f\"Word '{word1}' exists: {exist(board1, word1)}\")\n\nboard2 = [\n  [\"A\",\"B\",\"C\",\"E\"],\n  [\"S\",\"F\",\"C\",\"S\"],\n  [\"A\",\"D\",\"E\",\"E\"]\n]\nword2 = \"SEE\"\nprint(f\"Word '{word2}' exists: {exist(board2, word2)}\")\n\nboard3 = [\n  [\"A\",\"B\",\"C\",\"E\"],\n  [\"S\",\"F\",\"C\",\"S\"],\n  [\"A\",\"D\",\"E\",\"E\"]\n]\nword3 = \"ABCB\"\nprint(f\"Word '{word3}' exists: {exist(board3, word3)}\")",
        "solution_output": "Word 'ABCCED' exists: True\nWord 'SEE' exists: True\nWord 'ABCB' exists: False"
    },
    {
        "id": 24,
        "title": "Unique Paths",
        "company": "Accenture",
        "difficulty": "Medium",
        "link": "#",
        "solution_explanation": "A robot is located at the top-left corner of a `m x n` grid. The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid. How many unique paths are there? This is a dynamic programming problem. Each cell's unique paths are the sum of paths from the cell directly above it and the cell directly to its left.",
        "solution_code": "def uniquePaths(m: int, n: int) -> int:\n    # Create a 2D DP table initialized with 1s (base case for first row/col)\n    dp = [[1] * n for _ in range(m)]\n    \n    # Fill the DP table\n    for r in range(1, m):\n        for c in range(1, n):\n            dp[r][c] = dp[r-1][c] + dp[r][c-1]\n            \n    return dp[m-1][n-1]\n\nprint(f\"Unique paths for 3x7 grid: {uniquePaths(3, 7)}\")\nprint(f\"Unique paths for 3x2 grid: {uniquePaths(3, 2)}\")",
        "solution_output": "Unique paths for 3x7 grid: 28\nUnique paths for 3x2 grid: 3"
    },
    {
        "id": 25,
        "title": "Climbing Stairs",
        "company": "Capgemini",
        "difficulty": "Easy",
        "link": "#",
        "solution_explanation": "You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top? This is a classic dynamic programming problem, essentially a variation of the Fibonacci sequence. The number of ways to reach step `n` is `ways(n-1) + ways(n-2)`.",
        "solution_code": "def climbStairs(n: int) -> int:\n    if n == 1: return 1\n    if n == 2: return 2\n\n    # dp[i] stores the number of ways to reach step i\n    dp = [0] * (n + 1)\n    dp[1] = 1\n    dp[2] = 2\n\n    for i in range(3, n + 1):\n        dp[i] = dp[i-1] + dp[i-2]\n\n    return dp[n]\n\nprint(f\"Ways to climb 2 stairs: {climbStairs(2)}\")\nprint(f\"Ways to climb 3 stairs: {climbStairs(3)}\")\nprint(f\"Ways to climb 4 stairs: {climbStairs(4)}\")",
        "solution_output": "Ways to climb 2 stairs: 2\nWays to climb 3 stairs: 3\nWays to climb 4 stairs: 5"
    },
    {
        "id": 26,
        "title": "Longest Palindromic Substring",
        "company": "TCS",
        "difficulty": "Hard",
        "link": "#",
        "solution_explanation": "Given a string `s`, return the longest palindromic substring in `s`. This can be solved using dynamic programming (O(N^2) time, O(N^2) space) or by expanding around the center (O(N^2) time, O(1) space). The expand around center method checks both odd and even length palindromes.",
        "solution_code": "def longestPalindrome(s: str) -> str:\n    if not s or len(s) < 1: return \"\"\n\n    start, end = 0, 0\n    \n    def expand_around_center(left, right):\n        while left >= 0 and right < len(s) and s[left] == s[right]:\n            left -= 1\n            right += 1\n        return left + 1, right - 1\n\n    for i in range(len(s)):\n        # Odd length palindromes (e.g., 'aba')\n        l1, r1 = expand_around_center(i, i)\n        # Even length palindromes (e.g., 'abba')\n        l2, r2 = expand_around_center(i, i + 1)\n        \n        if (r1 - l1) > (end - start):\n            start, end = l1, r1\n        if (r2 - l2) > (end - start):\n            start, end = l2, r2\n            \n    return s[start : end + 1]\n\nprint(f\"Longest Palindrome for 'babad': {longestPalindrome('babad')}\")\nprint(f\"Longest Palindrome for 'cbbd': {longestPalindrome('cbbd')}\")",
        "solution_output": "Longest Palindrome for 'babad': bab\nLongest Palindrome for 'cbbd': bb"
    },
    {
        "id": 27,
        "title": "Container With Most Water",
        "company": "Infosys",
        "difficulty": "Hard",
        "link": "#",
        "solution_explanation": "You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i`th line are `(i, 0)` and `(i, height[i])`. Find two such lines that, together with the x-axis, form a container that contains the most water. Return the maximum amount of water a container can store. Use a two-pointer approach, starting from both ends.",
        "solution_code": "def maxArea(height) -> int:\n    left = 0\n    right = len(height) - 1\n    max_water = 0\n    \n    while left < right:\n        # Calculate current area\n        current_height = min(height[left], height[right])\n        width = right - left\n        current_area = current_height * width\n        \n        max_water = max(max_water, current_area)\n        \n        # Move the pointer pointing to the shorter line\n        if height[left] < height[right]:\n            left += 1\n        else:\n            right -= 1\n            \n    return max_water\n\nprint(f\"Max water for [1,8,6,2,5,4,8,3,7]: {maxArea([1,8,6,2,5,4,8,3,7])}\")\nprint(f\"Max water for [1,1]: {maxArea([1,1])}\")",
        "solution_output": "Max water for [1,8,6,2,5,4,8,3,7]: 49\nMax water for [1,1]: 1"
    },
    {
        "id": 28,
        "title": "Three Sum",
        "company": "Wipro",
        "difficulty": "Hard",
        "link": "#",
        "solution_explanation": "Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`. Notice that the solution set must not contain duplicate triplets. A common approach involves sorting the array first, then using a two-pointer technique for the remaining two numbers after fixing one number.",
        "solution_code": "def threeSum(nums): # -> List[List[int]]:\n    nums.sort()\n    result = []\n    n = len(nums)\n    \n    for i in range(n - 2):\n        if i > 0 and nums[i] == nums[i-1]: # Skip duplicate for i\n            continue\n            \n        left, right = i + 1, n - 1\n        while left < right:\n            current_sum = nums[i] + nums[left] + nums[right]\n            \n            if current_sum < 0:\n                left += 1\n            elif current_sum > 0:\n                right -= 1\n            else: # current_sum == 0\n                result.append([nums[i], nums[left], nums[right]])\n                left += 1\n                right -= 1\n                \n                while left < right and nums[left] == nums[left - 1]: # Skip duplicate for left\n                    left += 1\n                while left < right and nums[right] == nums[right + 1]: # Skip duplicate for right\n                    right -= 1\n                    \n    return result\n\nprint(f\"Three sum for [-1,0,1,2,-1,-4]: {threeSum([-1,0,1,2,-1,-4])}\")\nprint(f\"Three sum for [0,1,1]: {threeSum([0,1,1])}\")",
        "solution_output": "Three sum for [-1,0,1,2,-1,-4]: [[-1, -1, 2], [-1, 0, 1]]\nThree sum for [0,1,1]: []"
    },
    {
        "id": 29,
        "title": "Generate Parentheses",
        "company": "Accenture",
        "difficulty": "Medium",
        "link": "#",
        "solution_explanation": "Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses. This is a classic backtracking problem. Use recursion and keep track of the number of open and close parentheses. Only add '(' if `open < n`, and only add ')' if `close < open`. Base case is when `open == close == n`.",
        "solution_code": "def generateParenthesis(n: int): # -> List[str]:\n    result = []\n    \n    def backtrack(current_string, open_count, close_count):\n        if len(current_string) == 2 * n:\n            result.append(current_string)\n            return\n            \n        if open_count < n:\n            backtrack(current_string + '(', open_count + 1, close_count)\n            \n        if close_count < open_count:\n            backtrack(current_string + ')', open_count, close_count + 1)\n            \n    backtrack(\"\", 0, 0)\n    return result\n\nprint(f\"Generate parentheses for n=3: {generateParenthesis(3)}\")\nprint(f\"Generate parentheses for n=1: {generateParenthesis(1)}\")",
        "solution_output": "Generate parentheses for n=3: ['((()))', '(()())', '(())()', '()(())', '()()()']\nGenerate parentheses for n=1: ['()']"
    },
    {
        "id": 30,
        "title": "Search in Rotated Sorted Array",
        "company": "Capgemini",
        "difficulty": "Medium",
        "link": "#",
        "solution_explanation": "Given a sorted array `nums` that has been rotated at some pivot unknown to you beforehand, and a `target` value, search if `target` is in the array. Return its index, otherwise return -1. This can be solved with a modified binary search algorithm (O(log n)). The key is to determine which half is sorted and whether the target lies within that sorted half.",
        "solution_code": "def search(nums, target) -> int:\n    left, right = 0, len(nums) - 1\n    \n    while left <= right:\n        mid = (left + right) // 2\n        \n        if nums[mid] == target:\n            return mid\n            \n        # Determine if the left half is sorted\n        if nums[left] <= nums[mid]: \n            if nums[left] <= target < nums[mid]: # Target is in the sorted left half\n                right = mid - 1\n            else:\n                left = mid + 1 # Target is in the unsorted right half\n        \n        # Else, the right half must be sorted\n        else: \n            if nums[mid] < target <= nums[right]: # Target is in the sorted right half\n                left = mid + 1\n            else:\n                right = mid - 1 # Target is in the unsorted left half\n                \n    return -1\n\nprint(f\"Index of 0 in [4,5,6,7,0,1,2]: {search([4,5,6,7,0,1,2], 0)}\")\nprint(f\"Index of 3 in [4,5,6,7,0,1,2]: {search([4,5,6,7,0,1,2], 3)}\")",
        "solution_output": "Index of 0 in [4,5,6,7,0,1,2]: 4\nIndex of 3 in [4,5,6,7,0,1,2]: -1"
    }
]