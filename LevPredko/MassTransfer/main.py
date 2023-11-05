import tkinter as tk


def convert_mass():
    mass = float(entry_mass.get())
    from_unit = combo_from.get()
    to_unit = combo_to.get()

    conversions = {
        ('grams', 'grams'): mass,
        ('grams', 'kilograms'): mass / 1000,
        ('grams', 'tons'): mass / 1000000,
        ('grams', 'centners'): mass / 10000,
        ('grams', 'carats'): mass * 5,
        ('kilograms', 'grams'): mass * 1000,
        ('kilograms', 'kilograms'): mass,
        ('kilograms', 'tons'): mass / 1000,
        ('kilograms', 'centners'): mass / 100,
        ('kilograms', 'carats'): mass * 5000,
        ('tons', 'grams'): mass * 1000000,
        ('tons', 'kilograms'): mass * 1000,
        ('tons', 'tons'): mass,
        ('tons', 'centners'): mass * 10,
        ('tons', 'carats'): mass * 5000000,
        ('centners', 'grams'): mass * 10000,
        ('centners', 'kilograms'): mass * 100,
        ('centners', 'tons'): mass / 10,
        ('centners', 'centners'): mass,
        ('centners', 'carats'): mass * 50000,
        ('carats', 'grams'): mass / 5,
        ('carats', 'kilograms'): mass / 5000,
        ('carats', 'tons'): mass / 5000000,
        ('carats', 'centners'): mass / 50000,
        ('carats', 'carats'): mass,
    }

    result = conversions[(from_unit, to_unit)]
    result_var.set(f"{result:.3f} {to_unit}")


window = tk.Tk()
window.resizable(False, False)
window.title("Mass Converter")


label_mass = tk.Label(window, text="Enter Mass:")
label_mass.grid(row=0, column=0, padx=10, pady=10)

entry_mass = tk.Entry(window)
entry_mass.grid(row=0, column=1, padx=10, pady=10)

combo_from = tk.StringVar(window)
combo_from.set("grams")
dropdown_from = tk.OptionMenu(window, combo_from, "grams", "carats", "kilograms","centners","tons")
dropdown_from.grid(row=0, column=2, padx=10, pady=10)

result_label = tk.Label(window, text="Result:")
result_label.grid(row=1, column=0, padx=10, pady=10)

result_var = tk.StringVar(window)
result_var.set("")
result_entry = tk.Entry(window, textvariable=result_var, state='readonly')  # state='readonly' вимикає редагування
result_entry.grid(row=1, column=1, padx=10, pady=10)

combo_to = tk.StringVar(window)
combo_to.set("grams")
dropdown_to = tk.OptionMenu(window, combo_to, "grams", "carats", "kilograms","centners","tons")
dropdown_to.grid(row=1, column=2, padx=10, pady=10)

convert_button = tk.Button(window, text="Convert", command=convert_mass)
convert_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10)


window.mainloop()
