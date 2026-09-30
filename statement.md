# Problem Statement & Project Scope

## 1. Problem Statement
Hostel-residing college students typically manage strict monthly allowances while navigating varied, frequent daily micro-transactions such as mess charges, canteen snacks, printing, hygiene products, and local travel. Lacking simple and lightweight personal finance management tools, students frequently default to informal paper logs or complex mobile applications that demand persistent internet connectivity, user registration, and bloated permissions. This leads to poor expenditure tracking, unchecked spending, and budget deficits before month-end.

## 2. Scope of the Project
The **Hostel Expense Tracker** is a modular, standalone CLI utility designed to offer zero-friction personal financial tracking for students:
- **Scope Inclusions:**
  - Recording daily transactions with monetary value, predefined category tagging, short descriptions, and timestamps.
  - Category-based filtering, itemized inspections, and cumulative expenditure summaries.
  - Dynamic monthly budget thresholds with real-time overspending alerts.
  - Flat-file persistence using structured CSV/delimited storage without requiring external database engines.
  - Standard error handling and validation for console inputs.
- **Scope Exclusions:**
  - Multi-user authentication and concurrent cloud synchronization.
  - Multi-currency conversions and automated bank API integrations.
  - Graphical or mobile front-ends.

## 3. Target Users
- College and university students residing in hostels/dorms.
- Budget-conscious individuals seeking a local, distraction-free expense logging utility.
- Students without access to reliable internet connectivity who require a lightweight offline tool.

## 4. High-Level Features
- **Transaction Management:** Add, list, view, and delete individual expense records.
- **Category-Based Organization:** Restrict expense tagging to hosteler-specific categories (`Food`, `Stationery`, `Hygiene`, `Daily Needs`, `Travel`, `Entertainment`, `Medical`, `Other`).
- **Financial Analytics & Budgeting:** Instant calculation of gross spending, category-wise breakdown totals, and monthly budget limit checks with deficit calculations.
- **Automatic File Persistence:** Non-volatile file I/O operations (`expenses.txt`) to restore and serialize records between execution sessions.