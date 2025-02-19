from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_transcript(transcript, chunk_size=1000, chunk_overlap=100):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,  
        chunk_overlap=chunk_overlap
    )
    return text_splitter.split_text(transcript)
