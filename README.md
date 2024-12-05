# Blog CMS Automation Testing Framework

This project is an automation testing framework for a Blog Content Management System (CMS). It includes tests for both the UI and API of the blog platform, ensuring functionality such as creating, viewing, updating, and deleting blog posts.

## Features
- **UI Testing**: Automated tests using Selenium for web-based interactions with the CMS.
- **API Testing**: Tests using `requests` to interact with the backend API endpoints.
- **Database Validation**: Checks to ensure that posts are correctly stored in the database.
- **CI/CD**: Integrated with GitHub Actions to run tests automatically with every push.

## Requirements
1. Python 3.x
2. Selenium WebDriver (ChromeDriver, Firefox, etc.)
3. pytest
4. requests

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Ggogua/Sevtest.git
   cd blog-cms-automation-testing

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
------------------------------------
pip install -r requirements.txt
------------------------------------
pytest tests/



