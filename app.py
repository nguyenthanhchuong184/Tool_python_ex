import pandas as pd
import xlsxwriter
import openpyxl

data = pd.ExcelFile("Contact_Rikai.xlsx")

data_file_1, data_file_2 = (
    pd.read_excel(data, "None IT Companies"),
    pd.read_excel(data, "Non IT 0829"),
)

data_old, data_new = (
    list(data_file_1["Company Url"]),
    list(data_file_2["Company Url"]),
)

new_list = list(set(data_new).difference(data_old))
list_column_key = [str(i).replace(".", "_") for i in new_list]

df = pd.DataFrame({"Company Url": new_list})

df.to_excel("new_file.xlsx", sheet_name="sheet1", index=False)
