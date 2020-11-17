from queries import lookup_select

# Doing the actual lookup. Does a select, and comparing it to the input values.
data = lookup_select()
count = 0
while True:    
    search = input("input a search term:")
    for row in data:
        URL = row['Website_URL']
        TITLE = row['Website_title']
        BODY = row['site_body']
        if str(search.lower()) in str(URL.lower()) or str(search.lower()) in str(TITLE.lower()) or str(search.lower()) in str(BODY.lower()):
            count += 1
            print(URL, TITLE)
    print("Total search result is: " + str(count))
 





