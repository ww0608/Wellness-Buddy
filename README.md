# Wellness Buddy: All-in-One Health Tracker
Wellness Buddy is a comprehensive Python GUI application developed to promote healthy lifestyles in alignment with UN Sustainable Development Goal 3: Good Health and Well-Being. It provides a centralized platform for users to monitor physical health, nutrition, sleep, and emotional wellness.

# Core Features
- Meal Tracker: Log daily meals and calculate total calorie intake. Features data validation to ensure calorie values are numeric.
- Sleep Tracker: Calculate total sleep duration using 24-hour format inputs. Includes logic to handle sleep cycles that cross over midnight.
- BMI Calculator: Instantly calculate Body Mass Index (BMI) with categorized health suggestions based on the results.
- Mood Journal: Record daily emotional states and receive a curated YouTube music playlist suggestion based on your mood.
- Data Persistence: Automatically prompts users to save records to local text files (meals.txt, sleep.txt, mood.txt) before closing features.

# Technical Highlights
- Language: Python 3.x
- GUI Framework: tkinter
- Key Modules: - webbrowser: For launching mood-based playlists.
  - datetime: For automated date stamping of entries.
  - random: For diversifying song suggestions.
- Advanced UI Elements: Implements Toplevel windows, Listbox for history viewing, OptionMenu for selections, and custom LabelFrames for a clean layout.
