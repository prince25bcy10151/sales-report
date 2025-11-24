#  Project Statement

## **Project Title: Sales Management System**

### **1. Problem Statement **

Small-scale retail operations, such as local shops, boutiques, and temporary sales counters, often struggle with inefficient and manual methods (like notebooks or basic spreadsheets) for managing their inventory and recording sales. This leads to frequent stock errors, delayed low-stock alerts, and difficulty in generating quick sales summaries. The core problem is the lack of a **simple, lightweight, and automated system** for real-time inventory tracking and immediate sales logging, aligned with the concepts covered in the subject syllabus.

---

### **2. Scope of the Project **

The project scope is limited to a **console-based, in-memory system** developed using Python. It focuses on the core functionalities of inventory management and sales logging for a single point of sale.

The system will:
* Maintain a dictionary-based inventory data structure.
* Allow the addition of new products with key details (name, price, stock, min-limit).
* Process sales transactions by updating stock and logging the sale record.
* Provide immediate low-stock notifications.
* Generate a final sales summary report.

**Exclusions:** The current scope **excludes** features requiring data persistence (no database/file saving), graphical user interfaces (GUI), and user authentication.

---

### **3. Target Users **

The primary target users are individuals or small businesses needing a basic digital solution for retail management:

* **Small Shop Owners:** Local vendors needing to track daily stock and sales.
* **Boutique Managers:** Requiring inventory visibility and pricing control.
* **Temporary Retail Counters:** Users who need a fast, simple logging system for events or pop-up sales.

---

### **4. High-Level Features**

The system provides three major functional modules:

1.  **Inventory Management:** Features for adding products and maintaining stock levels.(Relates to Data input & processing and CRUD operations).
2.  **Transaction Processing:** Features to record a sale, calculate the total bill, and reduce stock instantly. (Involves a Clear input/output structure).

3.  **Alerting & Reporting:** Features including automatic low-stock alerts and the generation of a detailed sales summary report. (Relates to Reporting or analytics).

