---
permalink: /projects/
title: "Projects"
---

# Project 1 	 	 	
# Translate using Google Cloud Platform (GCP) Translation API.  		

This is a short write-up for beginners who want to use the Google Cloud Platform (GCP) Translation Client API to translate one or multiple variables from a dataset. 		
			
The [GCP Translate API]("https://cloud.google.com/translate") can be used for quick and effective translation. The Basic API is free to use upto 500,000 characters per month and thereafter carries a cost of 20 USD for each 1 million character. There are also advanced, media and auto ML translate APIs which is beyond the scope of the article. Note that if you translate a string or text without specifying the source language, the characters are only counted once towards the quota. There's no additional cost of detecting the language. However, explicitly detecting source language count towards the quota. 		
			
Google provides an official translation API for Python and that is what the following blog uses. First of all we are going to setup a GCP account and create our credentials.   		
			
1. Go to [Google Cloud]("https://cloud.google.com") and sign in using your Google Account.  
2. Once you are in your dashboard, go to the top bar and create a new project.      
3. Then click billing and then setup billing for the project. You would ideally need your credit card to set it up. (Don't worry you will not be charged for any request beyond your quota unless to move to a paid account. The APIs will provide an error if you exceed your quota and will not proceed further without converting to a paid account.) Additionally, at the time of writing this post, Google provided a joining credit of 300 USD which can be used.          
4. Once billing has been setup, select the "APIs and Services" option in the right side menu and search for "Translate API" and click "Enable".  
5. Select "IAM and Admin" and then "Service Account".       
6. Create a Service Account and then create keys. (The keys automatically get downloaded as a json file. You cannot download the keys again so keep it somewhere safe in your local machine.)


### Import Necessary Packages
```
import pandas as pd
import numpy as np
import json
from google.cloud import translate
```

### Setup GCP Client Credentials
```
client_credentials = json.load(open("FULL_PATH_TO_KEY.json"))

# set project id and build client
project_id = client_credentials['project_id']
assert project_id
parent = f"projects/{project_id}"
client = translate.TranslationServiceClient()
```

### Getting all Language Codes
```
# Get all languages
response = client.get_supported_languages(parent=parent, display_language_code="en")
languages = response.languages

print(f" Languages: {len(languages)} ".center(60, "-"))
for language in languages:
    print(f"{language.language_code}\t{language.display_name}")
```

### Translate Example
```
# GCP translate
sample_text = ["Bonjour", "Oui"]
target_language_code = "en"

response = client.translate_text(
    contents= sample_text,
    target_language_code=target_language_code,
    parent=parent,
)

for translation in response.translations:
    print(translation.translated_text)
```

[here](/assets/md_pages/gcp_translate.md)


------------------------------------------------		

# Project 2



