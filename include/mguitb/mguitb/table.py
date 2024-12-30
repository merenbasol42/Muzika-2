import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

class Table(ctk.CTkFrame):
    def __init__(self, master=None, columns=None, data=None, **kwargs):
        super().__init__(master, **kwargs)
        self.columns = columns if columns else []
        self.data = data if data else []
        self._dragging_row = None

        # Treeview widget
        self.tree = ttk.Treeview(self, columns=self.columns, show='headings')
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Configure columns
        for col in self.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor=tk.CENTER)

        # Insert initial data
        for row in self.data:
            self.tree.insert("", tk.END, values=row)

        # Bind mouse events
        self.tree.bind("<ButtonPress-1>", self.__on_row_press)
        self.tree.bind("<B1-Motion>", self.__on_row_drag)
        self.tree.bind("<ButtonRelease-1>", self.__on_row_release)

    def __on_row_press(self, event):
        item = self.tree.identify_row(event.y)
        if item:
            self._dragging_row = item

    def __on_row_drag(self, event):
        if self._dragging_row:
            # Identify target row
            target_row = self.tree.identify_row(event.y)
            if target_row and target_row != self._dragging_row:
                # Check if the target is valid and not the same as the dragging row
                self.tree.move(self._dragging_row, self.tree.parent(target_row), self.tree.index(target_row))

    def __on_row_release(self, event):
        if self._dragging_row:
            # Finalize the dragging operation
            target_row = self.tree.identify_row(event.y)
            if target_row and target_row != self._dragging_row:
                self.tree.move(self._dragging_row, self.tree.parent(target_row), self.tree.index(target_row))
            self._dragging_row = None

    def get_data(self):
        """Returns the current data in the table."""
        rows = []
        for item in self.tree.get_children():
            rows.append(self.tree.item(item, "values"))
        return rows

# Example usage
if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.title("Draggable Table Example")
    root.geometry("600x400")

    columns = ["ID", "Name", "Age"]
    data = [
        [1, "Alice", 25],
        [2, "Bob", 30],
        [3, "Charlie", 35]
    ]

    table = Table(root, columns=columns, data=data)
    table.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    def print_data():
        print(table.get_data())

    button = ctk.CTkButton(root, text="Print Data", command=print_data)
    button.pack(pady=10)

    root.mainloop()
