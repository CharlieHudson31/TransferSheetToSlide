from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class SlideMaker:
  def __init__(self, creds, PRESENTATION_ID):
    self.creds = creds
    self.PRESENTATION_ID = PRESENTATION_ID
    self.slides = []
    try:
      self.service = build("slides", "v1", credentials=self.creds)
    except HttpError as error:
      print(f"An error occurred: {error}")
      return error
    
  def create_page(self, page_id):
    """ 
    Adds a slide to self.slides and to the presentation.
    Layout: BLANK - A blank page with no elements
    """
    try:
      # 

      requests = [
              {
                  "createSlide": {
                      "objectId": page_id,
                      "slideLayoutReference": {
                          "predefinedLayout": "BLANK"
                      }
                  }

              },

    ]

      # If you wish to populate the slide with elements,
      # add element create requests here, using the page_id.

      # Execute the request.
      body = {"requests": requests}
      response = (
          self.service.presentations()
          .batchUpdate(presentationId=self.PRESENTATION_ID, body=body)
          .execute()
      )
      create_slide_response = response.get("replies")[0].get("createSlide")
      self.slides.append(create_slide_response.get('objectId'))
      print(f"Created slide with ID:{(create_slide_response.get('objectId'))}")

    except HttpError as error:
      print(f"An error occurred: {error}")
      print("Slides not created")
      return error
    return response
  
  def view_slides(self):
    try:

      # Call the Slides API
      presentation = (
          self.service.presentations().get(presentationId=self.PRESENTATION_ID).execute()
      )
      slides = presentation.get("slides")

      print(f"The presentation contains {len(slides)} slides:")
      for i, slide in enumerate(slides):
        print(
            f"- Slide #{i + 1} contains"
            f" {len(slide.get('pageElements'))} elements."
        )
      el_1 = slides[1].get('pageElements')[0]
      print(el_1.get('description'))
    except HttpError as err:
      print(err)

  def create_textbox_with_text(self, page_id, text_id ="default_id", new_text="Placeholder Text", dimension = None):
    """
    Creates the textbox with text, the user has access to.
    """
    if (dimension is None):
      dimension = {'width': {"magnitude": 780, "unit": "PT"}, 'height' : {"magnitude": 38, "unit": "PT"}, 'offset' : [50,50]}
    print(dimension)
    try:
      # Create a new square textbox, using the supplied element ID.
      pt_height = dimension['height']
      pt_width = dimension['width']
      offset_x = int(dimension['offset'][0])
      offset_y = int(dimension['offset'][1])
      requests = [
          {
              "createShape": {
                  "objectId": text_id,
                  "shapeType": "TEXT_BOX",
                  "elementProperties": {
                      "pageObjectId": page_id,
                      "size": {"height": pt_height, "width": pt_width},
                      "transform": {
                          "scaleX": 1,
                          "scaleY": 1,
                          "translateX": offset_x,
                          "translateY": offset_y,
                          "unit": "PT",
                        },            },}
          },
          {# Insert text into the box, using the supplied element ID.
              "insertText": {
                  "objectId": text_id,
                  "insertionIndex": 0,
                  "text": new_text,}
          },]
      # Execute the request.
      body = {"requests": requests}
      response = (
          self.service.presentations()
          .batchUpdate(presentationId=self.PRESENTATION_ID, body=body)
          .execute()
      )
      create_shape_response = response.get("replies")[0].get("createShape")
      print(f"Created textbox with ID:{(create_shape_response.get('objectId'))}")
    except HttpError as error:
      print(f"An error occurred: {error}")

      return error

    return response

  def get_text(self, SLIDE_IDX, name='v1'):

    try:
      # Call the Slides API
      presentation = (
          self.service.presentations().get(presentationId=self.PRESENTATION_ID).execute()
      )
      slides = presentation.get("slides")

      slide_1 = slides[SLIDE_IDX]
      elements = slide_1.get('pageElements')
      for el in elements:
        if 'shape' in el and el['shape']['shapeType'] == 'TEXT_BOX' and 'text' in el['shape']:
          txt_elements = el['shape']['text']['textElements']
          for el in txt_elements:
            if 'textRun' in el:
              txt_content = ''.join(el['textRun']['content'])
          print(txt_content)

    except HttpError as err:
      print(err)

  def text_replace(self, shape_id, replacement_text):
    """
    Run simple_text_replace the user has access to.
    """
    try:
      # Remove existing text in the shape, then insert new text.
      requests = []
      requests.append(
          {"deleteText": {"objectId": shape_id, "textRange": {"type": "ALL"}}}
      )
      requests.append(
          {
              "insertText": {
                  "objectId": shape_id,
                  "insertionIndex": 0,
                  "text": replacement_text,
              }
          }
      )

      # Execute the requests.
      body = {"requests": requests}
      response = (
          self.service.presentations()
          .batchUpdate(presentationId=self.PRESENTATION_ID, body=body)
          .execute()
      )
      print(f"Replaced text in shape with ID: {shape_id}")
      return response
    except HttpError as error:
      print(f"An error occurred: {error}")
      print("Text is not merged")
      return error

  def text_delete(self, shape_id):
    """
    Run simple text delete.
    """

    try:
      # Remove existing text in the shape
      requests = []
      requests.append(
          {"deleteText": {"objectId": shape_id, "textRange": {"type": "ALL"}}}
      )


      # Execute the requests.
      body = {"requests": requests}
      response = (
          self.service.presentations()
          .batchUpdate(presentationId=self.PRESENTATION_ID, body=body)
          .execute()
      )
      print(f"Deleted text shape with ID: {shape_id}")
      return response
    except HttpError as error:
      print(f"An error occurred: {error}")
      print("Text is not merged")
      return error

  def change_title(self, PAGE_ID, new_title="default_title"):
    try:
      delete_request = {
          'deleteText': {
              'objectId': PAGE_ID,
              'textRange': {
                  'type': 'ALL'
              }
          }
      }
      # Insert new text into the title
      insert_request = {
          'insertText': {
              'objectId': PAGE_ID,
              'text': new_title,
              'insertionIndex': 0
          }
      }
      # Update the slide
      body = {
          'requests': [
              delete_request,
              insert_request
          ]
      }
      response = self.service.presentations().batchUpdate(presentationId=self.PRESENTATION_ID, body=body).execute()
    except HttpError as err:
      print(err)
  

  def get_all_pages(self):
      # Retrieve the presentation
      presentation = self.service.presentations().get(presentationId=self.PRESENTATION_ID).execute()

      # Get all slides from the presentation
      slides = presentation.get('slides', [])

      return slides
  
  def update_slides(self):
    #todo: set self.slides to all slides found from get_all_pages
    self.slides=self.get_all_pages
    return

  

