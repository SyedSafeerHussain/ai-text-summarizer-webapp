from transformers import pipeline

summarizer=pipeline("summarization", model="Falconsai/text_summarization")

def generate_summary(text):
    try:
        result=summarizer(text,max_length=50,min_length=15,do_sample=False)
        return result[0]["summary_text"]
    except Exception as e:
        return f"❌ Error: {e}"