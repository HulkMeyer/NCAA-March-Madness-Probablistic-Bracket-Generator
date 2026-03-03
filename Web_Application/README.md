# 🌐 Flask Application Deployment
This folder contains the production code for the March Madness Simulation Platform.

### 🚀 How to Launch
1. Ensure `requirements.txt` from the root is installed.
2. Run `python run.py`.
3. Navigate to `http://127.0.0.1:5000/`.

### 🛠️ Core Logic
* **`routes.py`**: Handles the UI navigation and API calls to the simulation engine.
* **`simulator.py`**: Contains the `Team` class and probabilistic game outcome logic.
* **`models.py`**: Loads the pre-trained PyTorch weights for real-time inference.