# import requests 


# url = 'https://sbmjed-my.sharepoint.com/personal/e004965_sbm_com_sa/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fe004965%5Fsbm%5Fcom%5Fsa%2FDocuments%2FDesktop%2FAramco&ga=1' # put the url


# r = requests.get(url, allow_redirects=True)

# open('sbmjed.aspx', 'wb').write(r.content) # change based on the url

from onedrivedownloader import download

url = 'https://drive.google.com/drive/folders/1GxY9CPwZ0tzJIMcBykCquZwKltYWN53n'

#download(url: str, file_name: str, unzip=False, unzip_path: str = None, force_download=False, force_unzip=False, clean=False)

download (url, filename = "CVs//", unzip=True, unzip_path="./data")

