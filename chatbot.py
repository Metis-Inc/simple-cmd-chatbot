import requests

# Base URL and headers
base_url = "https://api.metisai.ir/api/v1/chat"
api_key = "YOUR_API_KEY"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

def create_chat_session(bot_id, user=None, initial_messages=None):
    """
    Create a new chat session.
    """
    url = f"{base_url}/session"
    data = {
        "botId": bot_id,
        "user": user,
        "initialMessages": initial_messages or []
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

def send_message(session_id, content, message_type="USER"):
    """
    Send a message in a chat session.
    """
    url = f"{base_url}/session/{session_id}/message"
    data = {
        "message": {
            "content": content,
            "type": message_type
        }
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

def delete_chat_session(session_id):
    """
    Delete a chat session.
    """
    url = f"{base_url}/session/{session_id}"
    requests.delete(url, headers=headers)


def get_chat_sessions_for_bot(bot_id, page=0, size=10):
    """
    Get a list of chat sessions for a bot.
    """
    url = f"{base_url}/session?botId={bot_id}&page={page}&size={size}"
    response = requests.get(url, headers=headers)
    return response.json()

def get_chat_session_info(session_id):
    """
    Get information about a chat session.
    """
    url = f"{base_url}/session/{session_id}"
    response = requests.get(url, headers=headers)
    return response.json()

def main():
    bot_id = "BOT_ID"
    session_id = None

    while True:
        print("\nChat Bot Menu:")
        print("1. Create Chat Session")
        print("2. Send Message")
        print("3. Delete Chat Session")
        print("4. Get List of Sessions for Bot")
        print("5. Get Session Info")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            initial_messages = [{"content": "Hello, how can I help you today?", "type": "AI"}]
            session = create_chat_session(bot_id, initial_messages=initial_messages)
            print("** Chat session created:", session)
            session_id = session.get("id")

        elif choice == "2":
            if session_id:
                content = input("Enter your message: ")
                message_response = send_message(session_id, content)
                print("** Message sent, here is bot response:", message_response.get("content"))
            else:
                print("No active session. Please create a session first.")

        elif choice == "3":
            if session_id:
                delete_chat_session(session_id)
                print("** Chat session deleted:")
                session_id = None
            else:
                print("No active session to delete.")

        elif choice == "4":
            bot_sessions = get_chat_sessions_for_bot(bot_id)
            print("List of chat sessions for bot:", bot_sessions)

        elif choice == "5":
            if session_id:
                session_info = get_chat_session_info(session_id)
                print("Chat session info:", session_info)
            else:
                print("No active session. Please create a session first.")

        elif choice == "6":
            print("Exiting chat bot.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
