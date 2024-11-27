# Rock, Paper, Scissors Tournament

This project implements strategic games based on the popular "Rock, Paper, Scissors" game using various agents that employ different decision-making approaches. The project conducts a tournament between these agents and displays the game results.

## Project Structure

```
/agents                  # Folder containing agents with different strategies
├── rock.py              # Strategy that always chooses rock
├── paper.py             # Strategy that always chooses paper
├── scissors.py          # Strategy that always chooses scissors
├── copy_opponent.py     # Strategy that copies the opponent's move
├── reactionary.py       # Strategy that chooses a move that beats the opponent's move
├── counter_reactionary.py  # Strategy that counters the reactionary strategy
├── statistical.py       # Strategy that chooses a move that beats the opponent's most frequent move
├── alternating.py       # Strategy that alternates between moves
├── random_choice.py     # Strategy that chooses a move randomly
├── cycle_opponent.py    # Strategy that cyclically chooses a move based on the opponent's last move
├── adaptive_response.py # Strategy that adapts to the opponent's moves
├── delayed_reaction.py # Strategy that reacts to the opponent's move with a delay
└── __init__.py          # Package initialization for agents

tournament.py            # Main script to run the tournament between agents
README.md                # This file
```

## Agent Descriptions

This project includes different strategies for playing "Rock, Paper, Scissors":

1. **rock** — always chooses rock.
2. **paper** — always chooses paper.
3. **scissors** — always chooses scissors.
4. **copy_opponent** — copies the opponent's last move.
5. **reactionary** — chooses a move that beats the opponent's move.
6. **counter_reactionary** — counters the reactionary strategy.
7. **statistical** — chooses a move that beats the opponent's most frequent move.
8. **alternating** — alternates between rock, paper, and scissors.
9. **random_choice** — randomly chooses a move.
10. **cycle_opponent** — cyclically chooses a winning move based on the opponent's last move.
11. **adaptive_response** — adapts to the opponent's moves, choosing moves that beat them.
12. **delayed_reaction** — reacts to the opponent's move with a delay.

## Running the Tournament

To run the tournament, execute the following command:

```bash
python tournament.py
```

This script will conduct the tournament between all agents and display the results in the console.

## How it Works

1. Each agent chooses a move based on its strategy.
2. The tournament is run between all possible pairs of agents.
3. The results of each match are stored in a dictionary and displayed after the tournament concludes.

## License

This project uses an open license. See the LICENSE file for details.
