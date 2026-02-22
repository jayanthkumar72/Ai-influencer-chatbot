from services.llm_service import get_llm

def generate_campaign_brief(data):

    llm = get_llm()

    prompt = f"""
    Create a professional campaign brief with:

    Budget: {data.get("budget")}
    Deliverables: {data.get("deliverables")}
    Timeline: {data.get("timeline")}
    Platform: {data.get("platform")}

    Structure it clearly.
    """

    return llm.invoke(prompt)