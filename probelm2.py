import pandas as pd
import datetime


# read the excel file
df =pd.read_excel('SampleData.xlsx')
# replace the empty cell with the name of ayushi
df['SalesMan'].fillna('Ayushi',inplace=True)


def convert_date_in_full_month(date_str):
    # date_str is simply a date in string format that gets passed to the function for conversion. The function then returns the updated date string based on the specified logic.
    day, month, year = date_str.split('/')
    year = int(year)
    if year >= 0 and year <= 20:
        year_str = "20" + str(year).zfill(2)
    else:
        year_str = str(year).zfill(2)
    return f'{day}/{month}/{year_str}'

# repalce the date formate dd/mm/yy to dd/mm/20yy
df['OrderDate'] = df['OrderDate'].apply(convert_date_in_full_month)

# create all the time of hit the button create new update excel with time 
timestamp_str = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
output_file = f'updated_data_{timestamp_str}.xlsx'

# update DataFrame to new Excel file
df.to_excel(output_file, index=False)

print(f"New Excel file '{output_file}' with updated data has been created.")
