from ACCImport import *
from CustomTableWidget import *
from CustomTextEditWidget import *

# Main GUI
class ClozeTable(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.cloze_counters = {} # Dictionary to keep track of cloze counters
        self.nomenclature = "" # Initialize a nomenclature
        self.offset = "" # V: Initialize offset


    def update_nomenclature(self, text):
        self.nomenclature = text

    def update_offset(self, offset_number):
        self.offset = offset_number

    def cloze_text_changed(self, row):
        cloze_column_widget = self.table.cellWidget(row, 2)
        cloze_text = cloze_column_widget.toPlainText()
        if cloze_text.strip():  # Check if there's text in the cloze column
            offset = int(self.offset) + 1
            number = self.nomenclature + f"{row + offset:04d}"  # Format the number with leading zeros
            self.table.setItem(row, 0, QTableWidgetItem(number))  # Update the "Number" column

    def initUI(self):
        self.setWindowTitle('Anki Card Creator')
        self.setWindowIcon(QIcon('ankiankicardcretor.ico')) # V: Added an icon for the program. Paste of /dist when bundled by the installer.
        self.setGeometry(100, 100, 800, 600)

        # Create table
        self.table = CustomTableWidget(self)
        self.table.setRowCount(500)  # Set this to the number of rows you want
        self.table.setColumnCount(6)  # We have 6 columns
        
        # Adjust rows widths to fit content
        self.table.resizeRowsToContents()

        # Allow users to resize columns manually
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Interactive)  # Enable manual resizing for all columns

        # Set up the table setHorizontalHeaderLabels
        headers = ['Number', 'Title', 'Cloze Column', 'Topic', 'Back Extra', 'Back Image']
        self.table.setHorizontalHeaderLabels(headers)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.table)

        # Add a line edit for the user to specify the nomenclature
        self.nomenclature_input = QLineEdit(self)
        self.nomenclature_input.setPlaceholderText("Enter identifier (e.g., 'FAR.CM.')")
        self.offset_input = QLineEdit(self)
        self.offset_input.setPlaceholderText("Enter number to offset starting")
        layout.addWidget(self.offset_input)
        layout.addWidget(self.nomenclature_input)

        # Connect the line edit to a method to update the nomenclature
        self.nomenclature_input.textChanged.connect(self.update_nomenclature)
        self.offset_input.textChanged.connect(self.update_offset)

        # Add a QTextEdit widget for the cloze column
        for row in range(self.table.rowCount()):
            text_edit_widget = CustomTextEdit(self)
            text_edit_widget.textChanged.connect(lambda row=row: self.update_row_height_cc(row)) # Update the row height
            text_edit_widget.textChanged.connect(lambda row=row: self.cloze_text_changed(row)) # Check changes
            self.table.setCellWidget(row, 2, text_edit_widget)
            # QTextEdit Read-Only
            text_edit_widget.setReadOnly(True)

        # Add a QTextEdit widget for the Back Extra
        for row in range(self.table.rowCount()):
            text_edit_widget = CustomTextEdit(self)
            text_edit_widget.textChanged.connect(lambda row=row: self.update_row_height_be(row))
            self.table.setCellWidget(row, 4, text_edit_widget)
            # QTextEdit Read-Only
            text_edit_widget.setReadOnly(True)

        # Create a central widget and set the layout on it
        central_widget = QWidget(self)  # Create a central widget
        central_widget.setLayout(layout)  # Set the layout on the central widget

        self.setCentralWidget(central_widget)  # Set the central widget of the main window

        # Export button
        self.export_button = QPushButton('Export Data', self)
        self.export_button.clicked.connect(self.export_data)
        layout.addWidget(self.export_button)

        # Set the layout
        #container = self.centralWidget()
        #container.setLayout(layout)

        # Shortcuts
        self.shortcut_incremental_cloze = QShortcut(QKeySequence('Ctrl+Shift+C'), self)
        self.shortcut_incremental_cloze.activated.connect(self.apply_incremental_cloze)

        self.shortcut_same_number_cloze = QShortcut(QKeySequence('Ctrl+Shift+Alt+C'), self)
        self.shortcut_same_number_cloze.activated.connect(self.apply_same_number_cloze)

    def update_row_height_cc(self, row):
        text_edit_widget = self.table.cellWidget(row, 2)
        # Calculate the height and add some margin
        height = text_edit_widget.document().size().height() + 10
        # Round the height to the nearest int
        rounded_height = int(round(height))
        self.table.setRowHeight(row, rounded_height)

    def update_row_height_be(self, row):
        text_edit_widget = self.table.cellWidget(row, 4)
        # Calculate the height and add some margin
        height = text_edit_widget.document().size().height() + 10
        # Round the height to the nearest int
        rounded_height = int(round(height))
        self.table.setRowHeight(row, rounded_height)

    def apply_incremental_cloze(self):
        # Get the current selected row and column
        current_row = self.table.currentRow()
        current_column = 2  # Assuming cloze column is always column index 2
        
        # Get the QTextEdit widget in the specified cell
        text_edit_widget = self.table.cellWidget(current_row, current_column)
        
        if isinstance(text_edit_widget, QTextEdit):
            cursor = text_edit_widget.textCursor()
            if cursor.hasSelection():
                selected_text = cursor.selectedText()

                # Check if the cell already has a cloze counter
                cell_key = (current_row, current_column)
                if cell_key not in self.cloze_counters:
                    self.cloze_counters[cell_key] = 1
                else:
                    self.cloze_counters[cell_key] += 1

                # Apply cloze deletion using the cell-specific counter
                cloze_counter = self.cloze_counters[cell_key]
                cloze_text = f'{{{{c{cloze_counter}::{selected_text}}}}}'
                cursor.insertText(cloze_text)
                # self.cloze_counter += 1

    def apply_same_number_cloze(self):
        # Get the current selected row and column
        current_row = self.table.currentRow()
        current_column = 2  # Assuming cloze column is always column index 2
        
        # Get the QTextEdit widget in the specified cell
        text_edit_widget = self.table.cellWidget(current_row, current_column)
        
        if isinstance(text_edit_widget, QTextEdit):
            cursor = text_edit_widget.textCursor()
            if cursor.hasSelection():
                cell_key = (current_row, current_column)
                if cell_key in self.cloze_counters:
                    # Use the last counter used in current cell
                    cloze_counter = self.cloze_counters[cell_key]
                    selected_text = cursor.selectedText()
                    cloze_text = f'{{{{c{cloze_counter}::{selected_text}}}}}' # V: Removed the -1 to keep up with the counter
                    cursor.insertText(cloze_text)

    def export_data(self):
        # Open a file dialog to specify the path and file name for export
        path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt)")
        if not path:  # If no path is provided, return without doing anything
            return

        with open(path, 'w', encoding='utf-8') as file:
            for row in range(self.table.rowCount()):
                row_data = []
                row_is_empty = True  # Assume the row is empty until we find data
                for column in range(self.table.columnCount()):
                    if column == 2:  # Cloze column with QTextEdit
                        text_edit_widget = self.table.cellWidget(row, column)
                        text = text_edit_widget.toPlainText()
                        # Replace line breaks with a placeholder
                        text = text.replace('\n', '<br>')
                    else:  # Other columns with QTableWidgetItem
                        cell_item = self.table.item(row, column)
                        text = cell_item.text() if cell_item else ''
                    row_data.append(text)
                    if text.strip():  # If there's any text, mark the row as non-empty
                        row_is_empty = False
                # Write the tab-delimited row to the file only if the row is not empty
                if not row_is_empty:
                    file.write('\t'.join(row_data) + '\n')

        # Show a message box that the data was exported successfully
        QMessageBox.information(self, "Export Successful", f"Data exported to '{path}'")