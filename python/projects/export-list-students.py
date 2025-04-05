import json
from tkinter import Tk, Button, filedialog, messagebox, ttk
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Global variable to store student data
student_data = []

# Function to load student data from the JSON file
def load_students():
    global student_data
    file_path = filedialog.askopenfilename(
        title="Select the students.json file",
        filetypes=[("JSON files", "*.json")]
    )

    if not file_path:
        messagebox.showwarning("No File Selected", "No file was selected. Please try again.")
        return

    try:
        with open(file_path, "r") as file:
            student_data = json.load(file)
        display_students_in_table()
        messagebox.showinfo("Success", "Student data loaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to display students in the table
def display_students_in_table():
    # Clear the table
    for row in table.get_children():
        table.delete(row)

    # Insert student data into the table
    for student in student_data:
        table.insert("", "end", values=(student["name"], student["age"], student["registration_id"]))

# Function to generate a PDF from student data
def generate_pdf():
    if not student_data:
        messagebox.showwarning("No Data", "No student data to export. Please load a JSON file first.")
        return

    pdf_filename = filedialog.asksaveasfilename(
        title="Save PDF As",
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf")]
    )

    if not pdf_filename:
        messagebox.showwarning("No File Selected", "No file was selected for saving the PDF. Please try again.")
        return

    try:
        # Create a PDF file
        c = canvas.Canvas(pdf_filename, pagesize=letter)
        width, height = letter

        # Set the title
        c.setFont("Helvetica-Bold", 16)
        c.drawString(50, height - 50, "List of Registered Students")

        # Set the starting position for the list
        y_position = height - 80

        # Add each student to the PDF
        c.setFont("Helvetica", 12)
        for student in student_data:
            student_info = f"Name: {student['name']}, Age: {student['age']}, Registration ID: {student['registration_id']}"
            c.drawString(50, y_position, student_info)
            y_position -= 20  # Move to the next line

            # Add a new page if necessary
            if y_position < 50:
                c.showPage()
                y_position = height - 50

        # Save the PDF
        c.save()
        messagebox.showinfo("Success", f"PDF generated successfully and saved as {pdf_filename}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main application window
def main():
    global table

    root = Tk()
    root.title("Student List Manager")
    root.geometry("600x400")

    # Create a button to import JSON
    import_button = Button(
        root,
        text="Import JSON",
        command=load_students
    )
    import_button.pack(pady=10)

    # Create a table to display students
    columns = ("Name", "Age", "Registration ID")
    table = ttk.Treeview(root, columns=columns, show="headings")

    # Set column headings
    for col in columns:
        table.heading(col, text=col)
        table.column(col, width=150)

    table.pack(pady=10, fill="both", expand=True)

    # Create a button to export PDF
    export_button = Button(
        root,
        text="Export to PDF",
        command=generate_pdf
    )
    export_button.pack(pady=10)

    # Run the application
    root.mainloop()

# Run the app
if __name__ == "__main__":
    main()