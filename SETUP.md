# **Project Setup Guide**

## **Prerequisites to run this project**

Before you begin, ensure you have the following software installed on your system:

- **VS Code** (recommended) https://code.visualstudio.com/
- **Python** (version 3.11.6) https://www.python.org/downloads/release/python-3116/
- **Git** https://git-scm.com/downloads
- **MySQL**(version 8.) https://dev.mysql.com/downloads/installer/

### **Step 1: Clone the Repository**

1. Open up Vs Code and Clone the repository to your local machine

```cmd
git clone https://github.com/GregTakacsGergo/images-db-ui.git
```
2. Open the new folder (IMAGES-DB-UI)

### **Step 2: Create a virtual environment**

```bash
.venv\Scripts\activate
```

### **Step 3: Install dependencies**

```bash
pip install -r requirements.txt
```

### **Step 4: Set up MySQL connection**

1. Open your downloaded MySQL Workbench
2. Turn on the server if not turned on automatically (usually 127.0.0.1 and port: 3306 )
3. Ceate new schema
4. Configure db_config.py with your connection params
5. Create your config.py file ```DB_PASSWORD = "YOUR_pswd_123"```

### **Step 5: Run image_insert_read_ver3.py**

Please go through the README!

#### **Troubleshooting**

1. If dependency issues arise, try to ```pip install -r requirements_long.txt``` and take a long coffee
