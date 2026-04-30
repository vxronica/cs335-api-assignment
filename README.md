# Assignment 01 — Working with AI & ML APIs

**Name:** Veronica Perez  

## API Used

- **API:** PokeAPI  
- **Base URL:** https://pokeapi.co/api/v2  
- **Authentication:** None required (public API)


## Project Description

This project demonstrates how to interact with a REST API using Python.  
I used PokeAPI to retrieve and display Pokémon-related data by making HTTP GET requests, parsing JSON responses, and printing formatted output to the terminal.


## API Calls Implemented

This script makes three distinct API calls:

1. **Pokemon Info**
   - Endpoint: `/pokemon/pikachu`
   - Displays:
     - Name
     - Height
     - Weight
     - Abilities
     - Types

2. **Ability Info**
   - Endpoint: `/ability/static`
   - Displays:
     - Ability name
     - Effect description

3. **Pokemon Locations**
   - Endpoint: `/pokemon/pikachu/encounters`
   - Displays:
     - Locations where Pikachu can be found

## Sample Output

```text
--- Pokemon Info ---
Name: Pikachu
Height: 4
Weight: 60
Abilities: static, lightning-rod
Types: electric

--- Ability Info ---
Ability: Static
Effect: Has a 30% chance of paralyzing attacking Pokémon on contact.

--- Where to Find Pikachu ---
- viridian-forest-area
- power-plant-area
- kanto-route-2-south-towards-viridian-city
```

## Step-by-Step Setup

### Step 1 — Clone the repo

Clone the repo:

```bash
git clone https://github.com/vxronica/cs335-api-assignment.git
cd cs335-api-assignment
```

### Step 2 — Create a Virtual Environment

A virtual environment isolates this project's dependencies from your system Python.

```bash
# macOS / Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

You should see `(venv)` at the start of your prompt — this confirms the environment is active.

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4 — Run the Script

```bash
python starter.py
```
- No API key is required for this project  
- Basic error handling is implemented using HTTP status codes  
- The program runs entirely in the terminal  
