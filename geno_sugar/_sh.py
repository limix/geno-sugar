import os
import sys
import zipfile

def download(url):

    if sys.version_info < (3,):
        from urllib import urlretrieve
        from urlparse import urlparse
    else:
        from urllib.request import urlretrieve
        from urllib.parse import urlparse

    urlretrieve(url, os.path.basename(urlparse(url).path))


def unzip(filepath):

    zip_ref = zipfile.ZipFile(filepath, "r")
    zip_ref.extractall(".")
    zip_ref.close()
