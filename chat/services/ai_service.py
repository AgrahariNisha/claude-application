from groq import Groq
from django.conf import settings

client = Groq(api_key=settings.GROQ_API_KEY)

def get_ai_response(message):
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",  # ✅ FIXED MODEL
            messages=[
                {"role": "user", "content": message}
            ]
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"