@ECHO OFF
start cmd.exe C:\Python\DjangoGB\env\Scripts\activate.bat
python C:\Python\DjangoGB\geekshop\manage.py runserver
start C:\"Program Files (x86)"\Google\Chrome\Application\chrome.exe "http://127.0.0.1:8000/"