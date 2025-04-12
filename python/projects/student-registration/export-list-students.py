import json
from tkinter import Tk, Button, filedialog, messagebox, ttk
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Function to load student data from the JSON file
def load_students(table):
    file_path = filedialog.askopenfilename(
        title="Select the students.json file",
        filetypes=[("JSON files", "*.json")]
    )
    if file_path:
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
                update_table(table, data)
        except Exception as e:
            messagebox.showerror("Error", f"Error loading data: {e}")

# Function to update the table with student data
def update_table(table, data):
    for item in table.get_children():
        table.delete(item)
    for student in data:
        table.insert("", "end", values=(student["name"], student["age"], student["registration_id"]))

# Function to export student data to a PDF
def export_to_pdf(table):
    file_path = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf")]
    )
    if file_path:
        try:
            c = canvas.Canvas(file_path, pagesize=letter)
            c.setFont("Helvetica", 12)
            y = 750
            for item in table.get_children():
                values = table.item(item, 'values')
                text = ", ".join(values)
                c.drawString(50, y, text)
                y -= 20
            c.save()
            messagebox.showinfo("Success", "PDF exported successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error exporting to PDF: {e}")

# Create the main application window
def main():
    root = Tk()
    root.title("Student Data Viewer")

    columns = ("Name", "Age", "Registration ID")
    table = ttk.Treeview(root, columns=columns, show="headings")
    for col in columns:
        table.heading(col, text=col)
    table.pack(pady=10)

    load_button = Button(root, text="Load Data", command=lambda: load_students(table))
    load_button.pack(pady=5)

    export_button = Button(root, text="Export to PDF", command=lambda: export_to_pdf(table))
    export_button.pack(pady=5)

    root.mainloop()

# Run the app
if __name__ == "__main__":
    main()