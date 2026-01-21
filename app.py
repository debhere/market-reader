import gradio as gr

def func(message, history):
    return "bananas"


if __name__ == "__main__":
    gr.ChatInterface(fn=func).launch()
    