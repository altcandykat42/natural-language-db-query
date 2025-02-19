from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from splitter import split_transcript
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()


os.environ["GROQ_API_KEY"] = os.getenv('GROQ_API_KEY')

# chunks = split_transcript()
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.2,
    max_tokens=100,
    timeout=None
)

async def summarizer(input):
    chunks = split_transcript(input,chunk_size=1000,chunk_overlap=50)
    print('Total Chunks:', len(chunks))
    # print(type(chunks[0]))
    #messages
    system_message = 'You are master of generating SHORT, concise, accurate and informative summaries of call transcripts.'
    human_message = 'Summarize this(CONCISE, SHORT, INFORMATIVE): {subject}'

    prompt = ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template(system_message),
        HumanMessagePromptTemplate.from_template(human_message)
    ])

    chain = prompt | llm
    # output = chain.invoke({'subject': chunks[0]})
    tasks = [chain.ainvoke({'subject':chunk}) for chunk in chunks]
    output = await asyncio.gather(*tasks)
    return [output,chunks]

