import json

def main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    print(alphabetically_first_county(counties))
    print(percent_most_under_18(counties))
    print(county_most_under_18(counties))
    print(lowest_median_income(counties))
    print(high_income_counties(counties))
    print(state_with_most_counties(counties))
    print(your_interesting_demographic_function(counties))

def alphabetically_first_county(counties):
    """Return the county with the name that comes first alphabetically."""
    #Hint: you can use < to compare strings in Python. ex) "cat" < "dog" gives the value True
    first_county = counties[0]["County"]
    for county in counties:
        county["County"]
        if county["County"] < first_county:
            first_county = county["County"]
    return first_county
    
    
def percent_most_under_18(counties):
    """Return the highest percent of under 18 year olds."""  
    first_county = counties[0]["Age"]["Percent Under 18 Years"]
    for age in counties:
        age["Age"]["Percent Under 18 Years"]
        if age["Age"]["Percent Under 18 Years"] > first_county:
            first_county = age["Age"]["Percent Under 18 Years"]
    return first_county  
    

def county_most_under_18(counties):
    """Return the NAME of a county with the highest percent of under 18 year olds."""
    first_county = counties[0]["Age"]["Percent Under 18 Years"]
    county_name = ""
    for age in counties:
        age["Age"]["Percent Under 18 Years"]
        if age["Age"]["Percent Under 18 Years"] > first_county:
            first_county = age["Age"]["Percent Under 18 Years"]
            county_name = age["County"]
    return county_name
    
    
def lowest_median_income(counties):
    """Return a name of a county with the lowest median household income"""
    first_county = counties[0]["Income"]["Median Houseold Income"]
    county_name = ""
    for income in counties:
        income["Income"]["Median Houseold Income"]
        if income["Income"]["Median Houseold Income"] < first_county:
            first_county = income["Income"]["Median Houseold Income"]
            county_name = income["County"]
    return county_name
    
    
def high_income_counties(counties):
    """Return a LIST of the counties with a median household income over $90,000."""
    incomeList = []
    for income in counties:
        income["Income"]["Median Houseold Income"]
        if income["Income"]["Median Houseold Income"] > 90000:
            incomeList.append(income["County"])
    return incomeList


#To earn higher than a 3, complete one or both of the functions below
def state_with_most_counties(counties):
    """Return a state that has the most counties."""
    #1. Make a dictionary that has a key for each state and the values keep track of the number of counties in each state
    
    #2. Find the state in the dictionary with the most counties
    
    #3. Return the state with the most counties
    us_state_abbrev = {
        "AL": 0, 'AK': 0, 'AZ': 0, 'AR': 0,
        'CA': 0, 'CO': 0, 'CT': 0,
        'DE': 0,
        'FL': 0,
        'GA': 0,
        'HI': 0,
        'ID': 0, 'IL': 0, 'IN': 0, 'IA': 0,
        'KS': 0, 'KY': 0,
        'LA': 0,
        'ME': 0, 'MD': 0, 'MA': 0, 'MI': 0, 'MN': 0, 'MS': 0, 'MO': 0, 'MT': 0,
        'NE': 0, 'NV': 0, 'NH': 0, 'NJ': 0, 'NM': 0, 'NY': 0, 'NC': 0, 'ND': 0,
        'OH': 0, 'OK': 0, 'OR': 0,
        'PA': 0,
        'RI': 0,
        'SC': 0, 'SD': 0,
        'TN': 0, 'TX': 0,
        'UT': 0,
        'VT': 0, 'VA': 0,
        'WA': 0, 'WV': 0, 'WI': 0, 'WY': 0
    }
    for key in us_state_abbrev:
        for state in counties:
            if key == state["State"]:
                us_state_abbrev[key] = us_state_abbrev[key]+1
    
    most_counties = "test"
    amount = 0
    for x in us_state_abbrev:
        if amount < us_state_abbrev[x]:
            amount = us_state_abbrev[x]
            most_counties = x

    return most_counties
    
def your_interesting_demographic_function(counties):
    """Compute and return an interesting fact using the demographic data about the counties in the US."""
    averageGrad = 0
    numCounties = 0
    for num in counties:
        numCounties = numCounties+1
    print(numCounties)
    numGrads = 0;
    for grads in counties:
       numGrads = numGrads + grads["Education"]["High School or Higher"]
    averageGrad = numGrads/numCounties
    return averageGrad

if __name__ == '__main__':
    main()
