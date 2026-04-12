# Assistente LGPD - RAG

O **Assistente LGPD** é uma aplicação de IA baseada na arquitetura **RAG** (Retrieval-Augmented Generation). Este projeto foi desenvolvido para atuar como um assistente na Lei Geral de Proteção de Dados (LGPD) do Brasil, respondendo a dúvidas com alta precisão e baseando-se apenas no texto oficial da lei.

**[Acesse o aplicativo por aqui!](<https://lgpd-rag-app.streamlit.app/>)**

---

## Funcionalidades

* Utiliza banco de dados vetorial para encontrar os trechos exatos da lei que respondem à pergunta do usuário.
* Configurado com temperatura `0`, garantindo que a IA não invente informações, baseando-se 100% no contexto do documento fornecido.
* Interface de chat interativa que lembra o histórico da conversa durante a sessão (via `st.session_state`).
* Leitura e vetorização do documento em cache para garantir respostas rápidas e baixo consumo de recursos na nuvem.

---

## Tecnologias Utilizadas

O projeto foi construído utilizando um ecossistema de IA em Python:

* **[Streamlit](https://streamlit.io/):** Criação do Front-end interativo.
* **[LangChain](https://www.langchain.com/):** Gestão do pipeline RAG, divisão de textos e cadeias de perguntas e respostas.
* **[Google Gemini (Flash Lite)](https://aistudio.google.com/):** Modelo de Linguagem Grande (LLM) utilizado para estruturar as respostas.
* **[HuggingFace Embeddings](https://huggingface.co/):** Modelo `all-MiniLM-L6-v2` para conversão de texto em vetores.
* **[ChromaDB](https://www.trychroma.com/):** Banco de dados vetorial operando em memória para recuperação dos chunks da lei.
* **[PyMuPDF](https://pymupdf.readthedocs.io/):** Extração dos textos do documento PDF oficial.

---

## Estrutura do Projeto

```text
├── app.py                                    # Código principal da aplicação e interface
├── requirements.txt                          # Lista de dependências e bibliotecas
├── Lei_geral_protecao_dados_pessoais_1ed.pdf # Knowledge Base
└── README.md                                 # Documentação do projeto


