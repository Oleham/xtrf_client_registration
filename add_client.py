import requests, os, sys, json, pprint 


categoryOle = 172
categoryNysalg = 173
branchNorge = 3
salesPersonOle = 79
projectManagerPia = 48

def access_api():
    login_url = 'localhost:8000/api-auth/login/'
    api_url = 'localhost:8000/api/companies/' 

    username = os.environ.get("API_USER")
    password = os.environ.get("API_PASSWORD")
    #Get dictionary from API
    s = requests.Session()
    response = s.get(login_url)
    csrftoken = response.cookies['csrftoken']
    login_data = {'username': username, 'password': password, 'csrfmiddlewaretoken': csrftoken}
    headers = {"Referer": login_url}
    s.headers.update(headers)

    response2 = s.post(login_url, data=login_data, )
    response3 = s.get(api_url)

    return json.loads(response3.text)

def post_to_xtrf(company):
    name = company['name']
    fullName = company['name']
    primary = company['email']
    phones = [company['phone_number']]
    addressLine1 = company['adressLine1'] #Notice the misspelling in the API
    addressLine2 = company['adressLine2']
    postalCode = company['area_code']
    city = company['city']
    countryId = company['country_id']
    orgnumber = company['idNumber']

    #Logic to get right categories
    if countryId == 209:
        #Sverige
        salesPersonId = 70 #Maria Z.
        projectManagerId =  77 #Sofie N.
        categoriesIds = [173] #Categories Nysalg
        branchId = 2
        taxType = "Momsnr."

    elif countryId == 60:
        #Danmark
        salesPersonId = 42 #Anne D.
        projectManagerId =  66 #Nina S.
        categoriesIds = [173] #Categories Nysalg
        branchId = 5
        taxType = "CVR"

    elif countryId == 165:
        #Norge
        salesPersonId = 79 #Ole H.
        projectManagerId =  48 #Pia L.
        categoriesIds = [172, 173] #Categories Ole and Nysalg
        branchId = 3
        taxType = "Orgnr"

    #Construct the body
    body = {
    "name": name,
    "fullName": fullName,
    "contact": {
        "phones": phones,
        "emails": {
        "primary": primary
        },
    },
    "accounting": {
        "taxNumbers": [{"number": orgnumber, "type": taxType}]
    },
    "billingAddress": {
        "addressLine1": addressLine1,
        "addressLine2": addressLine2,
        "city": city,
        "postalCode": postalCode,
        "countryId": countryId
    },
    "categoriesIds": categoriesIds,
    "branchId": branchId,
    "responsiblePersons": {"accountManagerId": None,
                            "projectCoordinatorId": None,
                            "projectManagerId": projectManagerId,
                            "salesPersonId": salesPersonId
                            }
                        }
    
    #Construct the headers
    hpURL = "https://xtrf.exampleexamplecom/home-api"
    header = {"X-AUTH-ACCESS-TOKEN": os.environ.get("XTRF_ACCESS_TOKEN")}
    js = json.dumps(body)
    newHeaders = {'Content-type': 'application/json'}

    with requests.Session() as s:
        s.headers.update(header)
        resp = s.post(hpURL + "/customers/", data=js, headers=newHeaders)
        print(resp.text)
        resp.raise_for_status()

        customj = json.loads(resp.text)

        pprint.pprint(customj)


## HER STARTER VI
if len(sys.argv) != 2:
    print("Usage: 'add_client.py <integer>'")
else:
    companyDict = access_api() 
    for company in companyDict:
        if str(company["id"]) == sys.argv[1]:
            post_to_xtrf(company)
            
            
            
