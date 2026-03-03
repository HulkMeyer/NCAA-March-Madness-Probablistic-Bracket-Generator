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

def simulate_game(team1, team2):
    """Simulate a game between two teams and return the scores"""
    # The team with more wins is more likely to win, but upsets can happen
    team1_win_pct = team1["Win-Loss Percentage"]
    team2_win_pct = team2["Win-Loss Percentage"]
    
    # Normalize to create a probability
    total_pct = team1_win_pct + team2_win_pct
    team1_win_probability = team1_win_pct / total_pct
    
    # Add a small random factor to allow for upsets
    team1_win_probability = team1_win_probability * 0.7 + random.random() * 0.3
    
    # Generate scores based on runs scored and allowed averages
    team1_score = int(team1["Runs Scored"] / 162 * random.uniform(0.5, 1.5))
    team2_score = int(team2["Runs Scored"] / 162 * random.uniform(0.5, 1.5))
    
    # Ensure we have a winner (no ties)
    while team1_score == team2_score:
        team1_score = int(team1["Runs Scored"] / 162 * random.uniform(0.5, 1.5))
        team2_score = int(team2["Runs Scored"] / 162 * random.uniform(0.5, 1.5))
    
    if team1_win_probability > random.random():
        if team1_score <= team2_score:
            team1_score = team2_score + random.randint(1, 5)
    else:
        if team2_score <= team1_score:
            team2_score = team1_score + random.randint(1, 5)
    
    return team1_score, team2_score

