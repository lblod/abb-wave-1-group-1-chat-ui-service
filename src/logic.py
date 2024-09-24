import os
from ollama import Client


class LLMClient:
    
    #http://hackathon-ai-1.s.redhost.be/11434
    def __init__(self, api=os.environ.get('OLLAMA_HOST', 'http://hackathon-ai-1.s.redhost.be/11434'), model="llama3.1"):
        self.llm = Client(host=api)
        self.model = model
        
    def preprocess_input(self, message, history):
        messages = []
        
        for old_turn in history:
            old_turn = [old_turn] if isinstance(old_turn, str) else old_turn
            
            for i, old_message in enumerate(old_turn):
                messages.append({
                    'role': 'user' if i%2 == 0 else 'assistant',
                    'content': old_message if isinstance(old_message, str) else old_message[i%2]
                })
            
        messages.append({
            'role': 'user',
            'content': message
        })
        
        return messages
        
    def chat(self, messages:list[dict[str, str]]):
        response = self.llm.chat(model=self.model, messages=messages)
        print(response)
        return response['message']['content']
