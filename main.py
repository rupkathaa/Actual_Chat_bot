import gradio as gr
import requests

def chatbot_response(user_input, chat_history):
    url = "https://brain-bot-8hky.vercel.app/chat"
    try:
        response = requests.post(url, json={"user_input": user_input})
        if response.status_code == 200:
            data = response.json()
            reply = data.get("response", "No response received.")
        else:
            reply = f"Error: {response.status_code}"
    except Exception as e:
        reply = f"Request failed: {e}"
    
    chat_history.append((user_input, reply))
    return "", chat_history

with gr.Blocks() as demo:
    gr.Markdown("# Brain Tumor Chatbot")
    gr.Markdown("Ask me anything about brain tumors!")
    
    chatbot = gr.Chatbot()
    user_input = gr.Textbox(label="Your question:")
    
    with gr.Row():
        submit_button = gr.Button("Ask")
        clear_button = gr.Button("Clear")
    
    submit_button.click(chatbot_response, inputs=[user_input, chatbot], outputs=[user_input, chatbot])
    clear_button.click(lambda: [], outputs=[chatbot])

def start():
    # Vercel will provide the PORT environment variable
    demo.launch(server_name="0.0.0.0", server_port=int(os.environ.get("PORT", 7860)))

if __name__ == "__main__":
    start()

