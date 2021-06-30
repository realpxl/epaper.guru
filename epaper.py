import requests
from merge import merge_pdf

url = "https://edb.reader.epaper.guru/de-CH/viewer/24a9e7d6-16cc-4a19-9594-b34f91a9c792"

s = requests.Session()

resp = s.get(url)
r= (resp.text)



ut = "url_template"
us = "url_suffix"
pg = "var pageCount = "

pg_pos = r.find(pg) + len(pg)
pg_end = r.find(";",pg_pos)
page_count = int(r[pg_pos:pg_end])

print(page_count)


url_template_pos = r.find(ut,pg_pos) + len(ut+" = '//")
url_template_end = r.find(";",url_template_pos)-2

 
url_template = r[url_template_pos:url_template_end]

url_suffix_pos = r.find(us,url_template_pos)+len(us+" = '")
url_suffix_end = r.find(";",url_suffix_pos)-1

url_suffix = r[url_suffix_pos:url_suffix_end]

print(url_template)
print(url_suffix)


for i in range (1,page_count+1):
 pdf_url = "https://" + url_template + "/" + str(i) + "/5.pdf?" + url_suffix;
 pdf = s.get(pdf_url);
 print(pdf_url)
 filename = str(i) + ".pdf"
 print(filename)
 with open(filename,'wb') as output_file:
     output_file.write(pdf.content)
 

merge_pdf(page_count)


