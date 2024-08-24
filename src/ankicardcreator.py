import sys
from PyQt5.QtWidgets import QInputDialog, QSplashScreen, QLineEdit, QHeaderView, QWidget, QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout, QPushButton, QShortcut, QFileDialog, QMessageBox
from PyQt5.QtGui import QKeySequence, QIcon, QPixmap
from PyQt5.QtCore import Qt, QFile, QTextStream
import stylesheets.breeze_resources


class CustomTextEdit(QTextEdit):
    def focusOutEvent(self, event):
        super().focusOutEvent(event)
        self.setReadOnly(True) # Make the QTextEdit read-only when it loses focus

    def keyPressEvent(self, event):
        if self.isReadOnly():
            if event.key() in (Qt.Key_Up, Qt.Key_Down, Qt.Key_Left, Qt.Key_Right):
                # Pass the event to the parent (table) only if read-only
                # self.clearFocus()  # Remove focus from QTextEdit # V: Removed to retain focus on the cells
                self.parent().keyPressEvent(event)  # Let the parent handle the navigation
            elif event.key() == Qt.Key_Escape:
                # Exit edit mode and make the QTextEdit read-only
                self.setReadOnly(True)
                self.clearFocus()  # Remove focus from QTextEdit
                self.parent().setFocus()  # Move the focus back to the parent table
            else:
                super().keyPressEvent(event)
        else:
            # Default behavior when editable
            if event.key() == Qt.Key_Escape:
                # Exit edit mode and make the QTextEdit read-only
                self.setReadOnly(True)
                self.clearFocus()  # Remove focus from QTextEdit
                self.parent().setFocus()  # Move the focus back to the parent table
            else:
                super().keyPressEvent(event)

class CustomTableWidget(QTableWidget):
    def keyPressEvent(self, event):
        current_row = self.currentRow()
        current_column = self.currentColumn()

        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            column_index = self.columnCount() - 1
            if current_column == column_index:  # Index of Cloze column and Back Exta
                text_edit_widget = self.cellWidget(current_row, current_column)
                if isinstance(text_edit_widget, CustomTextEdit):
                    text_edit_widget.setReadOnly(False)  # Make the QTextEdit editable
                    text_edit_widget.setFocus()  # Set focus to the QTextEdit
            event.accept()  # Prevent further processing
        else:
            current_row = self.currentRow()
            current_column = self.currentColumn()
            # Check if the event was ignored by a child widget
            if not event.isAccepted():
                # Handle arrow keys for navigation
                if event.key() == Qt.Key_Up and current_row > 0:
                    self.setCurrentCell(current_row - 1, current_column)
                elif event.key() == Qt.Key_Down and current_row < self.rowCount() - 1:
                    self.setCurrentCell(current_row + 1, current_column)
                elif event.key() == Qt.Key_Left and current_column > 0:
                    self.setCurrentCell(current_row, current_column - 1)
                elif event.key() == Qt.Key_Right and current_column < self.columnCount() - 1:
                    self.setCurrentCell(current_row, current_column + 1)
                else:
                    super().keyPressEvent(event)  # Handle other key events normally
            else:
                # If the event was accepted (handled by CustomTextEdit), do nothing
                super().keyPressEvent(event)

class EditableHeaderView(QHeaderView):
    def __init__(self, orientation, parent=None):
        super().__init__(orientation, parent)
        self.setSectionsClickable(True)
        self.sectionDoubleClicked.connect(self.on_sectionDoubleClicked)

    def on_sectionDoubleClicked(self, index):
        # Create a QLineEdit to edit the header
        self.editor = QLineEdit(self)
        header_text = self.model().headerData(index, self.orientation(), Qt.DisplayRole)
        self.editor.setText(header_text)
        self.editor.setGeometry(self.sectionViewportPosition(index), 0, self.sectionSize(index), self.height())
        self.editor.setFocus()
        self.editor.show()
        self.editor.selectAll()
        self.editor.editingFinished.connect(lambda: self.on_editingFinished(index))

    def on_editingFinished(self, index):
        # Update the header with the new text and remove the QLineEdit
        new_header = self.editor.text()
        self.model().setHeaderData(index, self.orientation(), new_header, Qt.EditRole)
        self.editor.deleteLater()

