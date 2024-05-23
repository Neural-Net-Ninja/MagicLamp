from prettytable import PrettyTable
from datetime import datetime

def calculate_return(performances):
    """
    Calculate the total return based on the performance of each company.

    Parameters:
    performances (dict): A dictionary of company names and performance percentages.

    Returns:
    float: The total return percentage.
    """
    # Initialize the total investment and the total return
    total_investment = 0
    total_return = 0

    # Create a table
    table = PrettyTable()
    table.field_names = ["Company", "Performance", "Investment", "Return"]

    # Loop through the performances
    for company, performance in performances.items():
        # Calculate the investment and the return for this company
        investment = 100 / len(performances)
        return_ = investment * (1 + performance / 100)

        # Update the total investment and the total return
        total_investment += investment
        total_return += return_

        # Add a row to the table
        table.add_row([company, f"{performance}%", f"{investment:.2f}", f"{return_:.2f}"])

    # Calculate the total return percentage
    total_return_percentage = (total_return - total_investment) / total_investment * 100

    # Print the date
    print(f"Date: {datetime.now().strftime('%d/%b/%Y')}")

    # Print the table
    print(table)

    return total_return_percentage


# Example usage:
performances = {
    "Solar Industries": 1.69, 
    "BEML": -0.21, 
    "Bharat Electronics": 1.73, 
    "Bharat Dynamics": 6.51
}
total_return_percentage = calculate_return(performances)
print(f"The total return percentage is {total_return_percentage:.2f}%.")