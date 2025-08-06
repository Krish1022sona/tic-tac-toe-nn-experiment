# Tic-Tac-Toe AI (Neural Network Experiment)

This is a small project I built to explore **feed-forward neural networks, backpropagation, and related concepts**.  
The goal was to train a neural net to play Tic-Tac-Toe using pre-defined optimal move data.

## 📌 What I Learned
- How to prepare input-output training data for neural networks
- How feed-forward networks process information
- How backpropagation updates weights and biases
- Why **simple neural networks struggle** in deterministic perfect-information games like Tic-Tac-Toe
- The difference between **pattern learning** and **game tree reasoning**

## ⚠️ Limitations
- The AI does **not guarantee perfect play**
- Neural networks cannot easily perform optimal game tree search (Minimax or RL are better)

## 📂 Files
- `data.py` → Training dataset
- `neural_network.py` → Custom feed-forward NN implementation
- `tic_tac_toe_AI.py` → Runs the game with the AI player
- `game.py` → Core Tic-Tac-Toe game logic
- `math_mine.py` → Math helper functions (softmax, cross-entropy, etc.)
- `testing.ipynb` → Jupyter Notebook for experiments
- `updates_values.txt` → Pre-trained weights and biases

## 🐍 Requirements
No external libraries required — everything is implemented from scratch in Python.  
Only the built-in `math` module is used.

## 🚀 Running the Game
You can run the game in two ways:
1. Run the [tic_tac_toe_AI.py](tic_tac_toe_AI.py) script directly.
2. Open [testing.ipynb](testing.ipynb) for interactive testing.

> **Note:** The provided files do **not automatically load** the pre-trained values.  
> The model will train on startup before you can play.  
> Pre-trained values are stored in [updates_values.txt](updates_values.txt).

## 🧠 Conclusion
This project was not about building the best Tic-Tac-Toe AI.  
It was about **understanding how neural networks work from scratch** — forward pass, backpropagation, and training dynamics.  
For this type of game, **rule-based algorithms (Minimax)** or **reinforcement learning** are far more effective.
