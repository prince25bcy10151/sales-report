# 🛍️ Sales Management System (SMS)

## **Project Title**
**Sales Management System (SMS)**

---

## **Project Overview**

The Sales Management System (SMS) is a **lightweight, console-based application** built entirely in Python. [cite_start]It is designed to assist small retail businesses, boutiques, or temporary sales counters with basic inventory control and sales tracking. [cite: 5]

[cite_start]The primary goal is to provide an efficient, automated method for recording sales, ensuring accurate stock levels, and generating immediate low-stock alerts, replacing manual tracking methods[cite: 8, 11, 12].

---

## **Key Features**

[cite_start]The system provides the following major functional modules[cite: 21]:

### **1. [cite_start]Inventory Management (Data Input & Processing) [cite: 26]**
* [cite_start]**Product Addition (CRUD):** Allows users to easily add new products with initial stock, unit price, and a set minimum stock warning limit[cite: 29].
* **Automatic Stock Update:** Stock quantity is automatically reduced immediately after every successful sale transaction.

### **2. Transaction Processing**
* [cite_start]**Sale Recording (Clear Input/Output):** Processes sales by calculating the total amount and ensuring sufficient stock is available[cite: 22].
* **Transaction Logging:** Records detailed sales entries, including the product name, quantity sold, and calculated total bill amount.

### **3. [cite_start]Alerting & Reporting (Analytics) [cite: 28]**
* **Low Stock Alerts:** Provides **instantaneous alerts** if a product's current stock drops to or below its minimum threshold.
* **Sales Summary Report:** Generates a clear, consolidated report of all recorded sales transactions.

---

## **Technologies/Tools Used**

| Category | Technology/Tool | Purpose |
| :--- | :--- | :--- |
| **Programming Language** | Python 3.x | Core implementation language. |
| **IDE** | VS Code / PyCharm | Development and debugging environment. |
| **Modules Used** | `json`, `os`, `time`, `random` | Utility functions for data handling, system interaction, timing, and generating unique IDs. |
| **Version Control** | Git / GitHub | [cite_start]Used for managing source code, collaboration, and submission[cite: 55, 84]. |

---

## **Steps to Install & Run the Project**

This project is console-based and requires a standard Python environment.

### **1. Prerequisites**
Ensure you have **Python 3.x** installed on your machine.

### **2. Clone the Repository**
```bash
# Clone the repository from GitHub
git clone [YOUR_GITHUB_REPO_LINK_HERE]
cd SalesManagementSystem