import tkinter as tk
from tkinter import scrolledtext
from financial_chatbot import FinancialChatbot

class ChatbotUI:
    """
    A class to create the user interface for the Financial Chatbot.
    """
    def __init__(self, root, chatbot):
        """
        Initialize the ChatbotUI with the root window and chatbot instance.
        
        Args:
            root (tk.Tk): The root window.
            chatbot (FinancialChatbot): The chatbot instance.
        """
        self.chatbot = chatbot
        self.root = root
        self.root.title("Financial Chatbot")
        
        self.text_area = scrolledtext.ScrolledText(root, height=20, width=50, wrap=tk.WORD)
        self.text_area.pack(pady=10)
        
        self.entry_frame = tk.Frame(root)
        self.entry_frame.pack(pady=10)
        
        self.entry = tk.Entry(self.entry_frame, width=40)
        self.entry.grid(row=0, column=0, padx=5)
        self.entry.bind("<Return>", self.get_response)
        
        self.send_button = tk.Button(self.entry_frame, text="Send", command=self.get_response)
        self.send_button.grid(row=0, column=1, padx=5)
        
        self.exit_button = tk.Button(root, text="Exit", command=root.quit)
        self.exit_button.pack(pady=10)
        
        self.text_area.insert(tk.END, "Welcome to the Financial Chatbot!\n")
        self.text_area.insert(tk.END, "You can ask about net income, revenue, expenses, or growth metrics.\n")
        self.text_area.insert(tk.END, "Type 'exit' to quit the application.\n\n")
    
    def get_response(self, event=None):
        """
        Get the response from the chatbot and display it in the text area.
        
        Args:
            event (tk.Event, optional): The event that triggered the method. Defaults to None.
        """
        user_query = self.entry.get()
        if user_query.lower() == "exit":
            self.root.quit()
        else:
            response = self.chatbot.get_response(user_query)
            self.text_area.insert(tk.END, f"You: {user_query}\n")
            self.text_area.insert(tk.END, f"Bot: {response}\n\n")
            self.entry.delete(0, tk.END)

if __name__ == "__main__":
    chatbot = FinancialChatbot()
    
    root = tk.Tk()
    app = ChatbotUI(root, chatbot)
    root.mainloop()
