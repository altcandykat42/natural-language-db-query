from dotenv import load_dotenv
import os
from groq import Groq

load_dotenv()

# Initialize the Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
def generate_query(query):
    prompt = f"""
    You are an SQL expert. DONT MAKE INCORRECT QUERIES & return "CANNOT EXECUTE QUERY" if you are unsure.Convert the following natural language query into an SQL query.
    The database schema is as follows:
    
    Table: Employees
    - ID (INTEGER, Primary Key)
    - Name (TEXT)
    - Department (TEXT)
    - Salary (REAL)
    - Hire_Date (TEXT)
    
    Table: Departments
    - ID (INTEGER, Primary Key)
    - Name (TEXT)
    - Manager (TEXT)

    Convert this natural language request into an SQL query:
    
    "{query}"

    DONT USE attributes outside schema, if no query can be generated return "CANNOT EXECUTE QUERY"
    Only return the SQL query without any explanation in a single line.
    """
    chat_completion = client.chat.completions.create(
    messages=[
        {"role": "user", "content": prompt}
    ],
    model="llama3-8b-8192",
)
    return chat_completion.choices[0].message.content

# print(generate_query("Total salary of employees with name starting with A"))