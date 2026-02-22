from services.llm_service import get_llm

def summarize_text(text):

    llm = get_llm()

    prompt = f"""
    Summarize the following conversation highlighting:
    - Key agreements
    - Budget decisions
    - Deadlines
    - Pending items

    Conversation:
    {text}
    """

    return llm.invoke(prompt)