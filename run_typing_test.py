#!/usr/bin/env python3
"""
Simple launcher for the Typing Speed Test application
"""

import sys
import os

def main():
    """Launch the typing speed test application"""
    try:
        # Import and run the main application
        from typing_speed_test import main as app_main
        print("🚀 Launching Typing Speed Test...")
        app_main()
    except ImportError as e:
        print(f"❌ Error: Could not import the application: {e}")
        print("Make sure typing_speed_test.py is in the same directory.")
        return 1
    except Exception as e:
        print(f"❌ Error running application: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())