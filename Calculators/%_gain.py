from prettytable import PrettyTable
from datetime import datetime

def calculate_return(performances):
    """
    Calculate the total return based on the performance of each company.

    Parameters:
    performances (dict): A dictionary of company names and performance percentages.

    Returns:
    dict: A dictionary of company names and their performance, investment, and return.
    """
    # Initialize the total investment and the total return
    total_investment = 0
    total_return = 0

    # Create a dictionary to store the results
    results = {}

    # Loop through the performances
    for company, performance in performances.items():
        # Calculate the investment and the return for this company
        investment = 100 / len(performances)
        return_ = investment * (1 + performance / 100)

        # Update the total investment and the total return
        total_investment += investment
        total_return += return_

        # Add the results to the dictionary
        results[company] = {"Performance": f"{performance}%", "Investment": f"{investment:.2f}", "Return": f"{return_:.2f}"}

    # Calculate the total return percentage
    total_return_percentage = (total_return - total_investment) / total_investment * 100

    # Add the total return percentage to the results dictionary
    results["Total Return %"] = f"{total_return_percentage:.2f}%"

    # Get the date
    date = datetime.now().strftime('%d/%b/%Y')

    # Create a table
    table = PrettyTable()
    table.field_names = ["Company", "Performance", "Investment", "Return", "Date", "Total Return %"]

    # Add rows to the table from the results dictionary
    companies = list(performances.keys())
    middle_index = len(companies) // 2
    for i, company in enumerate(companies):
        data = results[company]
        if i == middle_index:
            table.add_row([company, data["Performance"], data["Investment"], data["Return"], date, results["Total Return %"]])
        else:
            table.add_row([company, data["Performance"], data["Investment"], data["Return"], "", ""])

    # Print the table
    print(table)

    return results

# Example usage:
performances = {
    "Solar Industries": 1.69, 
    "BEML": -0.21, 
    "Bharat Electronics": 1.73, 
    "Bharat Dynamics": 6.51
}
results = calculate_return(performances)