#!/bin/bash

# Get the directory of the script
SCRIPT_DIR="$(dirname "$(realpath "$0")")"

# Navigate to the directory containing your virtual environment and application
cd "$SCRIPT_DIR"

# Create logs directory if it doesn't exist
mkdir -p logs

# Source the virtual environment
source venv/bin/activate

# Start the Flask application in detached mode
cd site
nohup python3 cors-http.py &> ../logs/cors-http.log &  # Redirecting output to a log file
FLASK_PID=$!  # Capture the PID of the Flask process
cd ..

# Start the translation script in detached mode
cd translate
nohup python3 translate.py &> ../logs/translate.log &  # Redirecting output to a log file
TRANSLATE_PID=$!  # Capture the PID of the translation process
cd ..

# Optional: You can print the PIDs of the last processes started
echo "Started site (PID: $FLASK_PID) and translator (PID: $TRANSLATE_PID) in detached mode."

# Optionally wait for both processes to finish
wait $FLASK_PID
wait $TRANSLATE_PID

echo "Both processes have completed."
