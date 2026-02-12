import os
import shutil
import subprocess


# Define the absolute path to the OTHER environment's python
# Based on your previous 'which python' output
piano_python = os.path.abspath("env_piano/bin/python")

# Define paths
submodule_path = "modelAttackDecay-for-piano-transcription"
source_dir = os.path.join(submodule_path, "result")
target_dir = "results/nmf_outputs"

# 1. Run the transcription script
print("Starting transcription...")
subprocess.run([piano_python, "train-template.py"], cwd=submodule_path)

# 2. Move files to main results folder
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

for filename in os.listdir(source_dir):
    if filename.endswith(".mat") or filename.endswith(".npy"):
        shutil.move(os.path.join(source_dir, filename), os.path.join(target_dir, filename))
        print(f"Moved: {filename} to {target_dir}")