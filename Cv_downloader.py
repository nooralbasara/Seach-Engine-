#!/bin/env python
#
#

import sys
import gdown

DOWNLOAD_FOLDER="./CVs/"

def main():
    with open('download_links.txt','r') as g_links:
        for g_link in g_links:
            g_link = g_link.replace('\n','')
            if  "/folders/" in g_link:
                gdown.download_folder(g_link,output=DOWNLOAD_FOLDER,quiet=False,remaining_ok=True)
            else:
                gdown.download(g_link,output=DOWNLOAD_FOLDER,quiet=False)

if __name__ == '__main__':
    main()