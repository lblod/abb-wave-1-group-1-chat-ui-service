import gradio as gr

from dao import LODDAO
from logic import LLMClient

llmClient = LLMClient()
dao = LODDAO()


def handle_chat(message, history, designation_id):
    
    print(message)
    print(history)
    print(designation_id)
    print("------")
    
    rules = dao.get(designation_id)
    print(rules)
    
    if len(rules) == 0:
        return """Het aanduidingsobject dat u zoekt werd niet terug gevonden in onze databank.
    Controleer of u het juiste adres hebt opgegeven."""
    
    preprocessed = llmClient.preprocess_input(message, history, rules)
    return llmClient.chat(preprocessed)

gr.ChatInterface(
    handle_chat,
    chatbot=gr.Chatbot(height=300),
    textbox=gr.Textbox(placeholder="Hi! how can I help you?", container=False, scale=7),
    title="Heritage AI",
    description="",
    theme="soft",
    examples=[],
    cache_examples=True,
    retry_btn=None,
    undo_btn="Delete Previous",
    clear_btn="Clear",
    
    additional_inputs=[
        gr.Textbox(label="designation_id", value='14969')
    ]
).launch()