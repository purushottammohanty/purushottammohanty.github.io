---
title: 'Web Scraping Publications from Google Scholar'
excerpt: 'Extract title, citation count and year of publications for an author from Google Scholar.'
---

This post shows how to extract title (including co-authors and journal),
citation count and year of publication for all available publications
from an author profile in Google Scholar.

## Extract List of Faculty Names

For this example, I use names of Stanford Computer Science faculty
members .


## Function to Get Faculty Publications from Google Scholar

The below function first searches the corresponding researcher’s name in
Google Scholar and obtains the Google Scholar Author ID for the same.
Thereafter, it makes another request to obtain the list of publications
from the profile page. Google Scholar uses pagination and only shows up
the most cited 100 publications first. Another request is required to be
made for the next 100 publications. Since, repeated requests can cause
Google to temporarily block requests from an IP address or introduce a
CAPTCHA, the function below makes page requests with a 3 second delay.
Using this method, we extract the full title of the publication
including the names of co-authors and the journal it was published at.
Along with the title we also extract the year of publication and the
total citation count of the publication.

Finally, it appends all the data from all the pages and outputs a
dataframe. At the time of writing this post, the following method worked
without any issue however your mileage may vary depending on how many
requests you’re making and at what time you’re making them.


## Get Publications for all Authors

I use the author names that I extracted earlier to get all the
publications for all the faculties.


Note that some authors do not have a Google Scholar profile. In the
case, the function simply outputs a NULL value.