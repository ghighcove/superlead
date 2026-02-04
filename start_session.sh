#!/bin/bash

echo "================================================================"
echo " AUTONOMOUS PROJECTILE GUIDANCE RESEARCH SYSTEM"
echo "================================================================"
echo
echo "Starting session with automatic source ingestion..."
echo

# Check if Python is available
if ! command -v python3 &> /dev/null && ! command -v python &> /dev/null; then
    echo "❌ Python not found. Please install Python 3.8+ first."
    exit 1
fi

# Determine Python command
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
else
    PYTHON_CMD="python"
fi

# Run automatic ingestion
echo "🔍 Running automatic source ingestion..."
echo
$PYTHON_CMD session_ingestion.py

echo
echo "================================================================"
echo " Session ready. You can now begin your research work."
echo "================================================================"
echo