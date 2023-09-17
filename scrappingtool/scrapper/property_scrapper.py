from .models import Property
import requests
from bs4 import BeautifulSoup

def scrape_and_save_property_data():
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }
    urls=[
    "https://www.99acres.com/search/property/buy/pune?keyword=pune&preference=S&area_unit=1&budget_min=0&res_com=R&isPreLeased=N",
    "https://www.99acres.com/search/property/buy/delhi?keyword=delhi&preference=S&area_unit=1&budget_min=0&res_com=R&isPreLeased=N",
    "https://www.99acres.com/search/property/buy/mumbai?keyword=Mumbai&preference=S&area_unit=1&budget_min=0&res_com=R&isPreLeased=N",
    "https://www.99acres.com/search/property/buy/lucknow?city=205&preference=S&area_unit=1&budget_min=0&res_com=R&isPreLeased=N",
    "https://www.99acres.com/search/property/buy/agra?keyword=Agra&preference=S&area_unit=1&budget_min=0&res_com=R&isPreLeased=N",
    "https://www.99acres.com/search/property/buy/ahmedabad-all?city=45&preference=S&area_unit=1&budget_min=0&res_com=R&isPreLeased=N",
    "https://www.99acres.com/search/property/buy/kolkata?keyword=kolkata&preference=S&area_unit=1&budget_min=0&res_com=R&isPreLeased=N",
    "https://www.99acres.com/search/property/buy/jaipur?keyword=jaipur&preference=S&area_unit=1&budget_min=0&res_com=R&isPreLeased=N",
    "https://www.99acres.com/search/property/buy/chennai?keyword=chennai&preference=S&area_unit=1&budget_min=0&res_com=R&isPreLeased=N",
    "https://www.99acres.com/search/property/buy/bengaluru?keyword=bengaluru&preference=S&area_unit=1&budget_min=0&res_com=R&isPreLeased=N"
    ]
    city=["Pune","Delhi","Mumbai","Lucknow","Agra","Ahmedabad","Kolkata","Jaipur","Chennai","Bengaluru"]
    state=[" Maharashtra","Delhi"," Maharashtra","Uttar Pradesh","Uttar Pradesh","Gujarat","West Bengal","Rajasthan","Tamil Nadu","Karnataka"]
    j=0
    for url in urls:
        page=requests.get(url,headers=headers)
        soup=BeautifulSoup(page.content,"html.parser")
        results=soup.find_all("div",class_="srpTuple__tupleDetails")
        for element in results:
            try:
              d=dict()
              d["property_link"]=element.find("a",class_="body_med srpTuple__propertyName")["href"]
              d["property_name"]=element.find("h2",class_="srpTuple__tupleTitleOverflow").text.strip()
              d["property_city"]=city[j]
              d["property_area"]=element.find(id="srp_tuple_primary_area").text.strip()
              d["property_cost"]=element.find(id="srp_tuple_price").text.strip()
              d["property_type"]=element.find(id="srp_tuple_bedroom").text.strip()
              d["property_locality"]=d["property_name"][d["property_name"].index("in")+2:]
              Property.objects.create(name=d["property_name"],cost=d["property_cost"],property_type=d["property_type"],area=d["property_area"],link=d["property_link"],city=d["property_city"],locality=d["property_locality"])
            except:
                continue
        j+=1
        