from services.vectorstore_service import load_vectorstore
from services.llm_service import get_llm


def generate_rag_response(user_query):

    llm = get_llm()

    # 🔹 Handle Greetings First (No RAG Needed)
    if user_query.lower().strip() in ["hi", "hello", "hii", "hey"]:
        return "Hello! 👋 How can I assist you with brand–influencer collaboration today?"

    # 🔹 Load Vector Store
    vectorstore = load_vectorstore()
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    docs = retriever.get_relevant_documents(user_query)

    # 🔹 If no relevant docs found → normal LLM response
    if not docs:
        return llm.invoke(user_query)

    # 🔹 Build Context from Retrieved Docs
    context = "\n\n".join([doc.page_content for doc in docs])

    # 🔹 Build Final Prompt
    prompt = f"""
    You are an AI assistant helping brands and influencers communicate professionally.

    Use the provided context to answer the user clearly and professionally.

    Context:
    {context}

    User Question:
    {user_query}

    Provide a structured and helpful response.
    """

    # 🔹 Generate Final Answer
    response = llm.invoke(prompt)

    return response