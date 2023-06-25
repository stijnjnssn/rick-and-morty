from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
"""
To send a .csv file to your Google Drive after the container has been executed for 30 minutes, 
you can use the PyDrive library or the Google Drive API.
"""
# Authenticate and create GoogleDrive instance
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

# Wait for 30 minutes before uploading the file
time.sleep(1800)

# Define the file path
csv_file = 'df_final.csv'

# Save df_final to a CSV file
df_final.to_csv(csv_file)

# Upload the CSV file to Google Drive
file_drive = drive.CreateFile({'title': csv_file})
file_drive.SetContentFile(csv_file)
file_drive.Upload()

# Delete the local CSV file
os.remove(csv_file)
