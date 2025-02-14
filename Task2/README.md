# Financial Chatbot

This project implements an AI-powered financial chatbot that can answer queries about financial data for specific companies. The chatbot uses rule-based logic to provide responses based on predefined financial metrics.

## Prerequisites

- Python 3.x
- CSV files containing financial data (`final_summary.csv` and `final_data.csv`)

## Setup

1. Ensure you have Python 3.x installed on your system.
2. Place the `final_summary.csv` and `final_data.csv` files in the `Task1` directory.
3. Navigate to the `Task2` directory.

## Running the Chatbot

1. Open a terminal or command prompt.
2. Navigate to the `Task2` directory:

   ```sh
   cd /path/to/your/Task2
   ```

3. Run the `financial_chatbot_app.py` script:

   ```sh
   python financial_chatbot_app.py
   ```

4. The chatbot UI will open. You can ask a financial question in the input field and press Enter or click "Send".
   - Example Queries:
     - "What is the net income for Apple?"
     - "Tell me the revenue growth for Microsoft."
     - "How much are the expenses for Tesla?"
     - "What is the cash flow from operations growth for Apple?"
     - "What is the revenue for Microsoft?"
     - "Tell me the net income growth for Tesla."
     - "How much are the liabilities for Apple?"
     - "What is the assets growth for Microsoft?"

5. The chatbot will respond with the relevant financial information. If you misspell a company name or a keyword, the chatbot will suggest the correct name or keyword. You can confirm the suggestion by typing 'yes' or 'no'. If you confirm, the chatbot will provide the correct response based on the suggestion.

## Example Queries

- "What is the net income for Apple?"
- "Tell me the revenue growth for Microsoft."
- "How much are the expenses for Tesla?"
- "What is the cash flow from operations growth for Apple?"

## Notes

- The chatbot currently supports queries about net income, revenue, expenses, and growth metrics (revenue growth, net income growth, assets growth, liabilities growth, and cash flow from operations growth) for Apple, Microsoft, and Tesla.
- Ensure the CSV files are correctly formatted and placed in the appropriate directory for the chatbot to function properly.
- The chatbot can handle misspelled company names and keywords, providing suggestions for the correct names and keywords. Users can confirm the suggestions by typing 'yes' or 'no'. If confirmed, the chatbot will provide the correct response based on the suggestion.

## Contact

For any questions or issues, please contact the project maintainer.