def simulate_tournament(playoff_data, season):
    """Simulate a single elimination tournament for a given season"""
    # Filter data for the selected season
    season_data = playoff_data[playoff_data["Season"] == season].copy()
    
    # Dictionary to store tournament results by region and round
    tournament_results = {}
    
    # Dictionary to store bracket visualization
    bracket = {}
    
    regions = ["North", "South", "East", "West"]
    
    # First, simulate regional tournaments (rounds 1-4)
    for region in regions:
        tournament_results[region] = {}
        bracket[region] = {}
        
        # Get teams for this region
        region_teams = season_data[season_data["Region"] == region].sort_values("Seed").reset_index(drop=True)
        
        # Round 1 - 8 games (16 teams)
        round1_winners = []
        tournament_results[region]["Round 1"] = []
        bracket[region]["Round 1"] = []
        
        # Match up teams by seed (1 vs 16, 2 vs 15, etc.)
        for i in range(8):
            team1_idx = i
            team2_idx = 15 - i
            
            team1 = region_teams.iloc[team1_idx].to_dict()
            team2 = region_teams.iloc[team2_idx].to_dict()
            
            team1_score, team2_score = simulate_game(team1, team2)
            
            # Record the matchup and scores
            matchup = {
                "team1": f"{team1['Seed']}. {team1['Team']}",
                "team2": f"{team2['Seed']}. {team2['Team']}",
                "team1_score": team1_score,
                "team2_score": team2_score
            }
            tournament_results[region]["Round 1"].append(matchup)
            
            # Determine winner
            if team1_score > team2_score:
                round1_winners.append(team1)
                bracket[region]["Round 1"].append(f"{team1['Seed']}. {team1['Team']} ({team1_score}-{team2_score})")
            else:
                round1_winners.append(team2)
                bracket[region]["Round 1"].append(f"{team2['Seed']}. {team2['Team']} ({team2_score}-{team1_score})")
        
        # Round 2 - 4 games (8 teams)
        round2_winners = []
        tournament_results[region]["Round 2"] = []
        bracket[region]["Round 2"] = []
        
        for i in range(0, 8, 2):
            team1 = round1_winners[i]
            team2 = round1_winners[i+1]
            
            team1_score, team2_score = simulate_game(team1, team2)
            
            # Record the matchup and scores
            matchup = {
                "team1": f"{team1['Seed']}. {team1['Team']}",
                "team2": f"{team2['Seed']}. {team2['Team']}",
                "team1_score": team1_score,
                "team2_score": team2_score
            }
            tournament_results[region]["Round 2"].append(matchup)
            
            # Determine winner
            if team1_score > team2_score:
                round2_winners.append(team1)
                bracket[region]["Round 2"].append(f"{team1['Seed']}. {team1['Team']} ({team1_score}-{team2_score})")
            else:
                round2_winners.append(team2)
                bracket[region]["Round 2"].append(f"{team2['Seed']}. {team2['Team']} ({team2_score}-{team1_score})")
        
        # Round 3 - 2 games (4 teams)
        round3_winners = []
        tournament_results[region]["Round 3"] = []
        bracket[region]["Round 3"] = []
        
        for i in range(0, 4, 2):
            team1 = round2_winners[i]
            team2 = round2_winners[i+1]
            
            team1_score, team2_score = simulate_game(team1, team2)
            
            # Record the matchup and scores
            matchup = {
                "team1": f"{team1['Seed']}. {team1['Team']}",
                "team2": f"{team2['Seed']}. {team2['Team']}",
                "team1_score": team1_score,
                "team2_score": team2_score
            }
            tournament_results[region]["Round 3"].append(matchup)
            
            # Determine winner
            if team1_score > team2_score:
                round3_winners.append(team1)
                bracket[region]["Round 3"].append(f"{team1['Seed']}. {team1['Team']} ({team1_score}-{team2_score})")
            else:
                round3_winners.append(team2)
                bracket[region]["Round 3"].append(f"{team2['Seed']}. {team2['Team']} ({team2_score}-{team1_score})")
        
        # Round 4 - Regional Final (2 teams)
        tournament_results[region]["Round 4"] = []
        bracket[region]["Round 4"] = []
        
        team1 = round3_winners[0]
        team2 = round3_winners[1]
        
        team1_score, team2_score = simulate_game(team1, team2)
        
        # Record the matchup and scores
        matchup = {
            "team1": f"{team1['Seed']}. {team1['Team']}",
            "team2": f"{team2['Seed']}. {team2['Team']}",
            "team1_score": team1_score,
            "team2_score": team2_score
        }
        tournament_results[region]["Round 4"].append(matchup)
        
        # Determine regional champion
        if team1_score > team2_score:
            bracket[region]["Champion"] = {
                "team": team1,
                "display": f"{team1['Seed']}. {team1['Team']} ({team1_score}-{team2_score})"
            }
        else:
            bracket[region]["Champion"] = {
                "team": team2,
                "display": f"{team2['Seed']}. {team2['Team']} ({team2_score}-{team1_score})"
            }
    
    # Final Four (Round 5) - Semifinals
    # North vs East, South vs West
    tournament_results["Final Four"] = {}
    bracket["Final Four"] = {}
    
    # First semifinal: North vs East
    team_north = bracket["North"]["Champion"]["team"]
    team_east = bracket["East"]["Champion"]["team"]
    
    team_north_score, team_east_score = simulate_game(team_north, team_east)
    
    semifinal1 = {
        "team1": f"North: {team_north['Seed']}. {team_north['Team']}",
        "team2": f"East: {team_east['Seed']}. {team_east['Team']}",
        "team1_score": team_north_score,
        "team2_score": team_east_score
    }
    tournament_results["Final Four"]["Semifinal 1"] = semifinal1
    
    if team_north_score > team_east_score:
        finalist1 = {
            "region": "North",
            "team": team_north,
            "display": f"North: {team_north['Seed']}. {team_north['Team']} ({team_north_score}-{team_east_score})"
        }
    else:
        finalist1 = {
            "region": "East",
            "team": team_east,
            "display": f"East: {team_east['Seed']}. {team_east['Team']} ({team_east_score}-{team_north_score})"
        }
    
    # Second semifinal: South vs West
    team_south = bracket["South"]["Champion"]["team"]
    team_west = bracket["West"]["Champion"]["team"]
    
    team_south_score, team_west_score = simulate_game(team_south, team_west)
    
    semifinal2 = {
        "team1": f"South: {team_south['Seed']}. {team_south['Team']}",
        "team2": f"West: {team_west['Seed']}. {team_west['Team']}",
        "team1_score": team_south_score,
        "team2_score": team_west_score
    }
    tournament_results["Final Four"]["Semifinal 2"] = semifinal2
    
    if team_south_score > team_west_score:
        finalist2 = {
            "region": "South",
            "team": team_south,
            "display": f"South: {team_south['Seed']}. {team_south['Team']} ({team_south_score}-{team_west_score})"
        }
    else:
        finalist2 = {
            "region": "West",
            "team": team_west,
            "display": f"West: {team_west['Seed']}. {team_west['Team']} ({team_west_score}-{team_south_score})"
        }
    
    # Championship Game (Round 6)
    team1 = finalist1["team"]
    team2 = finalist2["team"]
    
    team1_score, team2_score = simulate_game(team1, team2)
    
    championship = {
        "team1": f"{finalist1['region']}: {team1['Seed']}. {team1['Team']}",
        "team2": f"{finalist2['region']}: {team2['Seed']}. {team2['Team']}",
        "team1_score": team1_score,
        "team2_score": team2_score
    }
    tournament_results["Championship"] = championship
    
    if team1_score > team2_score:
        champion = {
            "region": finalist1["region"],
            "team": team1,
            "display": f"{finalist1['region']}: {team1['Seed']}. {team1['Team']} ({team1_score}-{team2_score})"
        }
    else:
        champion = {
            "region": finalist2["region"],
            "team": team2,
            "display": f"{finalist2['region']}: {team2['Seed']}. {team2['Team']} ({team2_score}-{team1_score})"
        }
    
    bracket["Championship"] = champion
    
    return tournament_results, bracket

