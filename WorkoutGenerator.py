import random
from collections import defaultdict
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

# Complete exercise database
exercises = {
    'Beginner': {
        'Chest': [{'name': 'Push-ups (Knees)', 'sets': 3, 'reps': '8-12'},
                  {'name': 'Bench Press (Machine)', 'sets': 3, 'reps': '10-12'}],
        'Back': [{'name': 'Assisted Pull-ups', 'sets': 3, 'reps': '6-10'},
                 {'name': 'Seated Row (Machine)', 'sets': 3, 'reps': '10-12'}],
        'Legs': [{'name': 'Bodyweight Squats', 'sets': 3, 'reps': '12-15'},
                 {'name': 'Leg Press (Machine)', 'sets': 3, 'reps': '10-12'}],
        'Shoulders': [{'name': 'Shoulder Press (Machine)', 'sets': 3, 'reps': '10-12'},
                      {'name': 'Front Raises (Light)', 'sets': 3, 'reps': '10-12'}],
        'Biceps': [{'name': 'Bicep Curls (Light Dumbbells)', 'sets': 3, 'reps': '10-12'},
                   {'name': 'Hammer Curls (Light)', 'sets': 3, 'reps': '10-12'}],
        'Triceps': [{'name': 'Tricep Dips (Bench)', 'sets': 3, 'reps': '8-10'},
                    {'name': 'Push-downs (Machine)', 'sets': 3, 'reps': '10-12'}],
        'Cardio': [{'name': 'Brisk Walking', 'sets': 1, 'reps': '20-30 min'},
                   {'name': 'Cycling (Easy)', 'sets': 1, 'reps': '20-30 min'}],
        'Core': [{'name': 'Knee Plank', 'sets': 3, 'reps': '30-45 sec'},
                 {'name': 'Dead Bug', 'sets': 3, 'reps': '10-12/side'}]
    },
    'Intermediate': {
        'Chest': [{'name': 'Push-ups', 'sets': 4, 'reps': '8-12'},
                  {'name': 'Bench Press (Barbell)', 'sets': 4, 'reps': '6-10'}],
        'Back': [{'name': 'Pull-ups', 'sets': 4, 'reps': '6-10'},
                 {'name': 'Bent-over Rows', 'sets': 4, 'reps': '8-12'}],
        'Legs': [{'name': 'Barbell Squats', 'sets': 4, 'reps': '6-10'},
                 {'name': 'Lunges', 'sets': 4, 'reps': '8-10 each leg'}],
        'Shoulders': [{'name': 'Overhead Press', 'sets': 4, 'reps': '6-10'},
                      {'name': 'Lateral Raises', 'sets': 3, 'reps': '10-12'}],
        'Biceps': [{'name': 'Barbell Curls', 'sets': 3, 'reps': '8-10'},
                   {'name': 'Preacher Curls', 'sets': 3, 'reps': '8-12'}],
        'Triceps': [{'name': 'Close-grip Bench', 'sets': 4, 'reps': '6-10'},
                    {'name': 'Dips', 'sets': 3, 'reps': '8-12'}],
        'Cardio': [{'name': 'Running', 'sets': 1, 'reps': '25-40 min'},
                   {'name': 'HIIT (20s/40s)', 'sets': 1, 'reps': '15-20 min'}],
        'Core': [{'name': 'Plank', 'sets': 3, 'reps': '45-60 sec'},
                 {'name': 'Hanging Knee Raises', 'sets': 3, 'reps': '10-12'}]
    },
    'Professional': {
        'Chest': [{'name': 'Weighted Dips', 'sets': 4, 'reps': '6-8'},
                  {'name': 'Incline Bench (Heavy)', 'sets': 5, 'reps': '4-6'}],
        'Back': [{'name': 'Weighted Pull-ups', 'sets': 4, 'reps': '6-8'},
                 {'name': 'Deadlifts', 'sets': 5, 'reps': '3-5'}],
        'Legs': [{'name': 'Front Squats', 'sets': 5, 'reps': '4-6'},
                 {'name': 'Bulgarian Split Squats', 'sets': 4, 'reps': '6-8 each leg'}],
        'Shoulders': [{'name': 'Push Press', 'sets': 4, 'reps': '5-8'},
                      {'name': 'Arnold Press', 'sets': 4, 'reps': '6-8'}],
        'Biceps': [{'name': 'Spider Curls', 'sets': 4, 'reps': '6-8'},
                   {'name': '21s', 'sets': 3, 'reps': '21'}],
        'Triceps': [{'name': 'Weighted Dips', 'sets': 4, 'reps': '6-8'},
                    {'name': 'JM Press', 'sets': 4, 'reps': '6-8'}],
        'Cardio': [{'name': 'Sprints', 'sets': 1, 'reps': '10x100m'},
                   {'name': 'HIIT (40s/20s)', 'sets': 1, 'reps': '20 min'}],
        'Core': [{'name': 'Dragon Flags', 'sets': 3, 'reps': '6-8'},
                 {'name': 'Hanging Leg Raises', 'sets': 3, 'reps': '8-10'}]
    }
}

