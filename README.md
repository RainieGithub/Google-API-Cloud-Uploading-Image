# Google-API-Cloud-Uploading-Image
## Follow the steps written in the 'instruction document.pdf' to upload the required image categories to the cloud drive via the Google API.

### Step1.[Google API Tutorial] How to apply for OAuth 2.0 credentials? I'll demonstrate using the Google Drive API for you.

### Step2.In continuation of the previous document, when achieving "Authorize OAuth to Fetch Google Drive File Names using Python," before pasting the code, install the required modules using the following seven commands:

■■■■■■■■■■■■■■  library  ■■■■■■■■■■■■■■

■ pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

■ pip3 install google-cloud

■ pip3 install google-cloud-vision

■ pip3 install google.cloud.bigquery pip install google.cloud.storage

■ pip3 install google

■ pip3 install oauth2client     #############(IMPORTANT)#############

■ pip3 install gspread


(If pip3 doesn't work, use pip; it might be a minor bug related to the Python version.)

■■■■■■■■■■■■■■  library  ■■■■■■■■■■■■■■



### Step3.Create a new folder and place quickstart.py, google_api_try.py, and Google.py inside it.

### Step4.After running quickstart.py (refer to the Google technical documentation for details), a credentials.json file will be generated.

### Step5.Before executing google_try_api.py, adjust the following parameters.


■■■■■■■■■■  adjust parameter  ■■■■■■■■■■

folder_id = '1opml0Gw3TYmXT1qid9LiX1yGKTaz688z'

//Paste the desired Google Drive folder ID where you want to place the items.


file_names = ['me.jpeg']

//Paste the desired files and their names.


mime_types = ['image/jpeg']

//Find corresponding mime_types from the following URL. Here, an image is used as an example, and you can upload any file as long as it is configured properly.

//https://learndataanalysis.org/commonly-used-mime-types/


media = MediaFileUpload('me.jpeg', mimetype='image/jpeg', resumable=True)

//Re-enter the filename and configure the data in the upload feature of the MediaFileUpload function, setting resumable to True.

■■■■■■■■■■  adjust parameter  ■■■■■■■■■■

