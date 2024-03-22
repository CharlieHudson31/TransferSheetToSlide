from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

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
  
