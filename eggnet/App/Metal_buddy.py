import tkinter as tk
import openai
from PIL import Image, ImageTk

# Set up OpenAI API Key (You need to replace this with your actual API key)
openai.api_key = "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"

# Function to get AI response from OpenAI GPT-3.5 or GPT-4 using the Chat API
def get_ai_response(prompt):
    try:
        # Use the v1/chat/completions endpoint
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # You can use "gpt-3.5-turbo" or "gpt-4" here
            messages=[
                {"role": "system", "content": "You are a helpful, kind assistant for the eggman empire. You are named "Metal Sonic"},
                {"role": "user", "content": prompt}
            ]
        )
        # Extract and return the assistant's reply
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error: {e}"

# Function to handle dynamic user input and show the AI response with image
def show_response():
    user_input = entry.get().strip()
    
    if not user_input:
        response_label.config(text="Please enter a message!")
        image_label.config(image="")
        return
    
    # Get the AI's response based on user input
    ai_response = get_ai_response(user_input)
    
    # Display AI text response
    response_label.config(text=ai_response)

    # For now, just display a simple placeholder image
    try:
        # Example: Show a placeholder image for demonstration (replace with actual logic)
        img = Image.open("E:/Eggman empire/eggnet/App/MetalSonic3.png")  # Replace with path to an actual image
        img = img.resize((200, 200))
        img_tk = ImageTk.PhotoImage(img)
        image_label.config(image=img_tk)
        image_label.image = img_tk
    except Exception as e:
        image_label.config(image="")
        response_label.config(text=f"Error loading image: {e}")

# Set up the main window
window = tk.Tk()
window.title("AI Assistant")

# Create an entry box for user input
entry_label = tk.Label(window, text="Ask me anything!")
entry_label.pack()

entry = tk.Entry(window, width=50)
entry.pack()

# Button to trigger response
submit_button = tk.Button(window, text="Submit", command=show_response)
submit_button.pack()

# Label for displaying AI response text
response_label = tk.Label(window, text="", font=("Arial", 16))
response_label.pack()

# Label for displaying the image (optional, can be replaced with AI-generated content)
image_label = tk.Label(window)
image_label.pack()

# Run the Tkinter event loop
window.mainloop()
