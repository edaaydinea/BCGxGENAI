from financial_chatbot import FinancialChatbot
from financial_chatbot_ui import ChatbotUI
import tkinter as tk

def main():
    """
    Main function to start the Financial Chatbot application.
    """
    chatbot = FinancialChatbot()
    
    root = tk.Tk()
    app = ChatbotUI(root, chatbot)
    root.mainloop()

if __name__ == "__main__":
    main()
