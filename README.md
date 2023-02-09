# Testing tool
This is a tool to help applicants test their own APIs before submission.

# Usage
Make sure you have [python](https://www.python.org/downloads/) installed.

1. Clone the repository onto your machine.
```bash
git clone https://github.com/dyte-submissions/vit-hiring-2023-phase1-test.git
cd vit-hiring-2023-phase1-test
```

2. Set up a virtual environment
```bash
python3 -m venv venv
source ./venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Replace base URL in `main.py` with your own
```diff
 import requests
 from data import SLOTS, FACULTIES, COURSES, REGISTER_COURSES
 
-API_BASE = 'http://localhost:3000'
+API_BASE = 'http://localhost:4000/api/v1'
 STUDENT_AUTH_TOKEN = 'ENTER STUDENT AUTH TOKEN HERE'
 ADMIN_AUTH_TOKEN = 'ENTER ADMIN AUTH TOKEN HERE'
```

5. Run the test tool
```bash
python main.py
```