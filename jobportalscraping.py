import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import time
from datetime import datetime
from datetime import date
today = date.today()
now = datetime.now()

columns = ["jobportal","accessdate","title", "company", "location", "jobtype", "salary"]
sample_df = pd.DataFrame(columns = columns)
accessdate= now.strftime("%Y-%m-%d %H:%M:%S")
count = 0
jobportal="Monster"
jobqueries = ["Software-Programmer","IT-Recruiter","Database-Administrator","Big-Data-Engineer","Adjunct-Professor","Reports-Developer","Data-Scientist","Business-Application-Developer",
				"Microservices-Developer","Computer-Scientist","Technical-Writer","Business-Development-Manager","Systems-Analyst","Hadoop-Administrator", "Senior-Business-Intelligence-Reports-Developer",
				"Cloud-Solution-Architect", "Microservices-Software-Engineer", "Site-Reliability-Engineer", "Quality-Assurance-Engineer", "Research-and-Data-Analyst", "Mathematics-Professor", 
				"Software-Tester","Cloud-Developer","AI-Developer","Java-Developer","Python-Developer","PHP-Developer"]
joblocations = ["San-Antonio__2C-TX","Austin__2C-TX","Chicago__2C-IL","Miami__2C-FL","Mclean__2C-VA","New-York__2C-NY","Los-Angeles__2C-CA","Sacramento__2C-CA","Orlando__2C-FL","Colorado-Springs__2C-CO"]
urls=[]
for joblocation in joblocations:
	for jobquery in jobqueries:
		urls.append("https://www.monster.com/jobs/search/?q="+jobquery+"&where="+joblocation+"&intcid=skr_navigation_nhpso_searchMain")
for URL in urls:
	page = requests.get(URL)
	time.sleep(1)  
	soup = BeautifulSoup(page.text, "html.parser")
	resultsCol = soup.find("div",id="SearchResults")
	if resultsCol is None:
		print(soup.prettify())
	else:
		jobResults = resultsCol.findAll('section',attrs={'class': 'card-content'})	
		for jobResult in jobResults:
			job_post = []
			publishtime = jobResult.findAll('time')
			if len(publishtime)>0:
				publishtime = publishtime[0].text.strip()
			else:
				publishtime = ""
			title = jobResult.findAll('h2',attrs={'class': 'title'})
			if len(title)>0:
				title = title[0].text.strip()
			else:
				title = ""
			company = jobResult.findAll('div',attrs={'class': 'company'})
			if len(company)>0:
				company = company[0].text.strip()
			location = jobResult.findAll('div',attrs={'class': 'location'})
			if len(location)>0:
				location = location[0].text.strip()
			jobtype = ""
			salary = ""
			job_post=[jobportal,accessdate,title,company,location,jobtype,salary]
			sample_df.loc[count] = job_post
			count=count+1
jobportal="CareerBuilder"
jobqueries = ["IT+Recruiter","Data+Scientist","Software+Programmer","Database+Administrator","Reports+Developer","Big+Data+Engineer","Java+Developer","Microservices+Developer","Business+Application+Developer",
				"Microservices+Developer","Computer+Scientist","Technical+Writer","Business+Development+Manager","Systems+Analyst","Hadoop+Administrator", "Senior+Business+Intelligence+Reports+Developer",
				"Cloud+Solution+Architect", "Microservices+Software+Engineer", "Site+Reliability+Engineer", "Quality+assurance+Engineer", "Research+and+Data+Analyst", "Mathematics+Professor", 
				"Software+Tester","Cloud+Developer","AI+Developer","Java+Developer","Python+Developer","PHP+Developer"]
joblocations = ["Austin%2C+TX","Dallas%2C+TX","Houston%2C+TX","San+Antonio%2C+TX","New+York%2C+NY","Mclean%2C+VA","Sacramento%2C+CA","Jackson%2C+MI","Atlanta%2C+GA",
				"Miami%2C+FL","Orlando%2C+FL","Portland%2C+OR","Seattle%2C+WA","Mountain+View%2C+CA"]
urls=[]
for joblocation in joblocations:
	for jobquery in jobqueries:
		urls.append("https://www.careerbuilder.com/jobs?utf8=?&keywords="+jobquery+"&location="+joblocation)
