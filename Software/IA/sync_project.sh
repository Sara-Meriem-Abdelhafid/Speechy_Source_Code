#!/bin/bash

# Navigate to your project directory
cd /Users/saraabdelhafid/Desktop/Speechy_Source_Code/Source Code/Speechy_Robot_mac  
# Check current branch
echo "Checking current branch..."
git branch

# Fetch updates from remote
echo "Fetching updates from GitHub..."
git fetch

# Check status
echo "Checking status..."
git status

# Pull changes if necessary
echo "Pulling changes (if any)..."
git pull origin main

# Notify user
echo "Your project is up to date!"