def print_bracket(bracket, season):
    """Print a formatted bracket with scores"""
    print(f"\n{'='*50}")
    print(f"TOURNAMENT BRACKET FOR SEASON {season}")
    print(f"{'='*50}")
    
    regions = ["North", "South", "East", "West"]
    
    for region in regions:
        print(f"\n{'-'*50}")
        print(f"REGION: {region}")
        print(f"{'-'*50}")
        
        for round_num in range(1, 5):
            print(f"\nRound {round_num}:")
            if round_num < 4:
                for team in bracket[region][f"Round {round_num}"]:
                    print(f"  {team}")
            else:
                print(f"  Regional Champion: {bracket[region]['Champion']['display']}")
    
    print(f"\n{'-'*50}")
    print("FINAL FOUR")
    print(f"{'-'*50}")
    
    # Print semifinals
    north_champ = bracket["North"]["Champion"]["display"]
    east_champ = bracket["East"]["Champion"]["display"]
    south_champ = bracket["South"]["Champion"]["display"]
    west_champ = bracket["West"]["Champion"]["display"]
    
    print("\nSemifinal 1:")
    print(f"  North Champion: {north_champ}")
    print(f"  East Champion: {east_champ}")
    
    print("\nSemifinal 2:")
    print(f"  South Champion: {south_champ}")
    print(f"  West Champion: {west_champ}")
    
    # Print championship
    print(f"\n{'-'*50}")
    print("CHAMPIONSHIP")
    print(f"{'-'*50}")
    print(f"  Champion: {bracket['Championship']['display']}")

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
    
    # Ask user if they want to simulate a tournament for a specific year
    while True:
        try:
            year = int(input("\nEnter a year (2000-2025) to simulate a tournament, or 0 to exit: "))
            if year == 0:
                break
            
            if 2000 <= year <= 2025:
                # Simulate tournament for the selected year
                tournament_results, bracket = simulate_tournament(playoff_data, year)
                
                # Print the bracket with scores
                print_bracket(bracket, year)
                
                # Ask if user wants to save the tournament results
                save_option = input("\nDo you want to save the tournament results? (y/n): ").lower()
                if save_option == 'y':
                    # Save tournament results to JSON
                    import json
                    tournament_filename = f"tournament_results_{year}_{timestamp}.json"
                    with open(tournament_filename, 'w') as f:
                        json.dump(tournament_results, f, indent=4)
                    print(f"Tournament results saved to {tournament_filename}")
            else:
                print("Invalid year. Please enter a year between 2000 and 2025.")
        except ValueError:
            print("Invalid input. Please enter a valid year.")

if __name__ == "__main__":
    main()
