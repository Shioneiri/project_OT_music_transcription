# Optimal Transport for Music Transcription (STAT0035 Project)

My project on OT for music transcription. This repository contains experiments for piano transcription using Non-negative Matrix Factorization (NMF) variants and Optimal Transport (Wasserstein distance).

## Setup Instructions

### 1. Initialize Submodules
This project relies on external repositories as submodules (e.g., `libnmfd` and `modelAttackDecay-for-piano-transcription`). To pull these in, run:

```bash
git submodule update --init --recursive
```

### 2. Set Up the Python Environment
The project uses virtual environments to manage dependencies. `env_piano` is the primary working environment.

To activate the environment:
```bash
source env_piano/bin/activate
```

*(Note: If the path inside the environment breaks due to folder renaming, recreate the environment using `python3 -m venv env_piano` and reinstall dependencies).*

### 3. Set Up Jupyter Notebook Kernel
To ensure your Jupyter notebooks use the `env_piano` python environment where the dependencies are installed, register it as a Jupyter kernel:

```bash
# Inside the activated env_piano environment
pip install ipykernel
python -m ipykernel install --user --name=env_piano --display-name "Python (env_piano)"
```

### 4. Running the Code
- Open any Jupyter notebook (e.g., in the `libnmfd` or `notebooks` folder).
- In your editor's top-right corner, switch the active kernel to **Python (env_piano)**.
- For piano transcription tasks, you can use the wrapper script:
  ```bash
  python scripts/run_AD_transcription.py
  ```