for URL in urls:
	page = requests.get(URL)
	time.sleep(1)  
	soup = BeautifulSoup(page.text, "html.parser")
	resultsCol = soup.find("div",id="jobs_collection")
	if resultsCol is None:
		print(soup.prettify())
	else:
		jobResults = resultsCol.findAll('div',attrs={'class': 'data-results-content-parent relative'})	
		for jobResult in jobResults:
			job_post = []
			publishtime = jobResult.findAll('div',attrs={'class': "data-results-publish-time"})
			title = jobResult.findAll('div',attrs={'class': 'data-results-title'})[0].text.strip()
			dataDetail = jobResult.findAll('div',attrs={'class': 'data-details'})[0]
			dataDetails = dataDetail.findAll('span')
			if len(dataDetails)>2:
				company = dataDetails[0].text.strip()
				location = dataDetails[1].text.strip()
				jobtype = dataDetails[2].text.strip()
			else:
				company = ""
				location = ""
				jobtype = ""
			salary=""
			job_post=[jobportal,accessdate,title,company,location,jobtype,salary]
			sample_df.loc[count] = job_post
			count=count+1
city = "Texas"
jobquery="IT%20Recruiter"
jobportal="Indeed"
URL = "https://www.indeed.com/jobs?q="+jobquery+"&l="+city+""
cities=["Seattle%2C+WA","Atlanta%2C+GA","Sacramento%2C+CA","Denver%2C+CO","Chicago%2C+IL","Mclean%2C+VA","Orlando%2C+FL","New+York%2C+NY","San+Antonio%2C+TX","Austin%2C+TX","Houston%2C+TX","Dallas%2C+TX"]
jobqueries=["IT%20Recruiter","Database%20Administrator","Software%20Programmer","Project%20Manager","Crystal%20Reports%20Developer","Big%20Data%20Analyst","Big%20Data%20Engineer",
				"Business%20Application%20Developer","Microservices%20Developer","Computer%20Scientist","Technical%20Writer","Business%20Development%20Manager","Systems%20Analyst","Hadoop%20Administrator", 
				"Senior%20Business%20Intelligence%20Reports%20Developer","Cloud%20Solution%20Architect", "Microservices%20Software%20Engineer", "Site%20Reliability%20Engineer", "Quality%20assurance%20Engineer", 
				"Research%20and%20Data%20Analyst", "Mathematics%20Professor", "Software%20Tester","Cloud%20Developer","AI%20Developer","Java%20Developer","Python%20Developer","PHP%20Developer"]
urls=[]
for city in cities:
	for jobquery in jobqueries:
		urls.append("https://www.indeed.com/jobs?q="+jobquery+"&l="+city+"")
for URL in urls:
	page = requests.get(URL)
	time.sleep(1)  
	soup = BeautifulSoup(page.text, "html.parser")
	resultsCol = soup.find("td", {"id": "resultsCol"})
	if resultsCol is None:
		print(soup.prettify())
	else:
		jobCards = resultsCol.findAll(attrs={'class': 'jobsearch-SerpJobCard'})
		for jobCard in jobCards:
			job_post = []
			for a in jobCard.findAll(name="a", attrs={"data-tn-element":"jobTitle"}):
				title = a.text.strip()
			company = jobCard.findAll(attrs={"class":"company"})
			if len(company) > 0:
				company = company[0].text.strip()
			else: 
				company = ""
			location = jobCard.findAll(attrs={"class":"recJobLoc"})
			if len(location) > 0:
				location = location[0].text.strip()
			else: 
				location = jobCard.findAll(attrs={"class":"location"})
				if len(location) > 0:
					location = location[0].text.strip()
				else:
					location = ""
			salary = jobCard.findAll(attrs={"class":"salaryText"})
			if len(salary) > 0:
				salary = salary[0].text.strip()
			else:
				salary = ""
			job_post = [jobportal,accessdate,title,company,location,jobtype, salary]
			sample_df.loc[count] = job_post
			count=count+1
sample_df.to_csv("jobscraping.csv", encoding='utf-8')
