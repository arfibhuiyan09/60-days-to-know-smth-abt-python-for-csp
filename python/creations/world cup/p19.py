world_cup_winners = {
    "1930": "Uruguay",
    "1934": "Italy",
    "1938": "Italy",
    "1950": "Uruguay",
    "1954": "West Germany",
    "1958": "Brazil",
    "1962": "Brazil",
    "1966": "England",
    "1970": "Brazil",
    "1974": "West Germany",
    "1978": "Argentina",
    "1982": "Italy",
    "1986": "Argentina",
    "1990": "West Germany",
    "1994": "Brazil",
    "1998": "France",
    "2002": "Brazil",
    "2006": "Italy",
    "2010": "Spain",
    "2014": "Germany",
    "2018": "France",
    "2022": "Argentina"
}

world_cup_hosts = {
    "1930": "Uruguay",
    "1934": "Italy",
    "1938": "France",
    "1950": "Brazil",
    "1954": "Switzerland",
    "1958": "Sweden",
    "1962": "Chile",
    "1966": "England",
    "1970": "Mexico",
    "1974": "West Germany",
    "1978": "Argentina",
    "1982": "Spain",
    "1986": "Mexico",
    "1990": "Italy",
    "1994": "United States",
    "1998": "France",
    "2002": "South Korea and Japan",
    "2006": "Germany",
    "2010": "South Africa",
    "2014": "Brazil",
    "2018": "Russia",
    "2022": "Qatar",
    "2026": "United States, Canada, and Mexico",
    "2030": "Morocco, Portugal, and Spain (plus centenary matches in Uruguay, Argentina, and Paraguay)",
    "2034": "Saudi Arabia"
}

def WClookup():
    choice = input("type a year to see who won the FIFA world cup during that year. ").lower().strip()
    if choice in world_cup_winners:
        country = world_cup_winners[choice]
        print(country)
    else:
        print(f"--> Error: There was no FIFA mens World Cup tournement during {choice}!")

def WChostlookup():
    choice1 = input("type a year to see who hosted the FIFA world cup during that year. ").lower().strip()
    if choice1 in world_cup_hosts:
        country = world_cup_hosts[choice1]
        print(country)
    else:
        print(f"--> Error: There was no FIFA mens World Cup tournement during {choice1}!")

while True:
    decision = input("do you want to see the hosts or winners of each world cup (or quit) 'winner' or 'hosts' or 'Q' ").lower().strip()
    if decision == "winner":
        WClookup()
    elif decision == "hosts":
        WChostlookup()
    elif decision == "q":
        print("oka")
        break
    else:
        print(f"--> Error: '{decision}' is an invalid prompt answer!")