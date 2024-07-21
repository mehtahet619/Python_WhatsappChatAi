import google.generativeai as genai

API_key = "AIzaSyCJlrrriaupZ-9gtt-kiCz4qF-l4mVTgec"
command = "Hi Het How are you"

# Configure the API key
genai.configure(api_key=API_key)

# Initialize the generative model
model = genai.GenerativeModel('gemini-pro')

# Start the chat with an empty history
chat = model.start_chat(history=[])

# Send the initial command and get the response
question = command.strip()

if question:
    response = chat.send_message(question)
    print("\n")
    print(f"{response.text}")
else:
    print("No command provided.")

# Exit after the first response
# print("Chal Bye Bro")
