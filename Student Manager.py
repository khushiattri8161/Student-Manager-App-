from tkinter import *
from tkinter import messagebox

# ---------------- WINDOW ----------------
root = Tk()
root.title("Student Manager App")
root.geometry("650x780")
root.config(bg="#1E1E2E")
#root.resizable(False, False)

student = {}

# ---------------- TITLE ----------------
title = Label(
    root,
    text="📚 Student Manager App",
    font=("Comic Sans MS", 24, "bold"),
    bg="#1E1E2E",
    fg="#FFB6C1"
)
title.pack(pady=10)

subtitle = Label(
    root,
    text="Manage Students Easily",
    font=("Arial", 11),
    bg="#1E1E2E",
    fg="lightgray"
)
subtitle.pack()

# ---------------- STUDENT COUNT ----------------
count_label = Label(
    root,
    text="Total Students: 0",
    font=("Arial", 12, "bold"),
    bg="#1E1E2E",
    fg="#FFD700"
)
count_label.pack(pady=5)

# ---------------- INPUT FRAME ----------------
frame = Frame(root, bg="#2A2A40", bd=3, relief=RIDGE)
frame.pack(pady=15, padx=20, fill="x")

Label(
    frame,
    text="Student Name",
    font=("Arial", 12, "bold"),
    bg="#2A2A40",
    fg="white"
).pack(pady=5)

name_entry = Entry(
    frame,
    font=("Arial", 12),
    width=30,
    bg="#3B3B58",
    fg="white",
    insertbackground="white"
)
name_entry.pack(pady=5)

Label(
    frame,
    text="Marks",
    font=("Arial", 12, "bold"),
    bg="#2A2A40",
    fg="white"
).pack(pady=5)

marks_entry = Entry(
    frame,
    font=("Arial", 12),
    width=30,
    bg="#3B3B58",
    fg="white",
    insertbackground="white"
)
marks_entry.pack(pady=5)

# ---------------- FUNCTIONS ----------------
def update_count():
    count_label.config(
        text=f"Total Students: {len(student)}"
    )


def add_student():
    name = name_entry.get().strip()
    marks = marks_entry.get().strip()

    if name == "" or marks == "":
        messagebox.showwarning(
            "Warning",
            "Please fill all details!"
        )
        return

    try:
        marks = int(marks)

        if marks < 0 or marks > 100:
            messagebox.showerror(
                "Error",
                "Marks must be between 0 and 100!"
            )
            return

        student[name] = marks
        update_count()

        messagebox.showinfo(
            "Success",
            f"{name} Successfully Added! 🎉"
        )

        name_entry.delete(0, END)
        marks_entry.delete(0, END)

    except:
        messagebox.showerror(
            "Error",
            "Marks must be a number!"
        )


def view_students():
    result_box.delete("1.0", END)

    if not student:
        result_box.insert(
            END,
            "❌ No students found!"
        )

    else:
        result_box.insert(
            END,
            "📋 Student Report\n\n"
        )

        for name, marks in student.items():

            if marks >= 90:
                grade = "A+"
            elif marks >= 75:
                grade = "A"
            elif marks >= 60:
                grade = "B"
            elif marks >= 33:
                grade = "C"
            else:
                grade = "F"

            result_box.insert(
                END,
                f"👤 {name}\n"
                f"📊 Marks: {marks}\n"
                f"🏆 Grade: {grade}\n"
                f"{'-'*30}\n"
            )


def check_result():
    name = name_entry.get().strip()

    if name in student:
        marks = student[name]

        if marks >= 33:
            result = "PASS ✅"
        else:
            result = "FAIL ❌"

        messagebox.showinfo(
            "Result",
            f"{name}\nMarks: {marks}\n{result}"
        )

    else:
        messagebox.showwarning(
            "Not Found",
            "Student not found!"
        )


def delete_student():
    name = name_entry.get().strip()

    if name in student:
        del student[name]
        update_count()

        messagebox.showinfo(
            "Deleted",
            f"{name} removed successfully!"
        )

    else:
        messagebox.showwarning(
            "Error",
            "Student not found!"
        )


def clear_output():
    result_box.delete("1.0", END)


# ---------------- BUTTONS ----------------
button_frame = Frame(root, bg="#1E1E2E")
button_frame.pack(pady=10)

btn_style = {
    "font": ("Arial", 11, "bold"),
    "width": 16,
    "height": 2,
    "bd": 0,
    "cursor": "hand2"
}

Button(
    button_frame,
    text="➕ Add Student",
    bg="#FF69B4",
    fg="white",
    command=add_student,
    **btn_style
).grid(row=0, column=0, padx=8, pady=8)

Button(
    button_frame,
    text="📋 View Student",
    bg="#9370DB",
    fg="white",
    command=view_students,
    **btn_style
).grid(row=0, column=1, padx=8, pady=8)

Button(
    button_frame,
    text="✅ Check Result",
    bg="#20B2AA",
    fg="white",
    command=check_result,
    **btn_style
).grid(row=1, column=0, padx=8, pady=8)

Button(
    button_frame,
    text="🗑 Delete Student",
    bg="#FFA500",
    fg="white",
    command=delete_student,
    **btn_style
).grid(row=1, column=1, padx=8, pady=8)

Button(
    button_frame,
    text="🧹 Clear Output",
    bg="#808080",
    fg="white",
    command=clear_output,
    **btn_style
).grid(row=2, column=0, padx=8, pady=8)

Button(
    button_frame,
    text="❌ Exit",
    bg="#FF4C4C",
    fg="white",
    command=root.destroy,
    **btn_style
).grid(row=2, column=1, padx=8, pady=8)

# ---------------- OUTPUT BOX WITH SCROLLBAR ----------------
output_frame = Frame(root, bg="#1E1E2E")
output_frame.pack(pady=20)

scrollbar = Scrollbar(output_frame)

result_box = Text(
    output_frame,
    height=12,
    width=55,
    font=("Consolas", 11),
    bg="#2A2A40",
    fg="white",
    bd=0,
    yscrollcommand=scrollbar.set
)

scrollbar.config(command=result_box.yview)

scrollbar.pack(side=RIGHT, fill=Y)
result_box.pack(side=LEFT)

# ---------------- FOOTER ----------------
footer = Label(
    root,
    text=" Made with Python Tkinter ❤️",
    font=("Arial", 9),
    bg="#1E1E2E",
    fg="gray"
)
footer.pack(side=BOTTOM, pady=10)

root.mainloop()