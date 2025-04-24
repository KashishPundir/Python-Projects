import tkinter as tk
from tkinter import ttk
import webbrowser

# Dictionary containing libraries for each language
libraries = {
    "Python": ["Tkinter", "NumPy", "Pandas", "Matplotlib", "Seaborn"],
    "Java": ["Swing", "JavaFX", "Spring", "Mockito", "Jackson"],
    "JavaScript": ["React", "Vue.js", "Angular", "D3.js", "Node.js"],
    "C++": ["OpenCV", "Boost", "TensorFlow", "POCO", "Qt"],
    "C": ["stdlib", "Judy", "Cairo", "SQLite", "Zlib"],
    "R": ["ggplot2", "plotly", "stats", "Forecast", "readxl", "Caret"],
    "Ruby": ["Nokogiri", "Minitest", "Capybara", "RubyXL", "CarrierWave"]
}

# Dictionary containing documentation links for each library
documentation_links = {
    "Tkinter": "https://docs.python.org/3/library/tkinter.html",
    "NumPy": "https://numpy.org/doc/",
    "Pandas": "https://pandas.pydata.org/pandas-docs/stable/index.html",
    "Matplotlib": "https://matplotlib.org/stable/contents.html",
    "Seaborn": "https://seaborn.pydata.org/",
    "Swing": "https://docs.oracle.com/javase/tutorial/uiswing/index.html",
    "JavaFX": "https://openjfx.io/",
    "Spring": "https://docs.spring.io/spring-framework/reference/data-access.html",
    "Mockito": "https://www.toptal.com/java/a-guide-to-everyday-mockito",
    "Jackson": "https://javadoc.io/doc/com.fasterxml.jackson.core/jackson-core/latest/index.html",
    "React": "https://reactjs.org/docs/getting-started.html",
    "Vue.js": "https://vuejs.org/v2/guide/",
    "Angular": "https://angular.io/docs",
    "D3.js": "https://d3js.org/",
    "Node.js": "https://nodejs.org/api/all.html",
    "OpenCV": "https://docs.opencv.org/4.x/",
    "Boost": "https://beta.boost.org/doc/",
    "TensorFlow": "https://www.tensorflow.org/api_docs",
    "POCO": "https://pocoproject.org/documentation.html",
    "Qt": "https://devdocs.io/qt/",
    "stdlib": "https://stdlib.io/docs/api/latest",
    "Judy": "http://mutationtesting.org/judy/documentation/",
    "Cairo": "https://www.cairographics.org/documentation/",
    "SQLite": "https://www.sqlite.org/docs.html",
    "Zlib": "https://www.zlib.net/manual.html",
    "ggplot2": "https://www.rdocumentation.org/packages/ggplot2/versions/3.5.0",
    "plotly": "https://plotly.com/python/",
    "stats": "https://www.rdocumentation.org/packages/stats/versions/3.6.2",
    "Forecast": "https://www.rdocumentation.org/packages/forecast/versions/8.22.0",
    "readxl": "https://www.rdocumentation.org/packages/readxl/versions/1.4.3",
    "Caret": "https://www.rdocumentation.org/packages/caret/versions/6.0-94",
    "Nokogiri": "https://devdocs.io/nokogiri/",
    "Minitest": "https://devdocs.io/minitest/",
    "Capybara": "https://rubydoc.info/github/jnicklas/capybara",
    "RubyXL": "https://www.rubydoc.info/gems/rubyXL/",
    "CarrierWave": "https://www.rubydoc.info/gems/carrierwave/CarrierWave"
}

def on_language_select(event):
    # Clear the libraries dropdown
    library_combobox.set('')

    # Update the libraries dropdown based on the selected language
    selected_language = language_combobox.get()
    if selected_language in libraries:
        library_combobox.config(values=libraries[selected_language])
    else:
        library_combobox.config(values=[])

def display_documentation():
    # Get the selected language and library
    selected_library = library_combobox.get()

    # Retrieve the documentation link for the selected library
    if selected_library in documentation_links:
        doc_link = documentation_links[selected_library]
        webbrowser.open_new_tab(doc_link)

def change_theme(event=None):
    selected_theme = theme_combobox.get()
    if selected_theme == "Light":
        root.configure(bg="white")
        style.theme_use("default")
    elif selected_theme == "Dark":
        root.configure(bg="#333333")
        style.theme_use("clam")

# Create Tkinter window
root = tk.Tk()
root.title('Library Documentation Viewer')
root.configure(bg='white')  # Set background color

# Style for button
style = ttk.Style()

# Language dropdown
language_label = ttk.Label(root, text="Select Language:", background='white', font=('Arial', 12, 'bold'))
language_label.grid(row=0, column=0, padx=10, pady=10)
languages = list(libraries.keys())
language_combobox = ttk.Combobox(root, values=languages, state="readonly", font=('Arial', 10))
language_combobox.grid(row=0, column=1, padx=10, pady=10)
language_combobox.bind("<<ComboboxSelected>>", on_language_select)

# Library dropdown
library_label = ttk.Label(root, text="Select Library:", background='white', font=('Arial', 12, 'bold'))
library_label.grid(row=1, column=0, padx=10, pady=10)
library_combobox = ttk.Combobox(root, state="readonly", font=('Arial', 10))
library_combobox.grid(row=1, column=1, padx=10, pady=10)

# Button to display documentation
display_button = ttk.Button(root, text="Open Documentation Link", command=display_documentation)
display_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Theme dropdown
theme_label = ttk.Label(root, text="Select Theme:", background='white', font=('Arial', 12, 'bold'))
theme_label.grid(row=3, column=0, padx=10, pady=10)
theme_combobox = ttk.Combobox(root, values=["Light", "Dark"], state="readonly", font=('Arial', 10))
theme_combobox.grid(row=3, column=1, padx=10, pady=10)
theme_combobox.set("Light")  # Default theme
theme_combobox.bind("<<ComboboxSelected>>", change_theme)

root.mainloop()

