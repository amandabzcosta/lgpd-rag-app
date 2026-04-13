# Assistente LGPD - RAG

O **Assistente LGPD** é um app de IA baseado na arquitetura **RAG** (Retrieval-Augmented Generation). O seguinte projeto foi desenvolvido para atuar como um assistente na Lei Geral de Proteção de Dados (LGPD) do Brasil, respondendo a dúvidas de interesse do mercado com alta precisão e baseando-se apenas no texto oficial da lei.

**[Acesse o aplicativo por aqui!](<https://lgpd-rag-app.streamlit.app/>)**

---

## Funcionalidades

* Foi configurado com temperatura `0`, garantindo que a IA não invente informações, baseando-se 100% no contexto do documento fornecido.
* A cada resposta gerada, o assistente informa as páginas exatas do doc original que foram consultadas para estruturar o output.
* Utiliza a LPU do Groq rodando o modelo Llama 3 da Meta, garantindo inferências em milissegundos.
* Implementação de tela de login utilizando o cofre de secrets do Streamlit (st.secrets) para proteger o uso da solução.
* Interface de chat interativa tem memória do histórico da conversa durante a sessão (via `st.session_state`).

---

## Tecnologias Utilizadas

O projeto foi construído utilizando um ecossistema de IA em Python:

* **[Streamlit](https://streamlit.io/):** Criação do Front-end.
* **[LangChain](https://www.langchain.com/):** Gestão do pipeline RAG, divisão de textos e chain de perguntas e respostas.
* **[Groq (Llama 3.3 70B))](https://aistudio.google.com/):** LLM open source focado em alta velocidade e raciocínio lógico para estruturar as respostas.
* **[HuggingFace Embeddings](https://huggingface.co/):** Modelo transformer `all-MiniLM-L6-v2` para conversão de texto em vetores.
* **[ChromaDB](https://www.trychroma.com/):** Banco de dados vetorial operando em memória para recuperação dos chunks da lei.
* **[PyMuPDF](https://pymupdf.readthedocs.io/):** Extração dos textos do documento PDF oficial.

---

## Estrutura do Projeto

```text
├── app.py                                    # Código main do app e interface
├── requirements.txt                          # Lista de dependências e bibliotecas
├── Lei_geral_protecao_dados_pessoais_1ed.pdf # Knowledge Base
└── README.md                                 # Documentação