# Workout splits
splits = {
    'Beginner': {
        'full_body': ['Full Body', 'Cardio/Core', 'Full Body', 'Cardio/Core'],
        'upper_lower': ['Upper', 'Lower', 'Upper', 'Lower', 'Cardio/Core']
    },
    'Intermediate': {
        'push_pull_legs': ['Push', 'Pull', 'Legs', 'Push', 'Pull', 'Legs'],
        'upper_lower': ['Upper', 'Lower', 'Upper', 'Lower', 'Cardio/Core'],
        'bro_split': ['Chest', 'Back', 'Shoulders', 'Arms', 'Legs']
    },
    'Professional': {
        'push_pull_legs': ['Push', 'Pull', 'Legs', 'Push', 'Pull', 'Legs', 'Cardio/Core'],
        'upper_lower': ['Upper', 'Lower', 'Upper', 'Lower', 'Cardio/Core'],
        'power_hypertrophy': ['Power Upper', 'Power Lower', 'Hypertrophy Upper', 'Hypertrophy Lower']
    }
}

# Muscle group mapping
day_type_to_muscle_groups = {
    'Upper': ['Chest', 'Back', 'Shoulders', 'Biceps', 'Triceps'],
    'Lower': ['Legs', 'Core'],
    'Push': ['Chest', 'Shoulders', 'Triceps'],
    'Pull': ['Back', 'Biceps'],
    'Legs': ['Legs', 'Core'],
    'Chest': ['Chest', 'Triceps'],
    'Back': ['Back', 'Biceps'],
    'Shoulders': ['Shoulders'],
    'Arms': ['Biceps', 'Triceps'],
    'Full Body': ['Chest', 'Back', 'Legs', 'Shoulders'],
    'Cardio/Core': ['Cardio', 'Core'],
    'Power Upper': ['Chest', 'Back', 'Shoulders'],
    'Power Lower': ['Legs'],
    'Hypertrophy Upper': ['Chest', 'Back', 'Shoulders', 'Arms'],
    'Hypertrophy Lower': ['Legs', 'Core'],
    'Rest': []
}


class WorkoutGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ultimate Workout Generator")
        self.root.geometry("1000x800")

        # Initialize variables
        self.level_var = tk.StringVar(value="Intermediate")
        self.split_var = tk.StringVar()
        self.weeks_var = tk.IntVar(value=4)
        self.ex_per_group_var = tk.IntVar(value=3)
        self.workout_days_var = tk.IntVar(value=4)
        self.custom_exercises = defaultdict(dict)
        self.previous_workouts = []

        self.create_widgets()

    def create_widgets(self):
        # Create notebook for tabs
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill='both', expand=True)

        # Main tab
        main_frame = ttk.Frame(notebook)
        notebook.add(main_frame, text="Workout Generator")
        self.setup_main_tab(main_frame)

        # Custom Exercises tab
        custom_frame = ttk.Frame(notebook)
        notebook.add(custom_frame, text="Custom Exercises")
        self.setup_custom_exercises_tab(custom_frame)

        # Built-in Exercises tab
        builtin_frame = ttk.Frame(notebook)
        notebook.add(builtin_frame, text="Built-in Exercises")
        self.setup_builtin_exercises_tab(builtin_frame)

    def setup_main_tab(self, parent):
        # Settings frame
        settings_frame = ttk.LabelFrame(parent, text="Workout Settings")
        settings_frame.pack(fill='x', padx=10, pady=10)

        # Level selection
        ttk.Label(settings_frame, text="Fitness Level:").grid(row=0, column=0, sticky='w')
        level_combo = ttk.Combobox(settings_frame, textvariable=self.level_var,
                                   values=["Beginner", "Intermediate", "Professional"])
        level_combo.grid(row=0, column=1, sticky='ew', padx=5, pady=5)
        level_combo.bind("<<ComboboxSelected>>", self.update_split_options)

        # Split selection
        ttk.Label(settings_frame, text="Workout Split:").grid(row=1, column=0, sticky='w')
        self.split_combo = ttk.Combobox(settings_frame, textvariable=self.split_var)
        self.split_combo.grid(row=1, column=1, sticky='ew', padx=5, pady=5)
        self.update_split_options()

        # Days per week
        ttk.Label(settings_frame, text="Days per Week:").grid(row=2, column=0, sticky='w')
        ttk.Spinbox(settings_frame, from_=3, to=7, textvariable=self.workout_days_var).grid(
            row=2, column=1, sticky='ew', padx=5, pady=5)

        # Weeks to plan
        ttk.Label(settings_frame, text="Weeks to Plan:").grid(row=3, column=0, sticky='w')
        ttk.Spinbox(settings_frame, from_=1, to=12, textvariable=self.weeks_var).grid(
            row=3, column=1, sticky='ew', padx=5, pady=5)

        # Exercises per group
        ttk.Label(settings_frame, text="Exercises per Group:").grid(row=4, column=0, sticky='w')
        ttk.Spinbox(settings_frame, from_=2, to=6, textvariable=self.ex_per_group_var).grid(
            row=4, column=1, sticky='ew', padx=5, pady=5)

        # Buttons frame
        buttons_frame = ttk.Frame(parent)
        buttons_frame.pack(fill='x', padx=10, pady=5)

        ttk.Button(buttons_frame, text="Add Custom Exercise", command=self.add_custom_exercise).pack(
            side='left', padx=5)
        ttk.Button(buttons_frame, text="Generate Workout", command=self.generate_workout).pack(
            side='left', padx=5)

        # Output frame
        output_frame = ttk.LabelFrame(parent, text="Workout Plan")
        output_frame.pack(fill='both', expand=True, padx=10, pady=10)

        self.output_text = scrolledtext.ScrolledText(output_frame, wrap=tk.WORD)
        self.output_text.pack(fill='both', expand=True, padx=5, pady=5)

    def setup_custom_exercises_tab(self, parent):
        self.custom_tree = ttk.Treeview(parent, columns=('Level', 'Muscle Group', 'Exercise', 'Sets', 'Reps'))
        self.custom_tree.heading('#0', text='ID')
        self.custom_tree.heading('Level', text='Level')
        self.custom_tree.heading('Muscle Group', text='Muscle Group')
        self.custom_tree.heading('Exercise', text='Exercise')
        self.custom_tree.heading('Sets', text='Sets')
        self.custom_tree.heading('Reps', text='Reps')
        self.custom_tree.pack(fill='both', expand=True, padx=10, pady=10)

        ttk.Button(parent, text="Remove Selected", command=self.remove_custom_exercise).pack(pady=5)

    def setup_builtin_exercises_tab(self, parent):
        self.builtin_tree = ttk.Treeview(parent, columns=('Level', 'Muscle Group', 'Exercise', 'Sets', 'Reps'))
        self.builtin_tree.heading('#0', text='ID')
        self.builtin_tree.heading('Level', text='Level')
        self.builtin_tree.heading('Muscle Group', text='Muscle Group')
        self.builtin_tree.heading('Exercise', text='Exercise')
        self.builtin_tree.heading('Sets', text='Sets')
        self.builtin_tree.heading('Reps', text='Reps')

        # Populate with built-in exercises
        self.refresh_builtin_exercises()

        # Add scrollbar
        yscroll = ttk.Scrollbar(parent, orient='vertical', command=self.builtin_tree.yview)
        self.builtin_tree.configure(yscrollcommand=yscroll.set)

        self.builtin_tree.pack(side='left', fill='both', expand=True)
        yscroll.pack(side='right', fill='y')

    def refresh_builtin_exercises(self):
        self.builtin_tree.delete(*self.builtin_tree.get_children())
        for level, muscles in exercises.items():
            for muscle_group, ex_list in muscles.items():
                for ex in ex_list:
                    self.builtin_tree.insert('', 'end', values=(
                        level, muscle_group, ex['name'], ex['sets'], ex['reps']
                    ))

    def update_split_options(self, event=None):
        level = self.level_var.get()
        available_splits = splits[level]
        split_names = [s.replace('_', ' ').title() for s in available_splits.keys()]
        self.split_combo['values'] = split_names
        if split_names:
            self.split_combo.current(0)

    def add_custom_exercise(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Custom Exercise")

        ttk.Label(add_window, text="Level:").grid(row=0, column=0, padx=5, pady=5)
        level_combo = ttk.Combobox(add_window, values=["Beginner", "Intermediate", "Professional"])
        level_combo.grid(row=0, column=1, padx=5, pady=5)
        level_combo.current(1)

        ttk.Label(add_window, text="Muscle Group:").grid(row=1, column=0, padx=5, pady=5)
        muscle_combo = ttk.Combobox(add_window, values=list(exercises['Beginner'].keys()))
        muscle_combo.grid(row=1, column=1, padx=5, pady=5)
        muscle_combo.current(0)

        ttk.Label(add_window, text="Exercise Name:").grid(row=2, column=0, padx=5, pady=5)
        name_entry = ttk.Entry(add_window)
        name_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(add_window, text="Sets:").grid(row=3, column=0, padx=5, pady=5)
        sets_spin = ttk.Spinbox(add_window, from_=1, to=10)
        sets_spin.grid(row=3, column=1, padx=5, pady=5)
        sets_spin.set(3)

        ttk.Label(add_window, text="Reps:").grid(row=4, column=0, padx=5, pady=5)
        reps_entry = ttk.Entry(add_window)
        reps_entry.grid(row=4, column=1, padx=5, pady=5)
        reps_entry.insert(0, "8-12")

        def save_exercise():
            level = level_combo.get()
            muscle_group = muscle_combo.get()
            name = name_entry.get()
            sets = sets_spin.get()
            reps = reps_entry.get()

            if not name:
                messagebox.showerror("Error", "Please enter an exercise name")
                return

            if muscle_group not in self.custom_exercises[level]:
                self.custom_exercises[level][muscle_group] = []

            self.custom_exercises[level][muscle_group].append({
                'name': name,
                'sets': int(sets),
                'reps': reps
            })

            self.update_custom_exercises_list()
            add_window.destroy()
            messagebox.showinfo("Success", "Exercise added successfully!")

        ttk.Button(add_window, text="Save", command=save_exercise).grid(row=5, columnspan=2, pady=10)

    def update_custom_exercises_list(self):
        self.custom_tree.delete(*self.custom_tree.get_children())
        for level, muscles in self.custom_exercises.items():
            for muscle_group, ex_list in muscles.items():
                for ex in ex_list:
                    self.custom_tree.insert('', 'end', values=(
                        level, muscle_group, ex['name'], ex['sets'], ex['reps']
                    ))

    def remove_custom_exercise(self):
        selected = self.custom_tree.selection()
        if not selected:
            return

        for item in selected:
            values = self.custom_tree.item(item, 'values')
            level = values[0]
            muscle_group = values[1]
            exercise_name = values[2]

            if level in self.custom_exercises and muscle_group in self.custom_exercises[level]:
                self.custom_exercises[level][muscle_group] = [
                    ex for ex in self.custom_exercises[level][muscle_group]
                    if ex['name'] != exercise_name
                ]

                if not self.custom_exercises[level][muscle_group]:
                    del self.custom_exercises[level][muscle_group]

                if not self.custom_exercises[level]:
                    del self.custom_exercises[level]

            self.custom_tree.delete(item)

    def get_available_exercises(self, level, muscle_group):
        base_exercises = exercises.get(level, {}).get(muscle_group, [])
        custom = self.custom_exercises.get(level, {}).get(muscle_group, [])
        return base_exercises + custom

    def generate_workout(self):
        level = self.level_var.get()
        split_name = self.split_combo.get().replace(' ', '_').lower()
        weeks = self.weeks_var.get()
        ex_per_group = self.ex_per_group_var.get()
        workout_days = self.workout_days_var.get()

        # Get base days for selected split
        base_days = splits[level][split_name]
        days_pattern = self.adjust_split_pattern(base_days, workout_days)

        self.output_text.delete(1.0, tk.END)
        self.previous_workouts = []

        for week in range(1, weeks + 1):
            self.output_text.insert(tk.END, f"\n{'=' * 25} WEEK {week} {'=' * 25}\n\n")
            week_plan = days_pattern + ['Rest'] * (7 - len(days_pattern))

            if level != 'Professional':
                random.shuffle(week_plan)

            for day_idx, day_type in enumerate(week_plan, 1):
                if day_type == 'Rest':
                    self.print_workout(week, day_idx, day_type, {})
                else:
                    workout = self.generate_workout_day(level, day_type, week, ex_per_group)
                    self.print_workout(week, day_idx, day_type, workout)

    def generate_workout_day(self, level, day_type, week, exercises_per_group):
        workout_plan = {}
        muscle_groups = day_type_to_muscle_groups.get(day_type, [])

        progression_factor = 1 + (week // 4) * 0.1

        for group in muscle_groups:
            available = [ex for ex in self.get_available_exercises(level, group)
                         if ex['name'] not in self.previous_workouts]

            if not available:
                available = self.get_available_exercises(level, group)

            selected = random.sample(available, min(exercises_per_group, len(available)))

            workout_plan[group] = []
            for ex in selected:
                adjusted_sets = min(6, int(ex['sets'] * progression_factor))
                workout_plan[group].append({
                    'name': ex['name'],
                    'sets': adjusted_sets,
                    'reps': ex['reps']
                })
                self.previous_workouts.append(ex['name'])

        return workout_plan

    def adjust_split_pattern(self, base_days, workout_days):
        if workout_days < len(base_days):
            return base_days[:workout_days]
        elif workout_days > len(base_days):
            repeats = (workout_days // len(base_days)) + 1
            return (base_days * repeats)[:workout_days]
        return base_days

    def print_workout(self, week, day_number, day_type, workout):
        self.output_text.insert(tk.END, f"📅 Week {week} - Day {day_number}: {day_type}\n")
        self.output_text.insert(tk.END, "=" * 60 + "\n")

        if day_type == 'Rest':
            self.output_text.insert(tk.END, "\n🛌 Rest Day - Recovery is part of training!\n")
        else:
            for muscle_group, exs in workout.items():
                self.output_text.insert(tk.END, f"\n💪 {muscle_group.upper()}:\n")
                for ex in exs:
                    self.output_text.insert(tk.END, f"- {ex['name']: <30} {ex['sets']} × {ex['reps']}\n")

        self.output_text.insert(tk.END, "\n" + "=" * 60 + "\n\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = WorkoutGeneratorApp(root)
    root.mainloop()