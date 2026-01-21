import gradio as gr

with gr.Blocks() as app:
    gr.Label("bananas")


if __name__ == "__main__":
    app.launch()
    