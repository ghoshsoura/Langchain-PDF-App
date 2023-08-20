import streamlit as st
import pickle
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from streamlit_extras.add_vertical_space import add_vertical_space
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

with st.sidebar:
    st.title('🤗💬 LLM Chat App')
    st.markdown('''
    ## About
    This app is an LLM-powered chatbot built using:
    - [Streamlit](https://streamlit.io/)
    - [LangChain](https://python.langchain.com/)
    - [OpenAI](https://platform.openai.com/docs/models) LLM model
 
    ''')
    add_vertical_space(5)
    st.write('Made with ❤️ by Souradeep Ghosh')

load_dotenv()

def main():
    st.header("chat with pdf 💬")

    

    pdf=st.file_uploader("upload your pdf",type='pdf')

    st.write(pdf.name)

    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        
        text_split = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunks = text_split.split_text(text=text)

        embeddings = OpenAIEmbeddings()

        vectorst = FAISS.from_texts(chunks,embedding=embeddings)
        last_idx = pdf.name[:-4]

        with open(f"{last_idx}.pkl","wb") as f:
            pickle.dump(vectorst,f)


if __name__=='__main__':
    main()
