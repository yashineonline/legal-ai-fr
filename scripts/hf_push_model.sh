#!/bin/bash
# Set these variables
SPACE_REPO_URL="https://huggingface.co/spaces/yashineonline/legal-hf"
TEMP_DIR="temp_hf_space"



# Clone the space repo
git clone $SPACE_REPO_URL $TEMP_DIR

# Copy your app files
cp -r ../legal_hf/* .

# Commit and push
git add .
git commit -m "Deploy legal_hf to Hugging Face Space"
git push


