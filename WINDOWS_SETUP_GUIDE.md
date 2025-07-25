# 🖥️ Windows 11 Typing Speed Test - Setup Guide

## 🚀 Quick Start (3 Methods)

### Method 1: One-Click Python Run (Fastest)
1. **Install Python** from [python.org](https://python.org/downloads/)
2. **Download** `typing_speed_test.py` (see below)
3. **Double-click** the file to run instantly!

### Method 2: Build .exe File (Recommended)
1. **Download all files** (see File Downloads section)
2. **Install Python** with pip
3. **Run build script**: Double-click `build_windows_exe.py`
4. **Get your .exe** from `dist\TypingSpeedTest.exe`

### Method 3: Manual PyInstaller Build
```cmd
pip install pyinstaller
pyinstaller --onefile --windowed --name=TypingSpeedTest typing_speed_test.py
```

## 📁 File Downloads

Copy these files to your Windows 11 computer:

### 1. Main Application File
**File**: `typing_speed_test.py`
**Size**: ~15KB
**Description**: Complete typing speed test application

```python
# Copy this entire code block and save as typing_speed_test.py
import tkinter as tk
from tkinter import ttk, messagebox, font
import time
import random
import threading

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("1000x700")
        self.root.configure(bg="#f0f0f0")
        
        # Test variables
        self.test_text = ""
        self.start_time = None
        self.end_time = None
        self.is_test_running = False
        self.timer_duration = 60
        self.timer_thread = None
        self.remaining_time = 0
        
        # Statistics
        self.stats = {
            'wpm': 0, 'accuracy': 0, 'characters_typed': 0, 'errors': 0,
            'total_tests': 0, 'best_wpm': 0, 'best_accuracy': 0
        }
        
        # Sample texts
        self.sample_texts = [
            "The quick brown fox jumps over the lazy dog. This pangram contains every letter of the alphabet and is commonly used for typing practice.",
            "Technology is best when it brings people together. The future belongs to those who prepare for it today.",
            "Practice makes perfect, but nobody is perfect, so why practice? This reminds us that improvement is more important than perfection.",
        ]
        
        self.setup_ui()
        self.load_new_text()
        
    def setup_ui(self):
        # Title
        title_font = font.Font(family="Arial", size=24, weight="bold")
        title_label = tk.Label(self.root, text="Typing Speed Test", font=title_font, bg="#f0f0f0", fg="#2c3e50")
        title_label.pack(pady=20)
        
        # Statistics frame
        stats_frame = tk.Frame(self.root, bg="#f0f0f0")
        stats_frame.pack(pady=10)
        
        self.timer_label = tk.Label(stats_frame, text="Time: 60s", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#e74c3c")
        self.timer_label.grid(row=0, column=0, padx=20)
        
        self.wpm_label = tk.Label(stats_frame, text="WPM: 0", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#27ae60")
        self.wpm_label.grid(row=0, column=1, padx=20)
        
        self.accuracy_label = tk.Label(stats_frame, text="Accuracy: 100%", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#3498db")
        self.accuracy_label.grid(row=0, column=2, padx=20)
        
        # Text display
        text_frame = tk.Frame(self.root, bg="#ffffff", relief="solid", bd=2)
        text_frame.pack(pady=20, padx=50, fill="both", expand=True)
        
        text_label = tk.Label(text_frame, text="Text to Type:", font=("Arial", 12, "bold"), bg="#ffffff")
        text_label.pack(anchor="w", padx=10, pady=(10, 5))
        
        self.text_display = tk.Text(text_frame, height=8, font=("Courier", 14), wrap="word", 
                                   state="disabled", bg="#f8f9fa", fg="#2c3e50")
        self.text_display.pack(padx=10, pady=(0, 10), fill="both", expand=True)
        
        # Input area
        input_frame = tk.Frame(self.root, bg="#f0f0f0")
        input_frame.pack(pady=10, padx=50, fill="x")
        
        input_label = tk.Label(input_frame, text="Type here:", font=("Arial", 12, "bold"), bg="#f0f0f0")
        input_label.pack(anchor="w")
        
        self.text_input = tk.Text(input_frame, height=8, font=("Courier", 14), wrap="word")
        self.text_input.pack(fill="x", pady=(5, 0))
        self.text_input.bind('<KeyPress>', self.on_key_press)
        self.text_input.bind('<KeyRelease>', self.on_key_release)
        
        # Control buttons
        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.pack(pady=20)
        
        self.start_button = tk.Button(button_frame, text="Start Test", command=self.start_test,
                                     font=("Arial", 12, "bold"), bg="#27ae60", fg="white", padx=20, pady=10)
        self.start_button.grid(row=0, column=0, padx=10)
        
        self.reset_button = tk.Button(button_frame, text="Reset", command=self.reset_test,
                                     font=("Arial", 12, "bold"), bg="#e74c3c", fg="white", padx=20, pady=10)
        self.reset_button.grid(row=0, column=1, padx=10)
        
        self.new_text_button = tk.Button(button_frame, text="New Text", command=self.load_new_text,
                                        font=("Arial", 12, "bold"), bg="#3498db", fg="white", padx=20, pady=10)
        self.new_text_button.grid(row=0, column=2, padx=10)
        
        # Duration selector
        duration_frame = tk.Frame(button_frame, bg="#f0f0f0")
        duration_frame.grid(row=0, column=3, padx=20)
        
        tk.Label(duration_frame, text="Duration:", font=("Arial", 10), bg="#f0f0f0").pack()
        self.duration_var = tk.StringVar(value="60")
        duration_combo = ttk.Combobox(duration_frame, textvariable=self.duration_var, 
                                     values=["30", "60", "120", "300"], width=5, state="readonly")
        duration_combo.pack()
        duration_combo.bind('<<ComboboxSelected>>', self.on_duration_change)
        
        # Results frame
        self.results_frame = tk.Frame(self.root, bg="#ffffff", relief="solid", bd=2)
        self.results_frame.pack(pady=10, padx=50, fill="x")
        
        results_title = tk.Label(self.results_frame, text="Test Results", font=("Arial", 14, "bold"), bg="#ffffff")
        results_title.pack(pady=10)
        
        self.results_text = tk.Text(self.results_frame, height=4, font=("Arial", 11), 
                                   state="disabled", bg="#f8f9fa")
        self.results_text.pack(padx=10, pady=(0, 10), fill="x")
        
        # Configure highlighting tags
        self.text_display.tag_configure("correct", background="#d4edda")
        self.text_display.tag_configure("incorrect", background="#f8d7da")
        self.text_display.tag_configure("current", background="#fff3cd")
        
    def load_new_text(self):
        self.test_text = random.choice(self.sample_texts)
        self.update_text_display()
        
    def update_text_display(self):
        self.text_display.config(state="normal")
        self.text_display.delete("1.0", tk.END)
        self.text_display.insert("1.0", self.test_text)
        self.text_display.config(state="disabled")
        
    def start_test(self):
        if not self.is_test_running:
            self.is_test_running = True
            self.start_time = time.time()
            self.remaining_time = int(self.duration_var.get())
            
            self.text_input.delete("1.0", tk.END)
            self.text_input.config(state="normal")
            self.text_input.focus()
            
            self.start_button.config(text="Test Running...", state="disabled")
            self.new_text_button.config(state="disabled")
            
            self.timer_thread = threading.Thread(target=self.run_timer)
            self.timer_thread.daemon = True
            self.timer_thread.start()
            
    def run_timer(self):
        while self.remaining_time > 0 and self.is_test_running:
            self.root.after(0, lambda: self.timer_label.config(text=f"Time: {self.remaining_time}s"))
            time.sleep(1)
            self.remaining_time -= 1
            
        if self.is_test_running:
            self.root.after(0, self.end_test)
            
    def end_test(self):
        if self.is_test_running:
            self.is_test_running = False
            self.end_time = time.time()
            
            self.text_input.config(state="disabled")
            self.start_button.config(text="Start Test", state="normal")
            self.new_text_button.config(state="normal")
            
            self.calculate_results()
            
    def reset_test(self):
        self.is_test_running = False
        self.start_time = None
        self.end_time = None
        self.remaining_time = int(self.duration_var.get())
        
        self.text_input.config(state="normal")
        self.text_input.delete("1.0", tk.END)
        
        self.start_button.config(text="Start Test", state="normal")
        self.new_text_button.config(state="normal")
        
        self.timer_label.config(text=f"Time: {self.duration_var.get()}s")
        self.wpm_label.config(text="WPM: 0")
        self.accuracy_label.config(text="Accuracy: 100%")
        
        self.update_text_display()
        
    def on_duration_change(self, event):
        self.timer_duration = int(self.duration_var.get())
        if not self.is_test_running:
            self.timer_label.config(text=f"Time: {self.duration_var.get()}s")
            
    def on_key_press(self, event):
        if not self.is_test_running and event.char.isprintable():
            self.start_test()
            
    def on_key_release(self, event):
        if self.is_test_running:
            self.update_highlighting()
            self.update_live_stats()
            
    def update_highlighting(self):
        typed_text = self.text_input.get("1.0", tk.END).rstrip('\n')
        
        self.text_display.config(state="normal")
        self.text_display.tag_remove("correct", "1.0", tk.END)
        self.text_display.tag_remove("incorrect", "1.0", tk.END)
        self.text_display.tag_remove("current", "1.0", tk.END)
        
        for i, char in enumerate(typed_text):
            if i < len(self.test_text):
                start_pos = f"1.{i}"
                end_pos = f"1.{i+1}"
                
                if char == self.test_text[i]:
                    self.text_display.tag_add("correct", start_pos, end_pos)
                else:
                    self.text_display.tag_add("incorrect", start_pos, end_pos)
        
        if len(typed_text) < len(self.test_text):
            current_pos = f"1.{len(typed_text)}"
            next_pos = f"1.{len(typed_text)+1}"
            self.text_display.tag_add("current", current_pos, next_pos)
            
        self.text_display.config(state="disabled")
        
    def update_live_stats(self):
        if not self.is_test_running:
            return
            
        typed_text = self.text_input.get("1.0", tk.END).rstrip('\n')
        elapsed_time = time.time() - self.start_time
        
        if elapsed_time > 0:
            words_typed = len(typed_text) / 5
            wpm = (words_typed / elapsed_time) * 60
            
            correct_chars = sum(1 for i, char in enumerate(typed_text) 
                              if i < len(self.test_text) and char == self.test_text[i])
            accuracy = (correct_chars / len(typed_text) * 100) if len(typed_text) > 0 else 100
            
            self.wpm_label.config(text=f"WPM: {int(wpm)}")
            self.accuracy_label.config(text=f"Accuracy: {accuracy:.1f}%")
            
    def calculate_results(self):
        typed_text = self.text_input.get("1.0", tk.END).rstrip('\n')
        test_duration = int(self.duration_var.get())
        
        total_chars = len(typed_text)
        correct_chars = sum(1 for i, char in enumerate(typed_text) 
                           if i < len(self.test_text) and char == self.test_text[i])
        errors = total_chars - correct_chars
        
        gross_wpm = (total_chars / 5) / (test_duration / 60)
        net_wpm = max(0, gross_wpm - (errors / 5) / (test_duration / 60))
        
        accuracy = (correct_chars / total_chars * 100) if total_chars > 0 else 0
        
        self.stats['wpm'] = int(net_wpm)
        self.stats['accuracy'] = accuracy
        self.stats['characters_typed'] = total_chars
        self.stats['errors'] = errors
        self.stats['total_tests'] += 1
        
        if net_wpm > self.stats['best_wpm']:
            self.stats['best_wpm'] = int(net_wpm)
        if accuracy > self.stats['best_accuracy']:
            self.stats['best_accuracy'] = accuracy
            
        self.display_results()
        
    def display_results(self):
        results = f"""Test Complete! 

Net WPM: {self.stats['wpm']} | Gross WPM: {int((self.stats['characters_typed'] / 5) / (int(self.duration_var.get()) / 60))}
Accuracy: {self.stats['accuracy']:.1f}% | Errors: {self.stats['errors']}
Characters Typed: {self.stats['characters_typed']} | Test Duration: {self.duration_var.get()}s

Session Stats:
Total Tests: {self.stats['total_tests']} | Best WPM: {self.stats['best_wpm']} | Best Accuracy: {self.stats['best_accuracy']:.1f}%"""

        self.results_text.config(state="normal")
        self.results_text.delete("1.0", tk.END)
        self.results_text.insert("1.0", results)
        self.results_text.config(state="disabled")
        
        messagebox.showinfo("Test Complete", f"Your typing speed: {self.stats['wpm']} WPM\nAccuracy: {self.stats['accuracy']:.1f}%")

def main():
    root = tk.Tk()
    app = TypingSpeedTest(root)
    
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
    y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
    root.geometry(f"+{x}+{y}")
    
    root.mainloop()

if __name__ == "__main__":
    main()
```

### 2. Build Script (Optional)
**File**: `build_windows_exe.py`

```python
import subprocess
import sys
import os

def install_requirements():
    print("Installing PyInstaller...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("✓ PyInstaller installed successfully")
    except subprocess.CalledProcessError as e:
        print(f"✗ Error installing PyInstaller: {e}")
        return False
    return True

def build_executable():
    print("Building Windows executable...")
    
    command = [
        sys.executable, "-m", "PyInstaller",
        "--onefile",
        "--windowed", 
        "--name=TypingSpeedTest",
        "typing_speed_test.py"
    ]
    
    try:
        subprocess.check_call(command)
        print("✓ Executable built successfully!")
        print("📁 Find your .exe in the 'dist' folder")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Error building executable: {e}")
        return False

def main():
    print("🚀 Building Typing Speed Test for Windows")
    print("=" * 50)
    
    if not os.path.exists("typing_speed_test.py"):
        print("✗ Error: typing_speed_test.py not found")
        input("Press Enter to exit...")
        return
    
    if install_requirements() and build_executable():
        print("\n🎉 Build completed successfully!")
        print("Your .exe file is in the 'dist' folder")
    else:
        print("\n❌ Build failed")
    
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
```

### 3. Windows Batch File (Easy Launch)
**File**: `run_typing_test.bat`

```batch
@echo off
echo Starting Typing Speed Test...
python typing_speed_test.py
if %errorlevel% neq 0 (
    echo Error: Python not found or application failed
    echo Please install Python from python.org
    pause
)
```

## 🎯 Step-by-Step Instructions

### For Complete Beginners:

1. **Create a new folder** on your desktop called "TypingTest"

2. **Copy the Python code** from section 1 above into a text file

3. **Save it** as `typing_speed_test.py` (make sure it ends in .py, not .txt)

4. **Install Python**:
   - Go to [python.org/downloads](https://python.org/downloads)
   - Download Python for Windows
   - Run installer and check "Add Python to PATH"

5. **Run the application**:
   - Double-click `typing_speed_test.py`
   - OR open Command Prompt, navigate to folder, run: `python typing_speed_test.py`

### For .exe File:

6. **Copy the build script** from section 2 above

7. **Save it** as `build_windows_exe.py`

8. **Double-click** `build_windows_exe.py`

9. **Find your .exe** in the new `dist` folder

## ✅ What You'll Get

- ✅ **Full GUI application** with modern interface
- ✅ **Real-time typing statistics** (WPM, accuracy)
- ✅ **Visual feedback** with color-coded text
- ✅ **Multiple test durations** (30s to 5min)
- ✅ **Session tracking** for best scores
- ✅ **Windows 11 compatible**

## 🔧 Troubleshooting

**Python not found?**
- Reinstall Python and check "Add to PATH"
- Use Microsoft Store Python installation

**Application won't start?**
- Right-click file → "Open with" → Python
- Check Windows Defender hasn't blocked the file

**Build fails?**
- Run Command Prompt as Administrator
- Update pip: `python -m pip install --upgrade pip`

This method will give you a fully functional Windows 11 compatible executable!