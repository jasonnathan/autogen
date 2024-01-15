tool = SpreadsheetTool('test.xlsx')  # replace 'test.xlsx' with your file path
df = tool.read_spreadsheet()  # reads the spreadsheet and stores the data in df
tool.write_to_spreadsheet(df)  # writes the data in df back to the spreadsheet