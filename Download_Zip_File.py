import requests
import zipfile


def zip_file(url):
    response = requests.get(url)
    with open("file.zip", "wb") as f:
        f.write(response.content)

zip_file("http://download.geonames.org/export/zip/AD.zip")

with zipfile.ZipFile("file.zip","r") as zip_ref:
    zip_ref.extractall("targetdir")