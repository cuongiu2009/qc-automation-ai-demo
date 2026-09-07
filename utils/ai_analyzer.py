import os
from google import genai
from google.genai.errors import APIError

def analyze_failure_log(error_trace: str) -> str:
    """
    Nhận vào stack trace khi test bị FAILED, gọi Gemini API để phân tích lỗi.
    """
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return "AI Analysis skipped: GEMINI_API_KEY not set."

    try:
        client = genai.Client()
        
        prompt = (
            "You are a Senior Automation Engineer. Analyze the following failed test stack trace.\n"
            "Provide the response in this exact format:\n"
            "Issue: [Type of error]\n"
            "Root Cause: [Concise explanation of why it failed]\n"
            "Recommendation: [Concise fix in English, under 3 sentences]\n\n"
            f"Stack Trace:\n{error_trace}"
        )
        
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        
        return response.text.strip()
        
    except Exception as e:
        return f"AI Analysis failed: {str(e)}"
