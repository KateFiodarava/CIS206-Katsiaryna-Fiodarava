import tkinter as tk
from tkinter import messagebox
import json
from datetime import date

# Define Patient class
class Patient:
    def __init__(self, first, middle, last, address, city, state, zip_code, phone, emergency_name, emergency_phone):
        self.first = first
        self.middle = middle
        self.last = last
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone
        self.emergency_name = emergency_name
        self.emergency_phone = emergency_phone

# Define Procedure class
class Procedure:
    def __init__(self, name, practitioner, charge):
        self.name = name
        self.procedure_date = str(date.today())
        self.practitioner = practitioner
        self.charge = charge

# Predefined procedures
procedure_list = [
    Procedure("X-Ray", "Dr. Smith", 250.0),
    Procedure("MRI", "Dr. Lee", 1500.0),
    Procedure("Blood Test", "Nurse Kim", 200.0)
]

# Main App
class InvoiceApp:
    def __init__(self, root):
        self.root = root
        root.title("Patient Info and Invoice Generator")
        root.resizable(False, False)

        # Patient Info Frame with border
        self.patient_frame = tk.LabelFrame(root, text="Patient Information", padx=10, pady=10, borderwidth=2, relief="groove")
        self.patient_frame.grid(row=0, column=0, padx=10, pady=10)

        self.entries = {}
        fields = ["First Name", "Middle Name", "Last Name", "Address", "City", "State", "ZIP Code", "Phone", "Emergency Contact Name", "Emergency Contact Phone"]
        for i, field in enumerate(fields):
            label = tk.Label(self.patient_frame, text=field + ":")
            label.grid(row=i, column=0, sticky="e", padx=5, pady=3)
            entry = tk.Entry(self.patient_frame, width=35)
            entry.grid(row=i, column=1, padx=5, pady=3)
            self.entries[field] = entry

        # Procedure Frame with border
        self.procedure_frame = tk.LabelFrame(root, text="Select Procedures", padx=10, pady=10, borderwidth=2, relief="groove")
        self.procedure_frame.grid(row=1, column=0, padx=10, pady=10)

        self.check_vars = []
        for i, proc in enumerate(procedure_list):
            var = tk.IntVar()
            chk = tk.Checkbutton(self.procedure_frame, text=f"{proc.name} (${proc.charge:.2f})", variable=var)
            chk.grid(row=i, column=0, sticky="w", padx=25)
            self.check_vars.append(var)

        # Buttons
        button_frame = tk.Frame(root)
        button_frame.grid(row=2, column=0, pady=10)

        tk.Button(button_frame, text="Generate Invoice", command=self.generate_invoice, width=18).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Save as JSON", command=self.save_json, width=18).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Clear Invoice", command=self.clear_invoice, width=18).pack(side=tk.LEFT, padx=5)  # New Clear Invoice button

        # Invoice Display
        self.invoice_text = tk.Text(root, height=15, width=60, state=tk.DISABLED, bg="black", fg="white")
        self.invoice_text.grid(row=3, column=0, padx=10, pady=5)

    def validate_names(self, data):
        # Check if name fields contain digits
        name_fields = ["first_name", "middle_name", "last_name", "emergency_contact_name"]
        for field in name_fields:
            value = data.get(field, "")
            if any(char.isdigit() for char in value):
                messagebox.showerror("Invalid Input", f"{field.replace('_', ' ').title()} cannot contain numbers.")
                return False
        return True

    def clear_inputs(self):
        # Clear all entry fields
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        # Uncheck all procedure checkboxes
        for var in self.check_vars:
            var.set(0)

    def clear_invoice(self):
        # Clear the invoice text area
        self.invoice_text.config(state=tk.NORMAL)
        self.invoice_text.delete("1.0", tk.END)
        self.invoice_text.config(state=tk.DISABLED)

    def generate_invoice(self):
        # Get patient info
        data = {k.replace(" ", "_").lower(): e.get().strip() for k, e in self.entries.items()}

        # Validate names for digits
        if not self.validate_names(data):
            return

        # Validate all required fields are filled
        required_fields = ["first_name", "last_name", "phone", "emergency_contact_name", "emergency_contact_phone"]
        for field in required_fields:
            if not data.get(field):
                messagebox.showwarning("Missing Information", f"Please fill in the {field.replace('_', ' ').title()} field.")
                return

        # Create patient object
        self.patient = Patient(
            data.get("first_name"),
            data.get("middle_name", ""),
            data.get("last_name"),
            data.get("address", ""),
            data.get("city", ""),
            data.get("state", ""),
            data.get("zip_code", ""),
            data.get("phone"),
            data.get("emergency_contact_name"),
            data.get("emergency_contact_phone")
        )

        # Get selected procedures
        self.selected = [procedure_list[i] for i, var in enumerate(self.check_vars) if var.get() == 1]

        if not self.selected:
            messagebox.showwarning("No Procedures", "Please select at least one procedure.")
            return

        # Display invoice
        self.invoice_text.config(state=tk.NORMAL)
        self.invoice_text.delete("1.0", tk.END)
        self.invoice_text.insert(tk.END, f"Invoice Date: {date.today()}\n")
        self.invoice_text.insert(tk.END, f"Patient: {self.patient.first} {self.patient.middle} {self.patient.last}\n")
        self.invoice_text.insert(tk.END, f"Phone: {self.patient.phone}\n")
        self.invoice_text.insert(tk.END, f"Emergency Contact: {self.patient.emergency_name} ({self.patient.emergency_phone})\n")
        self.invoice_text.insert(tk.END, "\nProcedures:\n")

        total = 0
        for proc in self.selected:
            self.invoice_text.insert(tk.END, f"- {proc.name} by {proc.practitioner} on {proc.procedure_date}: ${proc.charge:.2f}\n")
            total += proc.charge

        self.invoice_text.insert(tk.END, f"\nTotal Charges: ${total:.2f}")
        self.invoice_text.config(state=tk.DISABLED)

        # Clear input fields and checkboxes but keep invoice text visible
        self.clear_inputs()

    def save_json(self):
        if not hasattr(self, 'patient') or not hasattr(self, 'selected') or not self.selected:
            messagebox.showerror("Missing Info", "Please generate an invoice before saving.")
            return

        invoice = {
            "invoice_date": str(date.today()),
            "patient": {
                "first_name": self.patient.first,
                "middle_name": self.patient.middle,
                "last_name": self.patient.last,
                "address": self.patient.address,
                "city": self.patient.city,
                "state": self.patient.state,
                "zip_code": self.patient.zip_code,
                "phone": self.patient.phone,
                "emergency_contact": {
                    "name": self.patient.emergency_name,
                    "phone": self.patient.emergency_phone
                }
            },
            "procedures": [
                {
                    "name": proc.name,
                    "date": proc.procedure_date,
                    "practitioner": proc.practitioner,
                    "charge": proc.charge
                } for proc in self.selected
            ],
            "total_charges": sum(proc.charge for proc in self.selected)
        }

        try:
            with open("invoice.json", "w") as f:
                json.dump(invoice, f, indent=4)
            messagebox.showinfo("Saved", "Invoice saved successfully as 'invoice.json'.")
        except Exception as e:
            messagebox.showerror("Error Saving File", f"An error occurred saving the file: {e}")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = InvoiceApp(root)
    root.mainloop()
