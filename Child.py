import openai
import gradio as gr
import sys

openai.api_key = "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"

def check_api_key():
    if not openai.api_key:
        print("Error: Model is not set.")
        sys.exit(1)

check_api_key()

# Update the system message to focus on parenting style and child development
system_message = {
    "role": "system",
    "content": "You are an AI specialized in providing information and advice on parenting style and child development."
               "Please ask questions related to these topics."
}

# Initialize messages as a global variable
messages_temp = [system_message]

def chatbot(input):
    global messages_temp  # Access the global variable

    try:
        MAX_MESSAGES = 20
        if input and len(messages_temp) < MAX_MESSAGES:
            messages_temp.append({"role": "user", "content": input})
            chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages_temp)
            reply = chat.choices[0].message['content']
            messages_temp.append({"role": "assistant", "content": reply})
            return reply
        else:
            # Reset messages_temp if the conversation history is too long
            messages_temp = [{"role": "system", "content": "You are AI specialized in Parenting style & Child development."}]
            return "The conversation history is too long. Please start a new conversation."
    except Exception as e:
        return f"An error occurred: {str(e)}"


# Use the 'gr.Interface' class and 'gr.TextArea' for input and output
iface = gr.Interface(
    fn=chatbot,
    inputs=gr.TextArea(lines=7, label="Chat with me"),
    outputs=gr.TextArea(label="Reply"),
    title="Parenting Style & Child Development",
    description="Know about Parenting Styles and Child Development.",
)

iface.launch(share=True,auth=("admin", "pass1234"))
