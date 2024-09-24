import os
from ollama import Client


class LLMClient:
    
    #http://hackathon-ai-1.s.redhost.be/11434
    def __init__(self, api=os.environ.get('OLLAMA_HOST', 'http://hackathon-ai-1.s.redhost.be/11434'), model="llama3.1"):
        self.llm = Client(host=api)
        self.model = model
        
    def preprocess_input(self, message:str, history:str, donts:list[dict[str, str]]):
        messages = [{
            'role': 'system',
            'content': '''You are a helpfull assitant that works for the Flemish government.
            You will answer questions about heritage objects.
            
            If a question is asked about the don'ts, always cite the relevant resource(s) if there are any!
            Answer always in Dutch.
            '''
        }]
        
        for old_turn in history:
            old_turn = [old_turn] if isinstance(old_turn, str) else old_turn
            
            for i, old_message in enumerate(old_turn):
                messages.append({
                    'role': 'user' if i%2 == 0 else 'assistant',
                    'content': old_message if isinstance(old_message, str) else old_message[i%2]
                })
            
        messages.append({
            'role': 'user',
            'content': f'''The following list might contain information that is usefull for the following question:
                        {donts}
                        
                        {message}
                        
                        Be helpfull and polite but keep it short and simple.
                        Only answer with information that is strictly relevant to this question'''
        })
        
        return messages
        
    def chat(self, messages:list[dict[str, str]]):
        response = self.llm.chat(model=self.model, messages=messages, options={'temperature': 0.1})
        return response['message']['content']


