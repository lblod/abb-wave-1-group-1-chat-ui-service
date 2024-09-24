import gradio as gr
from .dao import MockedHeritageDontDAO
from .logic import LLMClient

llmClient = LLMClient()
dao = MockedHeritageDontDAO()

def yes_man(message, history):
    donts = dao.get("")
    preprocessed = llmClient.preprocess_input(message, history, donts)
    return llmClient.chat(preprocessed)

gr.ChatInterface(
    yes_man,
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
).launch()