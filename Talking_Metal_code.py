import openai
import pyttsx3
import time

openai.api_key = "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"
assistant_id = "asst_GvqDZL4WXynP3T8wD8szSot3"  # Replace with your Assistant ID

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 150)  # Adjust speed if needed

# Create a new thread (reuse the same thread for conversation continuity)
thread = openai.beta.threads.create()
thread_id = thread.id

def chat_with_assistant(prompt):
    # Send user input to the assistant
    openai.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=prompt
    )

    # Start processing the assistant's response
    run = openai.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id
    )

    # Wait for the response
    while True:
        run_status = openai.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run.id
        )

        if run_status.status == "completed":
            break  # Exit loop when response is ready

        time.sleep(2)  # Wait before checking again

    # Fetch latest message from the assistant
    messages = openai.beta.threads.messages.list(thread_id=thread_id)
    response = messages.data[0].content[0].text.value  # Extract text response
    return response

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

# Main Loop
while True:
    user_input = input("You: ")  # Get user input
    if user_input.lower() in ["exit", "quit"]:
        break  # Exit loop on command
    
    response = chat_with_assistant(user_input)  # Get GPT's response
    print(f"Assistant: {response}")  # Print response
    speak_text(response)  # Speak response
