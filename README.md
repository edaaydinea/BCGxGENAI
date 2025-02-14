# BCGx GENAI Virtual Internship Program

This repository contains the deliverables for the BCGx GENAI Virtual Internship Program. The internship program consists of two tasks that focus on financial data analysis and the development of an AI-powered financial chatbot. The tasks are designed to provide hands-on experience in working with financial data, analyzing key metrics, and developing AI applications for financial insights.

## Task 1: Extracting Key Financial Data and Preparing for AI-Driven Insights

### What was requested

In Task 1, the objective was to extract key financial data from the 10-K filings of Microsoft, Tesla, and Apple for the last three fiscal years. The task involved the following steps:

1. **Data Extraction**: Manually extract key financial figures from the 10-K documents.
2. **Basic Analysis**: Identify significant financial trends and indicators.
3. **Data Preparation**: Format and clean the data for further processing in an AI model.

### What was done

#### Step 1: Data Extraction

- Navigated to the SEC's EDGAR database to locate the 10-K filings for Microsoft, Tesla, and Apple.
- Extracted the following financial figures for each company: Total Revenue, Net Income, Total Assets, Total Liabilities, and Cash Flow from Operating Activities.
- Compiled the extracted data into an Excel spreadsheet for easy reference during the analysis.

#### Step 2: Preparing the Jupyter Notebook Environment

- Installed Jupyter Notebook using pip and launched it in the web browser.
- Created a new notebook for the analysis.

#### Step 3: Python Analysis in Jupyter

- Imported the pandas library to work with the data.
- Loaded the data from the Excel file into a pandas DataFrame.
- Calculated year-over-year changes for each financial metric using pandas.
- Analyzed the data across different dimensions (by company, over years, etc.).
- Summarized the findings directly in the notebook using markdown cells to add narrative explanations.

#### Step 4: Documentation and Submission

- Documented the analysis methodology, observations, and conclusions throughout the Jupyter Notebook.
- Exported the Jupyter Notebook as a PDF or HTML file for submission.

### Purpose of the Task

The purpose of this task was to lay the groundwork for a sophisticated AI-driven financial analysis project. By extracting and analyzing key financial data from 10-K documents, the task aimed to:

- **Contextualize AI in Finance**: Understand how AI can transform raw financial data into insightful analytics.
- **Identify Key Financial Indicators**: Enhance the ability to recognize significant financial metrics crucial for AI analysis.
- **Ensure Data Quality**: Learn to identify and extract high-quality, relevant financial data for accurate AI modeling.
- **Understand Data Structure**: Comprehend the structuring of financial data, which is pivotal for preparing it for AI integration.

This task provided a deep understanding of financial data analysis and its significance in AI applications, setting the foundation for the rest of the project with the client, Global Finance Corp. (GFC).

## Task 2: Developing an AI-Powered Financial Chatbot

### What was requested

In Task 2, the objective was to develop an AI-powered financial chatbot that can analyze financial data and provide insights. The task involved the following steps:

1. **Develop the Chatbot**: Create an AI chatbot that can interpret and relay financial insights.
2. **Integrate Data**: Incorporate the previously extracted and analyzed financial data into the chatbot system.
3. **Test the Chatbot**: Ensure the chatbot can effectively communicate financial performance insights and comparisons.

### What was done

#### Step 1: Developing the Chatbot

- Implemented rule-based logic to handle predefined financial queries.
- Ensured the chatbot could respond accurately to specific financial questions using predetermined responses.

#### Step 2: Integrating Financial Data

- Structured the financial data in a format that the chatbot could easily access and interpret (e.g., JSON or CSV).
- Implemented retrieval methods to fetch the right piece of data based on user queries.
- Mapped predefined queries to specific data points in the dataset for accurate responses.

#### Step 3: Testing the Chatbot

- Tested the chatbot to handle various financial queries and ensure it provided accurate and insightful responses.
- Refined the chatbot's responses to improve clarity and relevance.
- Documented the testing process and results to ensure the chatbot met the project requirements.

### Purpose of the Task

The purpose of this task was to transform the previously analyzed financial data into interactive insights through an AI-powered chatbot. By developing this chatbot, the task aimed to:

- **Leverage AI in Financial Analysis**: Utilize AI to make complex financial data accessible and understandable.
- **Enhance User Interaction**: Create an interactive platform that allows users to explore financial data through natural language queries.
- **Improve Decision-Making**: Provide users with actionable financial insights to aid in decision-making processes.

This task built on the foundation laid in Task 1, integrating the analyzed financial data into a user-friendly AI chatbot, thereby enhancing the project's overall value to the client, Global Finance Corp. (GFC).

