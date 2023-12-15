from googleapiclient.http import MediaFileUpload
from Google import Create_Service

CLIENT_SECRET_FILE = 'credentials.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
#print(dir(service))
folder_id = '1opml0Gw3TYmXT1qid9LiX1yGKTaz688z'
file_names = ['me.jpeg']
mime_types = ['image/jpeg']

for file_name, mime_type in zip(file_names, mime_types):
    file_metadata = {
        'name': file_name,
        'parents':[folder_id]
    }
    #media = MediaFileUpload('./fishbone_original/{0}'.format(file_name), mimetype=mime_type)
    #media = MediaFileUpload(f'{C:\\Users\\88697\\Desktop\\fishbone_original}\\{me.jpeg}', resumable=True)
    media = MediaFileUpload('me.jpeg', mimetype='image/jpeg', resumable=True)
    service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()