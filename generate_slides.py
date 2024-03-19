import Sheets.spreadsheetmaker as sp
import Slides.quickstart as sl
import config as cf
from googleapiclient.errors import HttpError

PRESENTATION_ID = cf.SLIDES["ID"]
SHEET_ID = cf.SHEETS["ID"]
slides_creds = cf.get_credentials_slides()
sheets_creds = cf.get_credentials_sheets()

title_dim = dimension = {'width': {"magnitude": 780, "unit": "PT"}, 
                         'height' : {"magnitude": 38, "unit": "PT"}, 
                         'offset' : [50,50]}
author_dim = dimension = {'width': {"magnitude": 780, "unit": "PT"}, 
                         'height' : {"magnitude": 25, "unit": "PT"}, 
                         'offset' : [50,80]}

def creat_batch_slides():
    """
    Creates slides with information from google spreadsheet
    Data format:
        Google Spreadsheet:
            Col:   A      B    
                Title | Author
                ---------------
        sp_data:
            [
                [title, author],
                [ example_title, example_author,],
                ....
                [example_title, example_author]
            ]
    Returns:
        page_ids, title_ids, author_ids
    """
    try:
        slideshow = sl.SlideMaker(slides_creds, PRESENTATION_ID)
        sp_data = sp.get_values(sheets_creds, SHEET_ID, cf.SHEETS["DATARANGE"])
        print(sp_data)
        page_ids = []
        title_ids = []
        author_ids = []

        for r, row in enumerate(sp_data[1:]):
            title = row[0]
            author = row[1]
            title_id = f'title_{r}'
            page_id = f'page_{r}'
            slideshow.create_page(page_id)
            page_ids.append(page_id)
            #create title
            text_resp = slideshow.create_textbox_with_text(f'page_{r}', f'title_id_{r}', title, title_dim)
            new_title_id = text_resp['replies'][0]['createShape']['objectId']
            title_ids.append(new_title_id)
            #create author
            text_resp2 = slideshow.create_textbox_with_text(f'page_{r}', f'author_id_{r}', author, author_dim)
            new_author_id = text_resp2['replies'][0]['createShape']['objectId']
            author_ids.append(new_author_id)
       
    except HttpError as error:
        print(f"An error occurred: {error}")
        print("Slides not created")
        exit()
    return page_ids, title_ids, author_ids
    

def main():
    #page_ids, title_ids, author_ids = creat_batch_slides()
    

    return
if __name__ == "__main__":
    main()