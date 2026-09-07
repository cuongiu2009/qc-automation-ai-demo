import os
from google import genai
from google.genai.errors import APIError

def analyze_failure_stack_trace(stack_trace: str) -> str:
    """
    Nhận vào stack trace khi test bị FAILED, gọi Gemini API để phân tích lỗi.
    Yêu cầu thiết lập biến môi trường GEMINI_API_KEY trước khi chạy.
    """
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return (
            "Error: Environment variable 'GEMINI_API_KEY' is not set. "
            "Please set the environment variable to enable AI analysis."
        )

    try:
        # Khởi tạo client sử dụng bộ SDK google-genai mới nhất
        client = genai.Client()
        
        prompt = (
            "You are an expert software QA engineer. Below is a stack trace of a failed test case.\n"
            "Please analyze it to identify the Root Cause and suggest a concise solution/fix.\n"
            "Requirements:\n"
            "1. Focus strictly on the exact root cause and how to fix it.\n"
            "2. Respond in English.\n"
            "3. Keep the entire response under 3 sentences.\n\n"
            f"Stack Trace:\n{stack_trace}"
        )
        
        # Gọi mô hình gemini-2.5-flash tối ưu cho tốc độ và hiệu quả phân tích văn bản/code
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        
        return response.text.strip()
        
    except APIError as e:
        return f"Gemini API Error: {str(e)}"
    except Exception as e:
        return f"An unexpected error occurred during AI analysis: {str(e)}"
