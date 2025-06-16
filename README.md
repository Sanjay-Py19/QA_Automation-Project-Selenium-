# 🧪 Selenium WebDriver Automation Project (Python + BDD Framework)

## 📋 Project Overview

This is a web automation framework built using **Python**, **Selenium WebDriver**, and **Behave** (Cucumber-style BDD).
---

## 🧰 Tech Stack

- **Language**: Python 3.9.11
- **Automation Tool**: Selenium WebDriver  
- **BDD Framework**: Behave  
- **Test Runner**: Behave CLI  
- **Reports**: Allure / HTML reports (optional)  
- **IDE**: PyCharm / VSCode  
- **Version Control**: Git

---

## 📁 Project Structure

```
project-root/
│
├── features/
│   ├── steps/                  # Step definitions
│   ├── pages/                  # Page Object classes
│   ├── environment.py          # Hooks (before/after scenario)
│   ├── configs/                # Config files (like config.yaml or .env)
│   ├── login.feature           # Sample feature file
│
├── drivers/                    # WebDriver executables (e.g., chromedriver)
├── reports/                    # Test execution reports
├── requirements.txt            # Project dependencies
├── behave.ini                  # Behave configuration
└── README.md                   # Project documentation
```

---

## ✅ Prerequisites

- Python 3.7+
- pip (Python package manager)
- Chrome / Firefox browser
- Git

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Create Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run Tests

```bash
behave
```

You can also run specific features:

```bash
behave features/login.feature
```

---

## 📈 Reports (Optional)

To generate HTML or Allure reports, integrate with third-party plugins. For example:

```bash
behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results .
```

Then view the report:

```bash
allure serve reports/allure-results
```

---

## 📝 Sample Gherkin Scenario

```gherkin
Feature: Login functionality

  Scenario: Successful login with valid credentials
    Given the user is on the login page
    When the user enters valid credentials
    Then the user should be redirected to the dashboard
```

---

## 🔧 Configuration

You can store environment settings like URL, browser type, etc., in a `.env` or `config.yaml` file and load them in `environment.py`.

---

## 👨‍💻 Author

**Sanjay Rawat**  
SDET | QA Automation Engineer | Selenium | UFT| Python | Automation Frameworks | API Testing

---
