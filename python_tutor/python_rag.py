import os
import json
import time
import dotenv
from google import genai
from history_manager import validate_and_repair_history
from tutor_stats import display_cli_metrics
from google.api_core import exceptions

dotenv.load_dotenv()

class PythonTutor:
    def __init__(self, kb_path: str = 'python_basics.md'):
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        self.model_id = "gemini-2.0-flash"
        self.history_file = "query_history.jsonl"
        self.knowledge_base = self._load_kb(kb_path)
        self.conversation_history = []
        self.start_time = time.time() # Track start internally

    def _load_kb(self, path: str) -> str:
        try:
            with open(path, 'r') as f:
                return f.read()
        except FileNotFoundError:
            return "Standard Python documentation context."

    @property
    def system_instruction(self) -> str:
        role_context = """
Role: 
- Python tutor for neuroscientist researchers. 
- Explain the concepts clearly and conceptually, but be concise. 
- Avoid unnecessary code examples. 
- Aim for responses under 400 tokens."
"""
        return f"Context: {self.knowledge_base}\n{role_context}"

    def ask(self, query: str) -> str:
        elapsed = round((time.time() - self.start_time) / 60, 2)
        active_history = self.conversation_history[-4:]  # Last 4 exchanges (keeps context manageable and prevents rate limits for free tier)
        self.conversation_history.append({"role": "user", "parts": [{"text": query}]})

        max_retries = 5
        retry_delay = 5

        for attempt in range(max_retries):
            try:        
                response = self.client.models.generate_content(
                    model=self.model_id,
                    contents=self.conversation_history,
                    config=genai.types.GenerateContentConfig(system_instruction=self.system_instruction, max_output_tokens=400)
                )

                # tutor_text = response.text
                # self.conversation_history.append({"role": "model", "parts": [{"text": tutor_text}]})
        
                tutor_text = response.text
                self.conversation_history.append({"role": "model", "parts": [{"text": tutor_text}]})

                from datetime import datetime
                entry = {
                    "timestamp": datetime.now().isoformat(),
                    "query": query,
                    "response": tutor_text,
                    "response_length": len(tutor_text),
                    "model": self.model_id,
                    "session_duration": elapsed # Logged per query
                }
                with open(self.history_file, 'a') as f:
                    f.write(json.dumps(entry) + '\n')

                return tutor_text
            
            except Exception as e:
                # Check if it's a rate limit error
                if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
                    if attempt < max_retries - 1:
                        print(f"Rate limit hit. Retrying in {retry_delay} seconds...")
                        time.sleep(retry_delay)
                        retry_delay *= 2  # Exponential backoff
                        continue
                raise e

def main():
    tutor = PythonTutor()
    print("--- Python Tutor Active (Type 'exit' to end) ---")
    while True:
        try:
            user_input = input("\nStudent: ").strip()
            if user_input.lower() in ['exit', 'quit']:
                total_duration = round((time.time() - tutor.start_time) / 60, 2)
                print(f"\n[System] Finalizing session ({total_duration} min)...")
                is_valid = validate_and_repair_history()
                if not is_valid:
                    print("⚠️  Note: Logs were repaired.")
                display_cli_metrics(duration=total_duration)
                break
            if user_input:
                print(f"\nTutor: {tutor.ask(user_input)}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()