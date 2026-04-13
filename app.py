import streamlit as st
import os
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.chains import create_retrieval_chain

st.set_page_config(page_title="Assistente LGPD", page_icon="⚖️", layout="centered")
if "autenticado" not in st.session_state:
    st.session_state.autenticado = False

if not st.session_state.autenticado:
    user_password = st.text_input("Digite a senha de acesso:", type="password")
    
    if user_password: 
        if user_password == st.secrets["ACCESS_PASSWORD"]:
            st.session_state.autenticado = True
            st.rerun() 
        else:
            st.error("Senha incorreta. Tente novamente.")
    st.stop()

st.title("⚖️ Assistente LGPD")
st.write("Faça perguntas sobre a Lei Geral de Proteção de Dados.")

try:
    os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]
except KeyError:
    st.error("Chave de API não encontrada.")
    st.stop()

@st.cache_resource(show_spinner="Processando o documento LGPD...")
def load_rag_pipeline():
    file = "Lei_geral_protecao_dados_pessoais_1ed.pdf"
    
    if not os.path.exists(file):
        st.error(f"Arquivo {file} não encontrado.")
        st.stop()

    loader = PyMuPDFLoader(file)
    docs = loader.load()
    text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=1000, chunk_overlap=200
    )
    texts = text_splitter.split_documents(docs)
    
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_store = Chroma.from_documents(
        documents=texts,
        embedding=embeddings,
    )
    
    model = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash-lite",
        temperature=0,  
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system","Você é um assistente da LGPD. Use o seguinte contexto para responder: {context}"),
        ("human", "{input}"),
    ])
    
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})
    question_answer_chain = create_stuff_documents_chain(model, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)
    
    return rag_chain

rag_chain = load_rag_pipeline()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if question := st.chat_input("Digite sua dúvida sobre a LGPD..."):
    
    with st.chat_message("user"):
        st.markdown(question)
    st.session_state.messages.append({"role": "user", "content": question})

    with st.chat_message("assistant"):
        with st.spinner("Buscando na lei e formulando resposta..."):
            try:
                response = rag_chain.invoke({"input": question})
                answer = response["answer"]
                docs_used = response["context"] 
                
                pages = set() 
                for doc in docs_used:
                    if "page" in doc.metadata:
                        pages.add(doc.metadata["page"] + 1)
                
                text_pages = ", ".join(str(p) for p in sorted(pages))
                final_answer = f"{answer}\n\n---\n***Fonte consultada:** Página(s) {text_pages} da LGPD.*"
                
                st.markdown(final_answer)
                st.session_state.messages.append({"role": "assistant", "content": final_answer})
                
            except Exception as e:
                st.error(f"Ocorreu um erro ao processar sua pergunta: {e}")
