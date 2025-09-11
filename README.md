# Agentic Challenge

This repository contains the code for the agentic challenge.

## Setup Instructions

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Mohakmalhotra0411/Lynqr2.git
    cd agentic-challenge
    ```
2.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Configure API Keys:**
    -  Set up your environment variables or a configuration file with your API keys for the chosen LLM.

4.  **Run the scripts:**
    -  1. Run the llm_call.py on vscode
       2. Paste the command streamlit run C:\Users\User\Downloads\vpl_module-4.3.2\vpl\.vscode\pdf_reader.py on your local terminal to run the pdf_reader.py
       3. Run the weather_mcp.py first on vscode to create WeatherMCP server
       4. Once the server connects to the client_agent.py run it
## LLM API Used

-   **LLM Provider:** [Google Gemini]
-   **Specific Model:** [`gemini-2.5-pro`]

## Sample Inputs and Outputs

### Level 1: PDF Reader
-   **Input:** https://assets.airtel.in/static-assets/cms/investor/docs/annual_results_2024_25/Integrated_Report_and_Annual_Financial_Statements.pdf
-   **Output:** This report tells us about all the sim cards added in respective states of India

### Level 2: Weather Agent
-   **Input:**  "What's the weather like in gurugram today?"
-   **Output:** "Hot and Humid, 35°C"

## Final Deliverable

-   **GitHub Link:** https://github.com/Mohakmalhotra0411/Lynqr2.git
