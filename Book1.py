import pandas as pd

try:
    # Load the Excel file (replace 'Sheet1' with your actual sheet name if needed)
    df = pd.read_excel("Book1.xlsx", sheet_name="Sheet1")

    # Display the content of the Excel file in the terminal
    print(df)

except FileNotFoundError:
    print("Error: The file does not exist")
except Exception as e:
    print("Error:", e)
