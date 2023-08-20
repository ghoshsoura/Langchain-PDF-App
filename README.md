# Langchain-PDF-App
A chatgpt PDF app which will be used to detect and generate response from any PDF file.
# Requirements to build this App:

langchain==0.0.154 


PyPDF2==3.0.01


python-dotenv==1.0.0


streamlit==1.18.1


faiss-cpu==1.7.4


streamlit-extras

# Note:-

I build this app upto this stage, after this could not be able to proceed because of the API keys issues. As faiss-cpu is included in the main file which is used in

intergration with OpeanAI embeddings, there should be added a an OpenAI API keys which will act as providing chatgpt services and will embed that into our app. But 

everytime I try to check whether the file is detected or not I get a error message that says your current billing is exceeded its limit, renew your plan. It's 

because of the API permission is only permitted if you are using a premimum service in your openAI account. Unfortunately due to this issue, I was not able to 

proceed further in this project but till this phase everything seems perfect. 
