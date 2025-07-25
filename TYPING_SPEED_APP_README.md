# Typing Speed Test - Windows GUI Application

A professional typing speed test application with a modern GUI, built for Windows using Python and tkinter.

## 🚀 Features

- **Real-time typing speed measurement** (WPM - Words Per Minute)
- **Live accuracy tracking** with visual feedback
- **Customizable test duration** (30s, 60s, 2min, 5min)
- **Visual text highlighting** (correct/incorrect/current character)
- **Multiple sample texts** for varied practice
- **Session statistics** tracking (best WPM, best accuracy)
- **Professional Windows GUI** with modern design
- **Automatic test start** when you begin typing
- **Comprehensive results display** with both net and gross WPM

## 📊 Metrics Calculated

- **Net WPM**: Adjusted for errors (industry standard)
- **Gross WPM**: Raw typing speed without error adjustment
- **Accuracy**: Percentage of correctly typed characters
- **Error count**: Number of incorrect characters
- **Session statistics**: Track your progress across multiple tests

## 🖥️ System Requirements

- **Windows 7/8/10/11** (32-bit or 64-bit)
- **Python 3.6+** (for running from source)
- **2GB RAM minimum**
- **50MB free disk space**

## 🏃‍♂️ Quick Start

### Option 1: Run Executable (Recommended)
1. Download `TypingSpeedTest.exe` from the releases
2. Double-click to run
3. No installation required!

### Option 2: Run from Source
1. Install Python 3.6+ from [python.org](https://python.org)
2. Download this repository
3. Double-click `typing_speed_test.py` or run:
   ```bash
   python typing_speed_test.py
   ```

### Option 3: Build Your Own Executable
1. Install Python and clone this repository
2. Run the build script:
   ```bash
   python build_windows_exe.py
   ```
3. Find your executable in the `dist/` folder

## 🎯 How to Use

1. **Launch the application**
2. **Read the text** displayed in the upper text area
3. **Click "Start Test"** or simply **start typing** in the input area
4. **Type the text** as accurately and quickly as possible
5. **Watch real-time stats** update as you type
6. **Review results** when the timer ends
7. **Try again** with the same text or load a new one

## 🎨 Interface Guide

### Main Window Components:
- **Timer Display**: Shows remaining time in red
- **WPM Counter**: Live words-per-minute in green
- **Accuracy Display**: Current accuracy percentage in blue
- **Text Display**: Shows the text to type with color coding:
  - 🟢 **Green**: Correctly typed characters
  - 🔴 **Red**: Incorrectly typed characters  
  - 🟡 **Yellow**: Current character position
- **Input Area**: Where you type the text
- **Control Buttons**:
  - **Start Test**: Begin a new test
  - **Reset**: Clear current test and start over
  - **New Text**: Load a different sample text
- **Duration Selector**: Choose test length (30s - 5min)
- **Results Panel**: Detailed statistics after test completion

## 🔧 Building from Source

### Prerequisites
```bash
pip install -r requirements.txt
```

### Build Commands
```bash
# Install dependencies
pip install pyinstaller

# Build executable
python build_windows_exe.py

# Or manually with PyInstaller
pyinstaller --onefile --windowed --name=TypingSpeedTest typing_speed_test.py
```

## 📈 Understanding Your Results

### WPM (Words Per Minute)
- **Gross WPM**: Total characters typed ÷ 5 ÷ minutes
- **Net WPM**: Gross WPM - (errors ÷ 5 ÷ minutes)
- **Industry Standard**: Net WPM is the standard measurement

### Accuracy
- Percentage of correctly typed characters
- Calculated in real-time as you type

### Typing Speed Benchmarks
- **Beginner**: 0-25 WPM
- **Average**: 25-40 WPM  
- **Good**: 40-60 WPM
- **Excellent**: 60-80 WPM
- **Professional**: 80+ WPM

## 🐛 Troubleshooting

### Common Issues:

**Application won't start:**
- Ensure Python 3.6+ is installed
- Check that tkinter is available: `python -c "import tkinter"`

**Timer not working properly:**
- Close and restart the application
- Ensure no background processes are interfering

**Text highlighting issues:**
- Reset the test using the Reset button
- Load a new text sample

**Performance issues:**
- Close other applications to free up memory
- Restart the application

## 🛠️ Development

### File Structure
```
typing-speed-test/
├── typing_speed_test.py      # Main application
├── build_windows_exe.py      # Build script
├── requirements.txt          # Dependencies
├── TYPING_SPEED_APP_README.md # This file
└── dist/                     # Built executables (after build)
```

### Key Classes and Methods
- `TypingSpeedTest`: Main application class
- `setup_ui()`: Creates the user interface
- `start_test()`: Begins timing and input tracking
- `update_highlighting()`: Visual feedback system
- `calculate_results()`: Statistics computation

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues.

## 📞 Support

For support, please open an issue on the GitHub repository or contact the developer.

---

**Happy Typing! 🎯⌨️**