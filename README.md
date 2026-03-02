# AI Chess Engine ♟️

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Completed-success)](https://github.com/yourusername/I-Chess-Engine)

An interactive AI Chess Engine with **GUI and scalable difficulty levels**. Challenge yourself against an AI opponent powered by **Minimax and Alpha-Beta Pruning**.

---

##  Overview

This project demonstrates a Chess AI that evaluates moves strategically and optimizes its decisions. Users can play as White against the AI (Black) in a **GUI powered by Pygame**.  

Key focus:
- Artificial Intelligence
- Algorithm Optimization
- Game Development
- GUI Development

---

##  Features

- **Intelligent AI:** Scalable difficulty levels via Minimax depth.  
- **Optimized Performance:** Alpha-Beta Pruning for fast decision-making.  
- **Interactive GUI:** Play on a visual chessboard.  
- **Future-ready:** Modular design for adding features like full chess pieces, multiplayer, or ML-based AI.

---

##  Tech Stack

- **Language:** Python 3  
- **Libraries:** Pygame  
- **Algorithms:** Minimax, Alpha-Beta Pruning  
- **Data Structures:** Arrays, Trees (for move simulation)

---

## ⚙️ How It Works

1. **Board Representation:** 8x8 grid with pieces represented as strings.  
2. **Move Generation:** Generates all legal moves for the AI and player.  
3. **Decision Making:** Minimax algorithm simulates moves to select the best one.  
4. **Optimization:** Alpha-Beta pruning reduces unnecessary calculations.  
5. **GUI Interaction:** Player clicks on squares to move; AI responds automatically.

---

##  How to Run

```bash
# Clone repository

cd I-Chess-Engine

# Install dependencies
pip install -r requirements.txt

# Run the game
python main.py
