from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
#sheets have a title property, cells have a value property
#acess to a cell: c = ws['A4']
# or d = ws.cell(row=4, column=2, value=10)
# cells are created in memory when first accessed, not wheh wk is created
# looping thru cells will take a lot of memory
# instead:
# range of cells: cell_range = ws['A1':'C2']
# range of rows or cols: col_range = ws['C:D'],  row10 = [10], colC= ws['C']
# or: for row in  Worksheet.iter_rows(), Worksheet.iter_cols() <-- this 1 in read only


def create(creds, title):
  """
  Creates the Sheet the user has access to.
  """
  
  # pylint: disable=maybe-no-member
  try:
    service = build("sheets", "v4", credentials=creds)
    spreadsheet = {"properties": {"title": title}}
    spreadsheet = (
        service.spreadsheets()
        .create(body=spreadsheet, fields="spreadsheetId")
        .execute()
    )
    print(f"Spreadsheet ID: {(spreadsheet.get('spreadsheetId'))}")
    return spreadsheet.get("spreadsheetId")
  except HttpError as error:
    print(f"An error occurred: {error}")
    return error

def get_values(creds, spreadsheet_id, val_range):
  try:
    service = build("sheets", "v4", credentials=creds)

    result = (
        service.spreadsheets()
        .values()
        .get(spreadsheetId=spreadsheet_id, range=val_range)
        .execute()
    )
    values = result.get("values", [])
    print(f"{len(values)} rows retrieved")
    return values
  except HttpError as error:
    print(f"An error occurred: {error}")
    return error
  
