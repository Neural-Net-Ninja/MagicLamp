from datetime import date as dt

def todays_date():
    # Get today's date
    today = dt.today()

    # Format the date
    formatted_date = today.strftime('%d-%b-%Y')

    return formatted_date


# Use the function
# print(todays_date())