import requests
import json
import os
#whenever the term "other" is used, it's to signify the 
#other person in the one-on-one

#Add Action Network 'OSDI-API-Token' wherever it says "Add 'OSDI-API-Token' here"

def an_post(user_first, user_last, user_email, 
            other_first, other_last, other_email, description):
    
    # API_Token = #Add 'OSDI-API-Token' here
   
    payload = {	
        "title": "1-on-1: {} {} - {} {} : {}".format(user_first, user_last, 
                                                     other_first, other_last, 
                                                     description),
        "origin_system": "One-on-one",
        "description": description
    }
    
    request = requests.post('https://actionnetwork.org/api/v2/forms/', 
                            headers = {'OSDI-API-Token': os.environ.get("ACTION_NETWORK_API_TOKEN"), 
                            'Content-Type': 'application/json'}, 
                            params = payload)
    
    response = json.loads(request.text)
    submission_endpoint = response['_links']['osdi:submissions']['href']
    form_endpoint = response['_links']['self']['href']
    
    payload = {"person" : 
        {"family_name" : user_last,
        "given_name" : user_first,
        "email_addresses" : 
            [{ "address" : user_email }]
        }
    }
    
    request = requests.post(submission_endpoint, 
                            headers = {'OSDI-API-Token': os.environ.get("ACTION_NETWORK_API_TOKEN"), 
                                       'Content-Type': 'application/json'}, 
                            data =json.dumps(payload))

    payload = {"person" : 
        {"family_name" : other_last,
        "given_name" : other_first,
        "email_addresses" : 
            [{ "address" : other_email }]
        }
    }
    
    request = requests.post(submission_endpoint, 
                            headers = {'OSDI-API-Token': os.environ.get("ACTION_NETWORK_API_TOKEN"), 
                                       'Content-Type': 'application/json'}, 
                            data =json.dumps(payload))
    
    response = json.loads(request.text)
    other_endpoint = response["_links"]["osdi:person"]["href"]
    submission_status_code = request.status_code
    
    return submission_status_code, form_endpoint, other_endpoint, other_first, other_last, other_email, description
    

def an_put(form_endpoint, other_endpoint, 
           user_first, user_last, user_email, 
           other_first, other_last, other_email):
    
    #API_Token = #Add 'OSDI-API-Token' here
    
    payload = {	
        "title": "1-on-1: {} {} - {} {} : {}".format(user_first, user_last, 
                                                     other_first, other_last, 
                                                     description),
        "origin_system": "One-on-one",
        "description": description
    }
    
    request = requests.put(form_endpoint, 
                           headers = {'OSDI-API-Token': os.environ.get("ACTION_NETWORK_API_TOKEN"), 
                                      'Content-Type': 'application/json'}, 
                           data = json.dumps(payload))
    
    form_status_code = request.status_code
    
    payload = {
        "family_name" : other_last,
        "given_name" : other_first,
        "email_addresses" : 
            [{ "address" : other_email }]
    }
    
    request = requests.put(other_endpoint, 
                           headers = {'OSDI-API-Token': os.environ.get("ACTION_NETWORK_API_TOKEN"), 
                                      'Content-Type': 'application/json'}, 
                           data =json.dumps(payload))
    
    other_status_code = request.status_code
    
    return form_status_code, other_status_code
    
#the stuff below is for testing

#This is for testing the POST requests

"""
user_first = input("What's your first name? ")
user_last = input("What's your last name? ")
user_email = input("What's your email address? ")
other_first = input("What's the other person's first name? ")
other_last = input("What's the other person's last name? ")
other_email = input("What's the other person's email address? ")
description = input("Write a SHORT description of the one-on-one, KIND reflections on your partner. ")

#testing the original POST request
submission_status_code, form_endpoint, other_endpoint, other_first, other_last, other_email, description = an_post(user_first, user_last, user_email, other_first, other_last, other_email, description)
print("POST request status code: " + str(submission_status_code))
"""

#this is for testing the PUT requests, form and person submission respectively
#The way it works right now, have to do it in the same run as the code above
#have to change some of the parameters for this code to be a meaningful test
#I did test it this way and it worked.

"""
other_first = input("What's the other person's first name? ")
other_last = input("What's the other person's last name? ")
other_email = input("What's the other person's email address? ")
description = input("Write a SHORT description of the one-on-one, KIND reflections on your partner. ")

print("Form and submission PUT request status codes, respectively: " + str(an_put(form_endpoint, other_endpoint, user_first, user_last, user_email, other_first, other_last, other_email)))
"""
