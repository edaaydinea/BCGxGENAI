import csv
from difflib import get_close_matches
from config import SUMMARY_FILE_PATH, DATA_FILE_PATH

class FinancialChatbot:
    """
    A chatbot that provides financial information about specific companies.
    """
    def __init__(self):
        """
        Initialize the FinancialChatbot with summary and data files.
        """
        self.summary_data = self.load_csv_data(SUMMARY_FILE_PATH)
        self.data = self.load_csv_data(DATA_FILE_PATH)
        self.last_suggestion = None
        self.last_query = None
    
    def load_csv_data(self, file_path):
        """
        Load CSV data from the given file path.
        
        Args:
            file_path (str): The path to the CSV file.
        
        Returns:
            list: A list of dictionaries containing the CSV data.
        """
        data = []
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
        return data
    
    def get_response(self, query):
        """
        Get a response to the user's query.
        
        Args:
            query (str): The user's query.
        
        Returns:
            str: The chatbot's response.
        """
        query = query.lower()
        if self.last_suggestion and query in ["yes", "y"]:
            query = self.last_query.replace(self.last_suggestion[0], self.last_suggestion[1])
            self.last_suggestion = None
            self.last_query = None
        elif self.last_suggestion and query in ["no", "n"]:
            self.last_suggestion = None
            self.last_query = None
            return "Please ask your question again."
        
        keywords = ["net income", "revenue", "expenses", "revenue growth", "net income growth", "assets growth", "liabilities growth", "cash flow from operations growth"]
        matched_keyword = self.match_keyword(query, keywords)
        
        if matched_keyword:
            if "net income" in matched_keyword:
                return self.get_net_income(query)
            elif "revenue" in matched_keyword:
                return self.get_revenue(query)
            elif "expenses" in matched_keyword:
                return self.get_expenses(query)
            elif "revenue growth" in matched_keyword:
                return self.get_revenue_growth(query)
            elif "net income growth" in matched_keyword:
                return self.get_net_income_growth(query)
            elif "assets growth" in matched_keyword:
                return self.get_assets_growth(query)
            elif "liabilities growth" in matched_keyword:
                return self.get_liabilities_growth(query)
            elif "cash flow from operations growth" in matched_keyword:
                return self.get_cash_flow_growth(query)
        else:
            suggestion = self.suggest_keyword(query, keywords)
            if suggestion:
                self.last_suggestion = (self.extract_misspelled_word(query, keywords), suggestion)
                self.last_query = query
                return f"Did you mean '{suggestion}'? (yes/no)"
            else:
                return "Sorry, I can't assist with that. Please ask about net income, revenue, expenses, or growth metrics."
    
    def get_net_income(self, query):
        """
        Get the net income for a specific company.
        
        Args:
            query (str): The user's query.
        
        Returns:
            str: The net income information.
        """
        company = self.extract_company(query)
        if not company:
            return self.suggest_company(query)
        for row in self.data:
            if row['Company'].lower() == company:
                return f"The net income for {company.capitalize()} is {row['Net Income']}."
        return "Company not found."
    
    def get_revenue(self, query):
        """
        Get the revenue for a specific company.
        
        Args:
            query (str): The user's query.
        
        Returns:
            str: The revenue information.
        """
        company = self.extract_company(query)
        if not company:
            return self.suggest_company(query)
        for row in self.data:
            if row['Company'].lower() == company:
                return f"The revenue for {company.capitalize()} is {row['Total Revenue']}."
        return "Company not found."
    
    def get_expenses(self, query):
        """
        Get the expenses for a specific company.
        
        Args:
            query (str): The user's query.
        
        Returns:
            str: The expenses information.
        """
        company = self.extract_company(query)
        if not company:
            return self.suggest_company(query)
        for row in self.data:
            if row['Company'].lower() == company:
                return f"The expenses for {company.capitalize()} are {row['Total Liabilities']}."
        return "Company not found."
    
    def get_revenue_growth(self, query):
        """
        Get the revenue growth for a specific company.
        
        Args:
            query (str): The user's query.
        
        Returns:
            str: The revenue growth information.
        """
        company = self.extract_company(query)
        if not company:
            return self.suggest_company(query)
        for row in self.summary_data:
            if row['Company'].lower() == company:
                return f"The revenue growth for {company.capitalize()} is {row['Revenue Growth (%)']}%."
        return "Company not found."
    
    def get_net_income_growth(self, query):
        """
        Get the net income growth for a specific company.
        
        Args:
            query (str): The user's query.
        
        Returns:
            str: The net income growth information.
        """
        company = self.extract_company(query)
        if not company:
            return self.suggest_company(query)
        for row in self.summary_data:
            if row['Company'].lower() == company:
                return f"The net income growth for {company.capitalize()} is {row['Net Income Growth (%)']}%."
        return "Company not found."
    
    def get_assets_growth(self, query):
        """
        Get the assets growth for a specific company.
        
        Args:
            query (str): The user's query.
        
        Returns:
            str: The assets growth information.
        """
        company = self.extract_company(query)
        if not company:
            return self.suggest_company(query)
        for row in self.summary_data:
            if row['Company'].lower() == company:
                return f"The assets growth for {company.capitalize()} is {row['Assets Growth (%)']}%."
        return "Company not found."
    
    def get_liabilities_growth(self, query):
        """
        Get the liabilities growth for a specific company.
        
        Args:
            query (str): The user's query.
        
        Returns:
            str: The liabilities growth information.
        """
        company = self.extract_company(query)
        if not company:
            return self.suggest_company(query)
        for row in self.summary_data:
            if row['Company'].lower() == company:
                return f"The liabilities growth for {company.capitalize()} is {row['Liabilities Growth (%)']}%."
        return "Company not found."
    
    def get_cash_flow_growth(self, query):
        """
        Get the cash flow from operations growth for a specific company.
        
        Args:
            query (str): The user's query.
        
        Returns:
            str: The cash flow from operations growth information.
        """
        company = self.extract_company(query)
        if not company:
            return self.suggest_company(query)
        for row in self.summary_data:
            if row['Company'].lower() == company:
                return f"The cash flow from operations growth for {company.capitalize()} is {row['Cash Flow from Operations Growth (%)']}%."
        return "Company not found."
    
    def extract_company(self, query):
        """
        Extract the company name from the user's query.
        
        Args:
            query (str): The user's query.
        
        Returns:
            str: The company name.
        """
        companies = ["apple", "microsoft", "tesla"]
        for company in companies:
            if company in query:
                return company
        return ""
    
    def suggest_company(self, query):
        """
        Suggest a company name based on the user's query.
        
        Args:
            query (str): The user's query.
        
        Returns:
            str: The suggestion message.
        """
        companies = ["apple", "microsoft", "tesla"]
        words = query.split()
        for word in words:
            matches = get_close_matches(word, companies)
            if matches:
                return f"Did you mean {matches[0]}?"
        return "Company not found."
    
    def match_keyword(self, query, keywords):
        """
        Match a keyword in the user's query.
        
        Args:
            query (str): The user's query.
            keywords (list): A list of keywords to match.
        
        Returns:
            str: The matched keyword.
        """
        for keyword in keywords:
            if keyword in query:
                return keyword
        return None
    
    def suggest_keyword(self, query, keywords):
        """
        Suggest a keyword based on the user's query.
        
        Args:
            query (str): The user's query.
            keywords (list): A list of keywords to suggest.
        
        Returns:
            str: The suggested keyword.
        """
        words = query.split()
        for word in words:
            matches = get_close_matches(word, keywords)
            if matches:
                return matches[0]
        return None
    
    def extract_misspelled_word(self, query, keywords):
        """
        Extract the misspelled word from the user's query.
        
        Args:
            query (str): The user's query.
            keywords (list): A list of keywords to check against.
        
        Returns:
            str: The misspelled word.
        """
        words = query.split()
        for word in words:
            if not any(keyword in word for keyword in keywords):
                return word
        return None

if __name__ == "__main__":
    chatbot = FinancialChatbot()
    
    while True:
        user_query = input("Ask a financial question (or type 'exit' to quit): ")
        if user_query.lower() == "exit":
            print("Goodbye!")
            break
        response = chatbot.get_response(user_query)
        print(response)
