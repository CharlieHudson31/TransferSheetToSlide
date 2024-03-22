# TransferSheetToSlide


## This program transfers Google Sheet data into a new Google Slide presentation.

## Goal: 
The goal of this project is to easily output automated slideshows given user input from a spreadsheet. 
## Workflow: 
[Manually Input Enter Spreadsheet Data] -> [Collect Spreadsheet Data from Sheets API] -> [Convert data into a textbox, and add to presentation with Slides API]

## Requirements:
    - 1. [Google Cloud Console](https://console.cloud.google.com/)
        Note. A free trial is currently available with no auto renewal.
          
    - 2.A Google Account associated with the Cloud Console Account.
      
    - 3. The pip package management tool

Set-Up:
    Installation:
        1. Run pip install -r 'requirements.txt'
          
    Configuration:

    1. Create a google account that you will use certain services for (Google Slides and Googe Sheets)  
      
    2. Create a [google cloud console](https://console.cloud.google.com/) account subscription 
    
    3. Create a new project on your google console


    4. From the servies search bar, enable Google Slides API and Google Sheets API


    5. Create a Google Slides presentation


    6. Copy the presentation ID from the url in the address bar. Paste into example-config.py


    7. Create a Google Sheets spreadsheet.
      
    8. Copy the presentation ID from the url in the address bar. Paste into example-config.py
          
    9. Rename 'example-config.py' to 'config.py'
      
    10. Run the program in the terminal 'python example-config.py'
      

Slide Format:
  
The slides have a pre-defined format associated with the data layout of the spreadsheet. If someone wants to add/remove the type of data in the spreadsheet, then they may also wish the alter the slide format. For example, if someone wanted to add a "description category", they would need a additional textbox element in the slide. This project will only produce one specific format.
