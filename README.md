# Python Web & API Automation Testing Framework with AI-Assisted Analysis

A professional, enterprise-grade test automation repository designed to showcase modern QA engineering practices. This project implements comprehensive Web UI and API testing using a clean, scalable design pattern, integrated with state-of-the-art Generative AI for automated failure analysis.

---

## 🛠️ Tech Stack

- **Core Language**: Python 3.11+
- **Web UI Automation**: [Playwright](https://playwright.dev/python/) (Sync API)
- **Test Runner & Framework**: [Pytest](https://docs.pytest.org/)
- **API Testing**: [Requests](https://requests.readthedocs.io/)
- **AI Diagnostics**: [Google GenAI SDK](https://github.com/google/generative-ai-python) (`gemini-2.5-flash`)
- **CI/CD**: GitHub Actions

---

## 📐 Architecture & Features

### 1. Page Object Model (POM)
The Web UI testing suite is structured using the **Page Object Model (POM)** pattern to ensure high maintainability, reusability, and separation of concerns.
- **`pages/`**: Contains page objects encapsulating locators and interaction logic.
  - `LoginPage`: Houses username/password fields, submission, and error elements for [SauceDemo](https://www.saucedemo.com).
  - `InventoryPage`: Encapsulates products list, add-to-cart operations, and cart status badges.
- **`tests/`**: Contains test cases separate from selectors, enhancing readability.

### 2. API Testing Integration
A robust test suite targeting public API endpoints ([ReqRes](https://reqres.in)):
- Verifies POST payload delivery and authentication token returns.
- Validates GET response payloads, structure conformity, and non-empty records.

### 3. AI-Assisted Test Analysis
Leveraging the power of **Gemini 2.5 Flash**, the framework includes an automated failure diagnostics utility in `utils/ai_analyzer.py`.
- When a test fails, its execution stack trace is processed by Gemini.
- The model analyzes the error logs to produce a **Root Cause Analysis (RCA)** and concrete fix suggestions in under 3 concise sentences.

### 4. Smart CI/CD Adaptation
The framework intelligently detects execution environments:
- **Local Runs**: Launches in `headed` mode for live execution visibility.
- **CI Environments (GitHub Actions)**: Automatically switches to `headless` execution to run efficiently in virtual environments without a display buffer.

---

## 📂 Directory Structure

```text
miniProject/
│
├── .github/
│   └── workflows/
│       └── test.yml         # GitHub Actions CI workflow config
│
├── pages/
│   ├── login_page.py        # LoginPage POM implementation
│   └── inventory_page.py    # InventoryPage POM implementation
│
├── tests/
│   ├── conftest.py          # Global configurations & headed/headless fixtures
│   ├── test_web_ui.py       # Web UI test cases (SauceDemo)
│   └── test_api.py          # API test cases (ReqRes)
│
├── utils/
│   └── ai_analyzer.py       # Gemini AI-assisted error analyzer
│
├── requirements.txt         # Project dependencies
└── README.md                # Documentation
```

---

## 🚀 Getting Started Locally

### Prerequisites
- Python 3.11+ installed.
- (Optional) A `GEMINI_API_KEY` for AI-assisted failure diagnostics.

### 1. Clone & Navigate to Project
```powershell
git clone <your-repo-url>
cd miniProject
```

### 2. Set Up Virtual Environment
On Windows (PowerShell):
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies
```powershell
pip install -r requirements.txt
playwright install chromium
```

### 4. Run the Test Suite
To run all tests (Web UI and API) locally:
```powershell
pytest -v
```

---

## 🤖 Running AI Failure Analysis

To utilize the AI diagnostics feature, provide your Gemini API key:

**Windows (PowerShell)**:
```powershell
$env:GEMINI_API_KEY="your_api_key_here"
```

**Linux/macOS**:
```bash
export GEMINI_API_KEY="your_api_key_here"
```

---

## 🔄 CI/CD Workflow
This repository is fully integrated with **GitHub Actions** (`.github/workflows/test.yml`). Every `push` and `pull_request` to the `main` branch triggers:
1. Virtual environment setup with Python 3.11.
2. Fast caching and installation of all required dependencies.
3. System-level Playwright driver initialization.
4. Complete test execution in an optimized headless execution block.
