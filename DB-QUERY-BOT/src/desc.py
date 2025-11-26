from dotenv import load_dotenv
import os
from groq import Groq

load_dotenv()

# Initialize the Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
def generate_desc(query, result):
    if result == []:
        prompt = "THE SQL QUERY WAS UNSUCCESSFUL. Ask them to ask a different question. RETURN JUST THE MESSAGE."
        chat_completion = client.chat.completions.create(
        messages=[
            {"role": "user", "content": prompt}
        ],
        model="llama3-8b-8192",
)   
        return chat_completion.choices[0].message.content   
    else:
        prompt = f"""
        User query : {query}
        SQL Query result : {result}
        Provide summary(interpretation of the query result) in a paragraph. NO NEED TO EXPLAIN QUERY.
        """
        chat_completion = client.chat.completions.create(
        messages=[
            {"role": "user", "content": prompt}
        ],
        model="llama3-8b-8192",
    )   
        return chat_completion.choices[0].message.content
