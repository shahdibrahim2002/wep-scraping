# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests
import bs4

jop_titles=[]
company_names=[]
locations_names=[]
job_skills=[]
space=[]
Links=[]
page_num=0
while True:
  result =requests.get(f"https://wuzzuf.net/search/jobs/?a=spbg&q=front-end={page_num}")
  src=result.content

  soup=bs4.BeautifulSoup(src,"lxml")

  jop_titles=soup.find_all( "h2",{"class":"css-m604qf"})

  company_names=soup.find_all("a",{"class":"css-17s97q8"})

  locations_names=soup.find_all("span",{"class":"css-5wys0k"})

  job_skills=soup.find_all("div",{"class":"css-y4udm8"})

  for i in range(len(jop_titles)):
    jop_titles.append(print("jop_titles :"+jop_titles[i].text))
    company_names.append(print("company_names: "+company_names[i].text))
    locations_names.append(print("locations_names:"+locations_names[i].text))
    job_skills.append(print("job_skills:"+job_skills[i].text))
    Links.append(print("links:"+jop_titles[i].find("a").attrs['href']))
    space.append(print("-----------------------------------------------------------------------------"))
  page_num+=1
  if page_num>=221:
    break





#file_list=[ jop_titles,company_names, locations_names,job_skills]
#exported = zip_logest(*file_list)
#with open ("/user/islam/ducoments/jobstest.csv" ,"w") as python:
    #wr=csv.writer(python)
    #wr.writerow([ "jop_titles","company_names", "locations_names","job_skills"])
