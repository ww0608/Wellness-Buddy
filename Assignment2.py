import tkinter 
import tkinter.messagebox
from datetime import date
import random
import webbrowser

class WellnessBuddy:
    today = date.today().isoformat()

    # Constants for UI styles
    BG_COLOR = "#f8fbff"
    BTN_BG_COLOR = "#cdefff"
    BTN_QUIT_BG = "#ffc0c0"
    SECTION_FONT = ("Arial", 12, "bold")
    LABEL_FONT = ("Arial", 10)
    TITLE_FONT = ("Arial", 16, "bold")

    #HOME MENU
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Wellness Buddy")
        self.main_window.configure(bg=self.BG_COLOR)

        # Title
        self.title_label = tkinter.Label(self.main_window, text="Wellness Buddy",
                                         font=self.TITLE_FONT, bg=self.BG_COLOR)
        self.title_label.pack(pady=(20,5))
        self.subtitle_label = tkinter.Label(self.main_window, 
                                            text="Your daily guide to better health & mood",
                                            font=self.LABEL_FONT, bg=self.BG_COLOR)
        self.subtitle_label.pack(pady=(0,20))

        # Features LabelFrame
        self.feature_lbframe = tkinter.LabelFrame(self.main_window, text="Features",
                                                  font=self.SECTION_FONT, bg=self.BG_COLOR, labelanchor="n")
        self.feature_lbframe.pack(padx=20, pady=10, fill="x")


        # Features Buttons
        self.meal_button = tkinter.Button(self.feature_lbframe, text="Meal Tracker", width=20,
                                          bg=self.BTN_BG_COLOR, font=self.LABEL_FONT, command=self.mealTracker)
        self.sleep_button = tkinter.Button(self.feature_lbframe, text="Sleep Tracker", width=20,
                                           bg=self.BTN_BG_COLOR, font=self.LABEL_FONT, command=self.sleepTracker)
        self.bmi_button = tkinter.Button(self.feature_lbframe, text="BMI Calculator", width=20,
                                         bg=self.BTN_BG_COLOR, font=self.LABEL_FONT, command=self.bmiCalculator)
        self.mood_button = tkinter.Button(self.feature_lbframe, text="Mood Journal", width=20,
                                          bg=self.BTN_BG_COLOR, font=self.LABEL_FONT, command=self.moodJournal)
        self.meal_button.grid(row=0, column=0, padx=15, pady=10)
        self.sleep_button.grid(row=0, column=1, padx=15, pady=10)
        self.bmi_button.grid(row=1, column=0, padx=15, pady=10)
        self.mood_button.grid(row=1, column=1, padx=15, pady=10)

        # Quit Button
        self.bottom_frame = tkinter.Frame(self.main_window, bg=self.BG_COLOR)
        self.bottom_frame.pack(pady=15)
        self.quit_button = tkinter.Button(self.bottom_frame, text="Quit", bg=self.BTN_QUIT_BG,
                                          font=self.LABEL_FONT, width=15, command=self.main_window.destroy)
        self.quit_button.pack()
        tkinter.mainloop()
    
    def ask_and_save(self, filename, entry_text, title, prompt):
        save_record = tkinter.messagebox.askyesno(title, prompt)
        if save_record:
            with open(filename, "a") as file:
                file.write(entry_text)
        return save_record    

    #MEAL TRACKER    
    def mealTracker(self):
        # Meal Tracker Window
        meal_window = tkinter.Toplevel(self.main_window)
        meal_window.title("Meal Tracker")
        meal_window.configure(bg=self.BG_COLOR)
        meal_frame = tkinter.LabelFrame(meal_window, text="What did you eat today?", 
                                        font=self.SECTION_FONT, bg=self.BG_COLOR, padx=10, pady=10, labelanchor="n")
        meal_frame.pack(padx=15, pady=15, fill="both", expand=True)

        # Date
        date_frame = tkinter.Frame(meal_frame, bg=self.BG_COLOR)
        date_frame.pack(pady=5, anchor="w")
        date_label = tkinter.Label(date_frame, text="Date:", font=self.LABEL_FONT, bg=self.BG_COLOR, width=10, anchor="w")
        date_label.pack(side='left')
        date_entry = tkinter.Entry(date_frame, font=self.LABEL_FONT)
        date_entry.insert(0, self.today)
        date_entry.pack(side='left')

        # Meal Type
        mealType_frame = tkinter.Frame(meal_frame, bg=self.BG_COLOR)
        mealType_frame.pack(pady=5, anchor="w")
        mealType_label = tkinter.Label(mealType_frame, text="Meal Type:", font=self.LABEL_FONT, bg=self.BG_COLOR,
                                       width=15, anchor="w")
        mealType_label.pack(side='left')
        mealType_var = tkinter.StringVar(value="Breakfast")
        mealType_dropdown = tkinter.OptionMenu(mealType_frame, mealType_var,
                                               "Breakfast", "Lunch", "Dinner", "Snacks")
        mealType_dropdown.config(font=self.LABEL_FONT, bg="#ffffff")
        mealType_dropdown.pack(side='left')

        # Food Item
        food_frame = tkinter.Frame(meal_frame, bg=self.BG_COLOR)
        food_frame.pack(pady=5, anchor="w")
        food_label = tkinter.Label(food_frame, text="Food Item:", font=self.LABEL_FONT, bg=self.BG_COLOR, width=10, anchor="w")
        food_label.pack(side='left')
        food_entry = tkinter.Entry(food_frame, font=self.LABEL_FONT)
        food_entry.pack(side='left')

        # Calories 
        calories_frame = tkinter.Frame(meal_frame, bg=self.BG_COLOR)
        calories_frame.pack(pady=5, anchor="w")
        calories_label = tkinter.Label(calories_frame, text="Calories:", font=self.LABEL_FONT, bg=self.BG_COLOR,
                                       width=10, anchor="w")
        calories_label.pack(side='left')
        calories_entry = tkinter.Entry(calories_frame, font=self.LABEL_FONT)
        calories_entry.pack(side='left')

        # Meals display
        meal_listbox = tkinter.Listbox(meal_frame, width=40, font=("Arial", 9))
        meal_listbox.pack(pady=5)
        self.total_calories = 0
        self.total_label = tkinter.Label(meal_frame, text="Total Calories: 0", 
                                         font=self.LABEL_FONT, bg=self.BG_COLOR)
        self.total_label.pack(pady=5)

        # Add meal function
        def add_meal():
            mealType = mealType_var.get()
            food = food_entry.get()
            calories = calories_entry.get()
            if food and calories.isdigit():
                calories = int(calories)
                self.total_calories += calories
                entry_date = date_entry.get().strip()
                entry = f"{entry_date}  |  {mealType} - {food}: {calories} cal\n"
                self.total_label.config(text=f"Total Calories: {self.total_calories}")
                meal_listbox.insert(tkinter.END, entry)

                # clear fields for next entry
                food_entry.delete(0, tkinter.END)
                calories_entry.delete(0, tkinter.END)
            else:
                tkinter.messagebox.showerror("Error", "Please enter valid food name and numeric calories.")

        add_button = tkinter.Button(meal_frame, text="Add Meal", bg=self.BTN_BG_COLOR, font=self.LABEL_FONT,
                                   width=20, command=add_meal)
        add_button.pack(pady=10)

        def on_close():
            entries = meal_listbox.get(0, tkinter.END)
            if entries:
                entry_text = "".join(entries)
                self.ask_and_save("meals.txt", entry_text, "Save Entry", "Save the meal details to meals.txt?")
            meal_window.destroy()

        meal_window.protocol("WM_DELETE_WINDOW", on_close)

    #SLEEP TRACKER
    def sleepTracker(self):
        #Sleep Tracker Window        
        sleep_window = tkinter.Toplevel(self.main_window)
        sleep_window.title("Sleep Tracker")
        sleep_window.configure(bg=self.BG_COLOR)
        sleep_frame = tkinter.LabelFrame(sleep_window, text="How did you sleep?", 
                                        font=self.SECTION_FONT, bg=self.BG_COLOR, padx=10, pady=10, labelanchor="n")
        sleep_frame.pack(padx=15, pady=15, fill="both", expand=True)

        # Date Entry
        date_frame = tkinter.Frame(sleep_frame, bg=self.BG_COLOR)
        date_frame.pack(pady=5, anchor="w")
        date_label = tkinter.Label(date_frame, text="Date:", font=self.LABEL_FONT, bg=self.BG_COLOR, width=23, anchor="w")
        date_label.pack(side='left')
        date_entry = tkinter.Entry(date_frame, font=self.LABEL_FONT)
        date_entry.insert(0, self.today)
        date_entry.pack(side='left')

        # Bedtime Entry
        bedtime_frame = tkinter.Frame(sleep_frame, bg=self.BG_COLOR)
        bedtime_frame.pack(pady=5, anchor="w")
        bedtime_label = tkinter.Label(bedtime_frame, text="Bedtime (24h):", font=self.LABEL_FONT, bg=self.BG_COLOR,
                                      width=23, anchor="w")
        bedtime_label.pack(side='left')
        bedtime_entry = tkinter.Entry(bedtime_frame, font=self.LABEL_FONT)
        bedtime_entry.pack(side='left')

        # Wakeup Time Entry
        wake_frame = tkinter.Frame(sleep_frame, bg=self.BG_COLOR)
        wake_frame.pack(pady=5, anchor="w")
        wake_label = tkinter.Label(wake_frame, text="Wake-up Time (24h):", font=self.LABEL_FONT, bg=self.BG_COLOR,
                                   width=23, anchor="w")
        wake_label.pack(side='left')
        wake_entry = tkinter.Entry(wake_frame, font=self.LABEL_FONT)
        wake_entry.pack(side='left')

        # Sleep Duration Label
        self.sleep_label = tkinter.Label(sleep_frame, text="Sleep Duration: ", font=self.LABEL_FONT, bg=self.BG_COLOR)
        self.sleep_label.pack(pady=10)

        # Output Text Box
        output_text = tkinter.Text(sleep_frame, height=5, width=50, state="disabled", font=self.LABEL_FONT, wrap="word")
        output_text.pack(pady=5)

        # List to store entries
        sleep_entries = []

        # Calculate Button function
        def calcDuration():
            try:                
                bed_hour = int(bedtime_entry.get()[:2])
                bed_min = int(bedtime_entry.get()[2:])
                wake_hour = int(wake_entry.get()[:2])
                wake_min = int(wake_entry.get()[2:])

                if bed_hour > 23 or bed_hour < 0 or bed_min > 59 or bed_min < 0 or wake_hour > 23 or wake_hour < 0 or wake_min > 59 or wake_min < 0:
                    raise ValueError
                
                bed_total = bed_hour * 60 + bed_min
                wake_total = wake_hour * 60 + wake_min
                
                if wake_total < bed_total:
                    sleep_minutes = (24 * 60 - bed_total) + wake_total
                else:
                    sleep_minutes = wake_total - bed_total
                hours = sleep_minutes // 60
                minutes = sleep_minutes % 60
                entry_date = date_entry.get().strip()
                entry = f"{entry_date}  |  Sleep duration: {hours} hours {minutes} minutes \n"
                self.sleep_label.config(text=f"Sleep duration: {hours} hours {minutes} minutes")
                sleep_entries.append(entry)

                output_text.config(state="normal")
                output_text.insert(tkinter.END, entry)
                output_text.config(state="disabled")

            except ValueError:
                tkinter.messagebox.showerror("Error", "Please enter time in correct format (eg: 0000 to 2359).")
        calc_button = tkinter.Button(sleep_frame, text="Calculate", bg=self.BTN_BG_COLOR, font=self.LABEL_FONT,
                                    width=20, command=calcDuration)
        calc_button.pack(pady=10)

        def on_close():
            if sleep_entries:
                entries_text = "".join(sleep_entries)
                self.ask_and_save("sleep.txt", entries_text, "Save Entry", "Save the sleep status to sleep.txt?")
            sleep_window.destroy()

        sleep_window.protocol("WM_DELETE_WINDOW", on_close)

    #BMI CALCULATOR
    def bmiCalculator(self):
        #BMI Calculator Window        
        bmi_window = tkinter.Toplevel(self.main_window)
        bmi_window.title("BMI Calculator")
        bmi_window.configure(bg=self.BG_COLOR)
        bmi_frame = tkinter.LabelFrame(bmi_window, text="Let’s check your Body Mass Index",
                                      font=self.SECTION_FONT, bg=self.BG_COLOR, padx=10, pady=10, labelanchor="n")
        bmi_frame.pack(padx=15, pady=15, fill="both", expand=True)
        # Weight Entry
        weight_frame = tkinter.Frame(bmi_frame, bg=self.BG_COLOR)
        weight_frame.pack(pady=5, anchor="w")
        weight_label = tkinter.Label(weight_frame, text="Weight (kilogram):", font=self.LABEL_FONT, bg=self.BG_COLOR,
                                    width=15, anchor="w")
        weight_label.pack(side='left')
        weight_entry = tkinter.Entry(weight_frame, font=self.LABEL_FONT, width=15)
        weight_entry.pack(side='left', padx=5)

        # Height Entry
        height_frame = tkinter.Frame(bmi_frame, bg=self.BG_COLOR)
        height_frame.pack(pady=5, anchor="w")
        height_label = tkinter.Label(height_frame, text="Height (metre):", font=self.LABEL_FONT, bg=self.BG_COLOR,
                                    width=15, anchor="w")
        height_label.pack(side='left')
        height_entry = tkinter.Entry(height_frame, font=self.LABEL_FONT, width=15)
        height_entry.pack(side='left', padx=5)

        # BMI Result Label
        bmi_result_label = tkinter.Label(bmi_frame, text="BMI: ", font=self.LABEL_FONT, bg=self.BG_COLOR)
        bmi_result_label.pack(pady=5)

        # Suggestions Text box
        suggestion_label = tkinter.Label(bmi_frame, text="Suggestions:", font=self.LABEL_FONT, bg=self.BG_COLOR)
        suggestion_label.pack(anchor='w')
        suggestion_text = tkinter.Text(bmi_frame, width=50, height=5, wrap="word", font=self.LABEL_FONT)
        suggestion_text.pack(pady=5)

        def calculate_bmi():
            try:
                weight = float(weight_entry.get())
                height = float(height_entry.get())
                if height <= 0 or height > 3 or weight <= 0:
                    raise ValueError
                bmi = weight / (height ** 2)
                if bmi < 18.5:
                    category = "Underweight"
                    suggestions = [
                        "Eat more frequent, balanced meals.", "Eat nutrient-rich foods.", "Focus on strength training."
                    ]
                elif bmi < 25:
                    category = "Normal weight"
                    suggestions = [
                        "Maintain a balanced diet.", "Keep regular exercise.", "Stay hydrated and sleep well."
                    ]
                elif bmi < 30:
                    category = "Overweight"
                    suggestions = [
                        "Reduce sugary foods.", "Include more fruits & veggies.", "Aim for daily exercise."
                    ]
                else:
                    category = "Obesity"
                    suggestions = [
                        "Consult a healthcare professional.", "Establish healthy lifestyles.", "Stay physically active."
                    ]
                bmi_result_label.config(text=f"BMI: {bmi:.2f} ({category})")
                suggestion_text.delete("1.0", tkinter.END)
                for item in suggestions:
                    suggestion_text.insert(tkinter.END, f"- {item}\n")

            except ValueError:
                tkinter.messagebox.showerror("Error", "Please enter valid numeric values.")
        calc_button = tkinter.Button(bmi_frame, text="Calculate", bg=self.BTN_BG_COLOR, font=self.LABEL_FONT,
                                    width=20, command=calculate_bmi)
        calc_button.pack(pady=10)

    #MOOD JOURNAL
    def moodJournal(self):
        #Mood Journal Window        
        mood_window = tkinter.Toplevel(self.main_window)
        mood_window.title("Mood Journal")
        mood_window.configure(bg=self.BG_COLOR)
        mood_frame = tkinter.LabelFrame(mood_window, text="How are you feeling?", 
                                       font=self.SECTION_FONT, bg=self.BG_COLOR, padx=10, pady=10, labelanchor="n")
        mood_frame.pack(padx=15, pady=15, fill="both", expand=True)

        # Date Entry
        date_frame = tkinter.Frame(mood_frame, bg=self.BG_COLOR)
        date_frame.pack(pady=5, anchor="w")
        date_label = tkinter.Label(date_frame, text="Date:", font=self.LABEL_FONT, bg=self.BG_COLOR, width=10, anchor="w")
        date_label.pack(side='left')
        date_entry = tkinter.Entry(date_frame, font=self.LABEL_FONT)
        date_entry.insert(0, self.today)
        date_entry.pack(side='left')

        # Mood Selection
        mood_select_frame = tkinter.Frame(mood_frame, bg=self.BG_COLOR)
        mood_select_frame.pack(pady=5, anchor="w")
        mood_label = tkinter.Label(mood_select_frame, text="Mood:", font=self.LABEL_FONT, bg=self.BG_COLOR, width=10, anchor="w")
        mood_label.pack(side='left')
        mood_var = tkinter.StringVar(value="Feels Good")

        # Store entries
        mood_entries = []

        for mood in ["Feels Bad", "Calm", "Feels Good"]:
            tkinter.Radiobutton(mood_select_frame, variable=mood_var, text=mood, value=mood,
                               font=self.LABEL_FONT, bg=self.BG_COLOR).pack(side='left', padx=5)

        # Output Text Box
        output_text = tkinter.Text(mood_frame, height=5, width=50, state="disabled", font=self.LABEL_FONT, wrap="word")
        output_text.pack(pady=5)
        playlists = {
            "Feels Bad": [
                ("Fix You", "https://www.youtube.com/watch?v=Oncu0bgdcXU"),
                ("Keep Your Head Up Princess", "https://www.youtube.com/watch?v=77PbORk5TN0"),
                ("No One Noticed", "https://www.youtube.com/watch?v=s5XDsHedgBQ")
            ],
            "Calm": [
                ("Put Your Records On", "https://www.youtube.com/watch?v=cDrU3weV3_Y"),
                ("For Once In My Life", "https://www.youtube.com/watch?v=l3qi3E40aWE"),
                ("Summer Nights", "https://www.youtube.com/watch?v=PppiDdYRNWc")
            ],
            "Feels Good": [
                ("Happy", "https://www.youtube.com/watch?v=_s2d4Z5ikb0"),
                ("September", "https://www.youtube.com/watch?v=OBM0DO8Xt1c"),
                ("Can't Stop The Feeling!", "https://www.youtube.com/watch?v=KxKV_E-wB10")
            ]
        }

        def add_entry():
            entry_date = date_entry.get().strip()
            mood = mood_var.get()
            entry = f"{entry_date}  |  Mood: {mood}\n"
            mood_entries.append(entry)
            output_text.config(state="normal")
            output_text.insert(tkinter.END, entry)
            output_text.config(state="disabled")

        add_button = tkinter.Button(mood_frame, text="Add", bg=self.BTN_BG_COLOR, font=self.LABEL_FONT,
                                   width=20, command=add_entry)
        add_button.pack(pady=10)

        def on_close():
            if mood_entries:
                entries_text = "".join(mood_entries)
                self.ask_and_save("mood.txt", entries_text, "Save Entry", "Save the mood details to mood.txt?")

                # After saving, suggest playlist for last mood
                last_mood = mood_entries[-1].split("|  Mood: ")[1].strip()
                song_name, song_link = random.choice(playlists[last_mood])
                prompt = f"Suggested Playlist:\n{song_name}\n\nOpen it in your browser?"
                if tkinter.messagebox.askyesno("Playlist Suggestion", prompt):
                    webbrowser.open(song_link)
            mood_window.destroy()

        mood_window.protocol("WM_DELETE_WINDOW", on_close)

# Create the GUI
myGUI = WellnessBuddy()
