import pyautogui
import pyperclip
import time
import google.generativeai as genai

API_key = "AIzaSyCJlrrriaupZ-9gtt-kiCz4qF-l4mVTgec"
# command = "Hi Het How are you"

# Configure the API key
genai.configure(api_key=API_key)

# Step 1: Click on the icon at (909, 1048)
pyautogui.click(909, 1048)
time.sleep(6)  # Wait for a second to ensure the action is registered
# pyautogui.moveTo(277,613)##for third chat
# pyautogui.moveTo(277,613)##for third chat
pyautogui.moveTo(325,269)##for first chat
time.sleep(2)
pyautogui.click(325,269)

pyautogui.moveTo(718,882)
time.sleep(2)
pyautogui.tripleClick(718,882)
# pyautogui.dragTo(1919,882, duration=1)  # Drag to the end point, taking 2 seconds

# Step 3: Copy the selected text to the clipboard
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)  # Wait for a moment to ensure the copy action is completed

# Step 4: Retrieve the copied text into a variable
chat_his = pyperclip.paste()
print(f"Copied text: {chat_his}")

model = genai.GenerativeModel('gemini-pro')

# Start the chat with an empty history
chat = model.start_chat(history=[])

# Send the initial command and get the response
question = chat_his.strip()

if question:
    response = chat.send_message(question)
    print("\n")
    print(f"{response.text}")
else:
    print("No command provided.")

# Exit after the first response
print("Chaal Bye Bro")
pyperclip.copy(response.text)
time.sleep(1)
pyautogui.moveTo(1023, 987)
pyautogui.click(1023, 987)
pyautogui.hotkey('ctrl', 'v')
pyautogui.moveTo(1873,986)
pyautogui.hotkey('Enter')
