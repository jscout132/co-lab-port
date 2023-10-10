import requests, datetime

# start top 5 most recent birds
recent_url = "https://api.ebird.org/v2/data/obs/US-NC/recent"

payload={}
headers = {
  'X-eBirdApiToken': 'if3r105uacv7'
}

full_response = requests.request("GET", recent_url, headers=headers, data=payload).json()

how_many_response = [i for i in full_response if 'howMany' in i]

# sorting by quantity of birds reported
sorted_response_list = sorted(how_many_response, key=lambda x: x['howMany'])
top_five_birds = sorted_response_list[-6:-1]

# end top 5 most recent birds
# ------------------------------------------------------------------------------------------

# start top 3 contributors in NC of the day

x = datetime.datetime.now()
# automating url to update daily
contributors_url = f"https://api.ebird.org/v2/product/top100/US-NC/{x.year}/{x.month}/{x.day}"
response = requests.request("GET", contributors_url, headers=headers, data=payload).json()

top_contributors = sorted(response, key=lambda x: x['numSpecies'])
top_three_contributors = top_contributors[-4:-1]

print(top_three_contributors)
# end top 3 contributors in NC of the day
# ------------------------------------------------------------------------------------------
