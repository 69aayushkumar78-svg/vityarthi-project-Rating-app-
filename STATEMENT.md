Create a file named `STATEMENT.md` (Project Problem Statement & Specification) in your project folder and paste the following content:

```markdown
# Problem Statement & System Requirements Specification

## 1. Project Title
**Command-Line Product Rating and Feedback System**

---

## 2. Problem Statement
Businesses need a straightforward mechanism to collect feedback on products across specific metrics (such as value for money, quality, and support) rather than a simple single-rating score. Existing full-fledged GUI applications can be resource-heavy or overly complex for simple deployment scenarios. 

There is a requirement for a lightweight, command-line interface (CLI) application that securely separates administrative actions (adding products, viewing detailed analytics, updating credentials) from customer interactions (providing feedback with basic identity details), while retaining data locally across sessions.

---

## 3. Core Objectives
- **Authentication & Security:** Provide prompt-based initial credential creation for Administrators without hardcoded default passwords.
- **Product Management:** Enable Administrators to dynamic add products to the system.
- **Granular Feedback:** Allow users to submit detailed ratings across three distinct parameters:
  1. Worth of Money (1–5 scale)
  2. Product Quality (1–5 scale)
  3. Customer Support (1–5 scale)
- **Analytics Display:** Provide Administrators with calculated averages for each category along with individual review logs.
- **Persistence:** Ensure all product data, customer reviews, and admin credentials persist locally in JSON format without external database dependencies.

---

## 4. Functional Requirements

### 4.1 Administrator Module
- **First-Run Configuration:** Prompt for creation of Admin ID and Password if system data file is absent.
- **Authentication:** Restrict administrative features to validated ID and Password.
- **Product Operations:** Add new product records with empty rating lists.
- **Analytics & Reporting:** Display total reviews count, average score for each rating parameter, and individual user ratings alongside user details (Name, Email).
- **Credential Management:** Allow updating existing Admin ID and Password.

### 4.2 User Module
- **Identification:** Capture user's Name and Email prior to rating.
- **Product Selection:** Display a list of available products for selection.
- **Rating Collection:** Collect numerical input between 1.0 and 5.0 for each evaluation metric with input validation.

### 4.3 Data Management Module
- **File Input/Output:** Read and write system state to `app_data.json`.
- **Error Handling:** Gracefully handle missing data files, non-numeric ratings, and out-of-range rating entries.

---

## 5. Non-Functional Requirements
- **Usability:** Clean menu-driven interface executable from standard CLI environments.
- **Zero Configuration:** No external database engine or third-party Python packages required.
- **Maintainability:** Modular functions separating Data Layer, Admin Workflow, User Workflow, and Main Navigation Loop.