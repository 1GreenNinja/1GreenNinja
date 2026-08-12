#!/usr/bin/env python3
"""
Script to build Windows executable for Typing Speed Test application
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    print("Installing requirements...")
    try:
        subprocess.check_call(["python3", "-m", "pip", "install", "-r", "requirements.txt"])
        print("✓ Requirements installed successfully")
    except subprocess.CalledProcessError as e:
        print(f"✗ Error installing requirements: {e}")
        return False
    return True

def build_executable():
    """Build Windows executable using PyInstaller"""
    print("Building Windows executable...")
    
    # PyInstaller command with options for Windows GUI app
    command = [
        "python3", "-m", "PyInstaller",
        "--onefile",                    # Create single executable file
        "--windowed",                   # No console window (GUI only)
        "--name=TypingSpeedTest",       # Name of the executable
        "--icon=NONE",                  # No icon (can add .ico file later)
        "--distpath=dist",              # Output directory
        "--workpath=build",             # Temporary build directory
        "--specpath=build",             # .spec file location
        "typing_speed_test.py"          # Main Python file
    ]
    
    try:
        subprocess.check_call(command)
        print("✓ Executable built successfully!")
        print("📁 Executable location: dist/TypingSpeedTest.exe")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Error building executable: {e}")
        return False

def main():
    """Main build process"""
    print("🚀 Building Typing Speed Test for Windows")
    print("=" * 50)
    
    # Check if typing_speed_test.py exists
    if not os.path.exists("typing_speed_test.py"):
        print("✗ Error: typing_speed_test.py not found in current directory")
        return
    
    # Install requirements
    if not install_requirements():
        print("✗ Build failed during requirements installation")
        return
    
    # Build executable
    if build_executable():
        print("\n🎉 Build completed successfully!")
        print("\nTo run the application:")
        print("1. Navigate to the 'dist' folder")
        print("2. Double-click TypingSpeedTest.exe")
        print("\nYou can distribute the .exe file to any Windows computer!")
    else:
        print("\n❌ Build failed")

if __name__ == "__main__":
    main()