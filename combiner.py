from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

import asyncio
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os


load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv('GROQ_API_KEY')

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.2,
    max_tokens=None,
    timeout=None
)
def combiner(outputs):
    system_message = """You are an expert summarization master. Your task is to generate a single, concise, and coherent summary of an entire call. You will receive multiple summaries—each representing key points from different chunks of the call. Your final output should:
Integrate Information: Combine the insights from all provided summaries into one unified narrative.
Highlight Key Elements: Clearly state the overall purpose, major topics discussed, key decisions made, and any important action items or conclusions.
Eliminate Redundancy: Avoid repeating details; focus on the most relevant information.
Maintain Clarity: Ensure that the summary is well-organized, easy to understand, and reflects the overall essence of the call.
Generate a succinct, informative summary that captures the complete context of the conversation without referencing the individual summaries."""
    human_message= "Summarize this: {subject}"
    prompt = ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template(system_message),
        HumanMessagePromptTemplate.from_template(human_message)
    ])

    chain = prompt | llm
    summaries = "SUMMARIZED CHUNKS(IN ORDER) FROM THE SAME CALL TRANSCRIPT:"
    i=1
    for output in outputs:
        summaries += f'\nSummary {i}:\n'+output.content
        i += 1
    summaries += '\nGENERATE A COMPLETE SHORT, CONCISE SUMMARY WITH ALL IMPORTANT INFORMATION:'
    # return summaries
    return chain.invoke({'subject':summaries}).content