# Main GUI
class CardTable(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.cloze_counters = {} # Dictionary to keep track of cloze counters
        self.nomenclature = "" # Initialize a nomenclature
        self.offset = 0 # V: Initialize offset

        self.table.setHorizontalHeader(EditableHeaderView(Qt.Horizontal, self.table))

    def update_nomenclature(self, text):
        self.nomenclature = text

    def update_offset(self, offset_number):
        self.offset = offset_number

    def cloze_text_changed(self, row):
        column_index = self.table.columnCount() - 1
        cloze_column_widget = self.table.cellWidget(row, column_index)
        cloze_text = cloze_column_widget.toPlainText()
        if cloze_text.strip():  # Check if there's text in the cloze column
            offset = int(self.offset) + 1
            number = self.nomenclature + f"{row + offset:04d}"  # Format the number with leading zeros
            self.table.setItem(row, 0, QTableWidgetItem(number))  # Update the "Number" column

    def initUI(self):
        self.setWindowTitle('Anki Card Creator')
        self.setWindowIcon(QIcon('ankicardcreator.ico')) # V: Added an icon for the program. Paste to /dist when bundled by the installer.
        self.setGeometry(100, 100, 1000, 600)

        # Create table
        self.table = CustomTableWidget(self)
        self.table.setRowCount(500)  # Set this to the number of rows you want
        self.table.setColumnCount(1)  # V: We set the initial column to 1
        
        # Adjust rows widths to fit content
        self.table.resizeRowsToContents()

        # Allow users to resize columns manually
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Interactive)  # Enable manual resizing for all columns

        # Set up the table setHorizontalHeaderLabels
        headers = ['Sort Column']
        self.table.setHorizontalHeaderLabels(headers)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.table)

        # Add a line edit for the user to specify the nomenclature
        self.nomenclature_input = QLineEdit(self)
        self.nomenclature_input.setPlaceholderText("Enter identifier (e.g., 'SUBJECT.LESSON.'). Cannot be empty.")
        self.offset_input = QLineEdit(self)
        self.offset_input.setPlaceholderText("Enter number to offset starting point if you already have notes on the deck. This is to avoid duplication. Cannot be empty.")
        layout.addWidget(self.offset_input)
        layout.addWidget(self.nomenclature_input)

        # Connect the line edit to a method to update the nomenclature
        self.nomenclature_input.textChanged.connect(self.update_nomenclature)
        self.offset_input.textChanged.connect(self.update_offset)

        # V: Placeholder this is where we add the custom cloze columns before using the for loop

        # Create a central widget and set the layout on it
        central_widget = QWidget(self)  # Create a central widget
        central_widget.setLayout(layout)  # Set the layout on the central widget

        self.setCentralWidget(central_widget)  # Set the central widget of the main window

        # Export button
        self.export_button = QPushButton('Export Data', self)
        self.export_button.clicked.connect(self.export_data)
        layout.addWidget(self.export_button)

        # Shortcuts
        self.shortcut_incremental_cloze = QShortcut(QKeySequence('Ctrl+Shift+C'), self)
        self.shortcut_incremental_cloze.activated.connect(self.apply_incremental_cloze)

        self.shortcut_same_number_cloze = QShortcut(QKeySequence('Ctrl+Shift+Alt+C'), self)
        self.shortcut_same_number_cloze.activated.connect(self.apply_same_number_cloze)

        self.shortcut_bold = QShortcut(QKeySequence('Ctrl+B'), self)
        self.shortcut_bold.activated.connect(self.apply_bold)

        self.shortcut_underline = QShortcut(QKeySequence('Ctrl+U'), self)
        self.shortcut_underline.activated.connect(self.apply_underline)

        # Add buttons for adding and removing columns
        self.add_column_button = QPushButton('Add Column', self)
        self.add_column_button.clicked.connect(self.add_column)
        layout.addWidget(self.add_column_button)

        self.remove_column_button = QPushButton('Remove Column', self)
        self.remove_column_button.clicked.connect(self.remove_column)
        layout.addWidget(self.remove_column_button)

    def update_row_height_cc(self, row):
        column_index = self.table.columnCount() - 1
        text_edit_widget = self.table.cellWidget(row, column_index)
        # Calculate the height and add some margin
        height = text_edit_widget.document().size().height() + 10
        # Round the height to the nearest int
        rounded_height = int(round(height))
        self.table.setRowHeight(row, rounded_height)

    # def update_row_height_be(self, row):
    #     text_edit_widget = self.table.cellWidget(row, 4)
    #     # Calculate the height and add some margin
    #     height = text_edit_widget.document().size().height() + 10
    #     # Round the height to the nearest int
    #     rounded_height = int(round(height))
    #     self.table.setRowHeight(row, rounded_height)

    def apply_bold(self):
        # Get selected cell position
        current_row = self.table.currentRow()
        column_index = self.table.columnCount() - 1

        # Get the QTextEdit widget in the specified cell
        text_edit_widget = self.table.cellWidget(current_row, column_index)

        if isinstance(text_edit_widget, QTextEdit):
            cursor = text_edit_widget.textCursor()
            if cursor.hasSelection():
                selected_text = cursor.selectedText()
                bold_text = f'<b>{selected_text}</b>' # V: Bold
                cursor.insertText(bold_text)

    def apply_underline(self):
        # Get selected cell position
        current_row = self.table.currentRow()
        column_index = self.table.columnCount() - 1

        # Get the QTextEdit widget in the specified cell
        text_edit_widget = self.table.cellWidget(current_row, column_index)

        if isinstance(text_edit_widget, QTextEdit):
            cursor = text_edit_widget.textCursor()
            if cursor.hasSelection():
                selected_text = cursor.selectedText()
                underline_text = f'<u>{selected_text}</u>' # V: Bold
                cursor.insertText(underline_text)

    def apply_incremental_cloze(self):
        # Get the current selected row and column
        current_row = self.table.currentRow()
        column_index = self.table.columnCount() - 1  # Assuming cloze column is always column index 2
        
        # Get the QTextEdit widget in the specified cell
        text_edit_widget = self.table.cellWidget(current_row, column_index)
        
        if isinstance(text_edit_widget, QTextEdit):
            cursor = text_edit_widget.textCursor()
            if cursor.hasSelection():
                selected_text = cursor.selectedText()

                # Check if the cell already has a cloze counter
                cell_key = (current_row, column_index)
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
        column_index = self.table.columnCount() - 1 # Assuming cloze column is always column index 2
        
        # Get the QTextEdit widget in the specified cell
        text_edit_widget = self.table.cellWidget(current_row, column_index)
        
        if isinstance(text_edit_widget, QTextEdit):
            cursor = text_edit_widget.textCursor()
            if cursor.hasSelection():
                cell_key = (current_row, column_index)
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
                    column_index = self.table.columnCount() - 1
                    if column_index:  # V: Custom columns should be stripped
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

    def add_column(self):
        # Prompt the user for the type of column to add
        column_type, ok = QInputDialog.getItem(self, "Select Column Type", "Column Type:", ["Regular", "CustomTextEdit"], 0, False)
        if ok and column_type:
            column_count = self.table.columnCount()
            self.table.insertColumn(column_count)
            header_name = f"Column {column_count + 1}"
            self.table.setHorizontalHeaderItem(column_count, QTableWidgetItem(header_name))
            
            if column_type == "CustomTextEdit":
                # Add CustomTextEdit widgets to the new column #V: Originally from the for loop to make Cloze Column
                for row in range(self.table.rowCount()):
                    text_edit_widget = CustomTextEdit(self)
                    text_edit_widget.textChanged.connect(lambda row=row: self.update_row_height_cc(row)) # Update the row height
                    text_edit_widget.textChanged.connect(lambda row=row: self.cloze_text_changed(row)) # Check changes
                    self.table.setCellWidget(row, column_count, text_edit_widget)
                    # QTextEdit Read-Only
                    text_edit_widget.setReadOnly(True)

    def remove_column(self):
        current_column = self.table.currentColumn()
        if current_column != -1:  # Check if a column is selected
            reply = QMessageBox.question(self, 'Remove Column', 'Are you sure you want to remove this column?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.table.removeColumn(current_column)



def main():
    app = QApplication(sys.argv)

    # Splash Screen
    splash_pix = QPixmap('ankicardcreator-splash.png')
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.show()
    app.processEvents()

    # Main window initialization
    main_window = CardTable()

    # V: Stylesheet
    file = QFile(":/dark/stylesheet.qss")
    file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(file)
    app.setStyleSheet(stream.readAll())

    splash.finish(main_window)
    main_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()