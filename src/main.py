import gradio as gr
from .dao import MockedHeritageDontDAO, LODDAO
from .logic import LLMClient

llmClient = LLMClient()
dao = LODDAO()


def handle_chat(message, history):
    rules = dao.get()
    print(rules)
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
).launch()
