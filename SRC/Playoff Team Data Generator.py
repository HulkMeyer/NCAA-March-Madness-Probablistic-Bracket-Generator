import random
import pandas as pd
from datetime import datetime

# Countries list for team names
def get_countries():
    # List of all countries in the world
    countries = [
        "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", 
        "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", 
        "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", 
        "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", 
        "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros", "Congo", 
        "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", 
        "Dominican Republic", "East Timor", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", 
        "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", 
        "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", 
        "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", 
        "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", 
        "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", 
        "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", 
        "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", 
        "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", 
        "North Korea", "North Macedonia", "Norway", "Oman", "Pakistan", "Palau", "Palestine", "Panama", 
        "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", 
        "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", 
        "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", 
        "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Korea", 
        "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan", 
        "Tajikistan", "Tanzania", "Thailand", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", 
        "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States", 
        "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"
    ]
    return countries

def generate_playoff_data():
    # Initialize empty list to store all data
    all_data = []
    
    # Years from 2000 to 2025
    years = range(2000, 2026)
    
    # Regions
    regions = ["North", "South", "East", "West"]
    
    for year in years:
        # Get a new shuffled list of countries for each year
        countries = get_countries()
        random.shuffle(countries)
        
        # Ensure we have enough countries (we need 64)
        if len(countries) < 64:
            raise ValueError(f"Not enough countries available: {len(countries)}")
        
        # Select the first 64 countries for this year
        selected_countries = countries[:64]
        
        # Assign seeds and regions
        team_counter = 0
        
        for region in regions:
            for seed in range(1, 17):  # Seeds 1-16
                team = selected_countries[team_counter]
                team_counter += 1
                
                # Generate random stats according to requirements
                wins = random.randint(25, 160)
                losses = 162 - wins
                win_loss_percentage = wins / 162
                conference_finish = random.randint(1, 8)
                runs_scored = random.randint(250, 1000)
                # Ensure runs_allowed is less than runs_scored
                runs_allowed = random.randint(250, runs_scored)
                
                # Generate random ages with decimals
                batters_age = round(random.uniform(25, 32), 1)
                pitchers_age = round(random.uniform(25, 32), 1)
                
                # Generate random player counts
                players_used = random.randint(38, 65)
                pitchers_used = random.randint(15, 40)
                
                # Append data to the list
                all_data.append({
                    "Season": year,
                    "Region": region,
                    "Seed": seed,
                    "Team": team,
                    "Games": 162,
                    "Wins": wins,
                    "Losses": losses,
                    "Win-Loss Percentage": win_loss_percentage,
                    "Conference Finish": conference_finish,
                    "Runs Scored": runs_scored,
                    "Runs Allowed": runs_allowed,
                    "Average Batters Age": batters_age,
                    "Average Pitchers Age": pitchers_age,
                    "Players Used": players_used,
                    "Pitchers Used": pitchers_used
                })
    
    # Convert to DataFrame
    df = pd.DataFrame(all_data)
    
    return df

def main():
    # Generate the playoff data
    playoff_data = generate_playoff_data()
    
    # Get current timestamp for the filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Save to CSV
    filename = f"playoff_bracket_data_{timestamp}.csv"
    playoff_data.to_csv(filename, index=False)
    
    print(f"Playoff bracket data has been generated and saved to {filename}")
    print(f"Total records: {len(playoff_data)}")
    
    # Display the first few rows
    print("\nSample data:")
    print(playoff_data.head())

if __name__ == "__main__":
    main()
