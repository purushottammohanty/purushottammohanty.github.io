This post shows how to extract title (including co-authors and journal),
citation count and year of publication for all available publications
from an author profile in Google Scholar.

## Extract List of Faculty Names

For this example, I use names of Stanford Computer Science faculty
members .

``` r
# Stanford CS Faculty
htmlpage = read_html("https://cs.stanford.edu/directory/faculty")

# regular faculty
faculty = htmlpage %>%
  html_elements(xpath = '//*[@id="node-113"]/div/div[1]/div/div/table[1]') %>%
  html_table() %>%
  .[[1]] %>%
  as.data.frame()

# dataframe headers
names(faculty) = c("name", "phone", "office", "email_prefix")
```

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

``` r
# function - get faculty publications with citations and year of publications
# using google scholar search and google scholar author profiles
# function takes one attribute - name of faculty
get_faculty_pubs = function(x){ 
  
  # tryCatch skips loops in case of an error (example, if the faculty has no Google Scholar profile)
  return(tryCatch({
    
    # get faculty name
    faculty_name = x
    
    # split name and tidy search string
    search_string = paste(str_split(faculty_name, " ")[[1]][1], 
                          str_split(faculty_name, " ")[[1]][2], 
                          sep = "+")
    
    # gc author search url
    gc_author_search_url = paste0(
      'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=',
      search_string, "&btnG=")
    
    # checks if author is available and gets its Google Scholar ID
    # get author search ID
    gc_author_id = read_html(gc_author_search_url) %>%
      html_elements(xpath = '//*[@id="gsc_sa_ccl"]/div/div/a') %>%
      .[[1]] %>%
      html_attr("href")
    
    # gc uses pagination with a maximum return of 100 entries 
    # loop over each page (I loop it over 5 pages or 500 entries) 
    # (most faculty don't have greater than 400 publications or above 300 
    #    there's repeated pubs or working papers without any citations or year)  
    gc_author_pubs = lapply(seq(0, 300, 100), function(i){
      
      # google scholar author profile url
      gc_author_url = paste0("https://scholar.google.com", gc_author_id,
                             "&oi=ao", "&cstart=", i, "&pagesize=100")
      
      # get html of author profile
      gc_author_html = read_html(gc_author_url)
      
      # get all publications of the author
      gc_author_pubs = gc_author_html %>%
        html_elements(xpath = '//*[@id="gsc_a_t"]') %>%
        html_table() %>%
        .[[1]]
      
      # fix column names
      names(gc_author_pubs) = c("publication", "citation_count", "year")
      
      # author affiliation for confirmation
      gc_author_affil = gc_author_html %>%
        html_elements(xpath = '//*[@id="gsc_prf_i"]/div[2]/a') %>%
        html_text()
      
      # add author affiliation
      gc_author_df = gc_author_pubs %>%
        mutate(author_affil = gc_author_affil)
      
      # add delay of 5 secs (to avoid Google detecting these requests)
      date_time = Sys.time()
      while((as.numeric(Sys.time()) - as.numeric(date_time))<3){}
      
      # get dataframe
      return(gc_author_df)
    })
    
    # append dataset from each page for the same author
    bind_rows(gc_author_pubs) %>%
      # remove unnecessary rows
      filter(!year %in% "Year") %>% 
      # add faculty name
      mutate(author = x) %>%
      # drop error message (after the last publication this error message gets added)
      filter(!year %in% "There are no articles in this profile.")
    
  }, error = function(e){NULL}))
  
}
```

## Get Publications for all Authors

I use the author names that I extracted earlier to get all the
publications for all the faculties.

``` r
# total number of faculty at Stanford with industry affiliation
n_fac_with_ind_affil = NROW(faculty[faculty$industry_affil == 1, 'name'])

# get publications for all such professors
df_final = lapply(1:n_fac_with_ind_affil, function(i){
  # faculty name
  fac_name = faculty[faculty$industry_affil == 1, 'name'][i]
  # get publications data frame using function built earlier
  get_faculty_pubs(fac_name)
})

# append all the data
df_final = bind_rows(df_final)
```

Note that some authors do not have a Google Scholar profile. In the
case, the function simply outputs a NULL value.
