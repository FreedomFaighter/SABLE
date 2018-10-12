#Name:            s1_download.py
#Purpose:         Download PDFs discovered during web crawling
#Python Version:  3

import codecs
import csv
import os
import re

#Name:       is_pdf
#Arguments:  url
#            metadata
#Purpose:    Determine whether the URL points to a PDF

def is_pdf(url, metadata):
    urlmatch = re.search(r"^(\S+)\.([pP][dD][fF])$", url)
    metadatamatch = re.search(r"Content-Type:application/pdf", metadata)
    return urlmatch or metadatamatch

#Name:       download_pdf
#Arguments:  url
#            projname
#Purpose:    Download the PDF

def download_pdf(url, projname):
    #Use the Linux/Unix utility wget to download the PDF
    os.system("wget --no-check-certificate -nv -P /" + projname + "/download/ " + url)
    return

def main():
    #Project name
    projname = "project"
    
    #Read in the list of URLs crawled by Apache Nutch and download the PDFs
    f = codecs.open("/" + projname + "/dump/dump.csv", "rU")
    rdr = csv.DictReader(f)
    for row in rdr:
        if is_pdf(row["Url"], row["Metadata"]):
            download_pdf(row["Url"], projname)
    f.close()
    
    return

if __name__ == "__main__":
    main()