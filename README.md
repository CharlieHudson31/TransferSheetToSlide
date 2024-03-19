# TransferSheetToSlide
This program transfers Google Sheet data into a new Google Slide presentation.

The workflow is [Enter Spreadsheet Data] -> [Collect Spreadsheet Data from Sheets API] ->  -> [Add data as new text box into a presentation with Slides API]

Requirements:
    1. Google Cloud Console Subscription 
    https://console.cloud.google.com/
        Note. A free trial is currently available with no auto renewal.
    2. A Google Account associated with the Cloud Console Account.
    3. TODO: create a requirements.txt file
Set-Up:
    1. Create a google account that you will use certain services for (Google Slides and Googe Sheets)
    2. Create a google cloud console account subscription 
    https://console.cloud.google.com/
    3. Create a new project on your google console
    4. From the servies search bar, enable Google Slides API and Google Sheets API
    5. Create a Google Slides presentation
        6. Copy the presentation ID from the url in the address bar. Paste into example-config.py
    7. Create a Google Sheets spreadsheet.
        8. Copy the presentation ID from the url in the address bar. Paste into example-config.py
    9. Rename 'example-config.py' to 'config.py'
    10. Run the program in the terminal 'python example-config.py'
    
