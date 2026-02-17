# 🧠 Databricks SQL AI Agent using LangChain

This project builds an AI-powered SQL Agent that connects to Databricks and allows users to ask questions in natural language.

### The agent automatically:
-------------------------------------------------------------------------
- Converts user questions into SQL queries
- Executes them on Databricks
- Returns clear, human-readable answers
- This helps automate data analysis and reduces manual SQL writing.

### 🚀 Technologies Used
--------------------------------------------------------------------------  
- Python
- LangChain
- OpenAI (gpt-4o-mini)
- SQLAlchemy
- Databricks SQL Connector
- dotenv

### ⚙️ How It Works
---------------------------------------------------------------------------

- Connects to Databricks using credentials stored in a .env file
- Creates a SQLDatabase object using SQLAlchemy
- Uses OpenAI LLM via LangChain
- Creates a SQL Agent
- Accepts user questions in natural language
- Converts question → SQL → Executes → Returns answer


### 🎯 Purpose of the Project
----------------------------------------------------------------------------
- Automates SQL query generation
- Reduces manual work for analysts
- Makes data accessible to non-technical users
- Demonstrates real-world AI + Database integration
- Improves productivity using LLM-powered automation

### 💡 Example Use Case
----------------------------------------------------------------------------

- Instead of writing:

SELECT SUM(sales) FROM sales_table;

- You simply ask:

"What is the total sales?"

The AI handles everything automatically.


### 📈 Future Improvements
----------------------------------------------------------------------------
- Add memory support
- Add Streamlit UI
- Add logging & error handling
- Deploy as web app
- Add role-based query control

## 👨‍💻 Author
Jayachandra
