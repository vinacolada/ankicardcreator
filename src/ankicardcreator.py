import sys
from PyQt5.QtWidgets import QHeaderView, QWidget, QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout, QPushButton, QShortcut, QFileDialog, QMessageBox
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import Qt

class CustomTextEdit(QTextEdit):
    def focusOutEvent(self, event):
        super().focusOutEvent(event)
        self.setReadOnly(True) # Make the QTextEdit read-only when it loses focus

    def keyPressEvent(self, event):
        if self.isReadOnly():
            if event.key() in (Qt.Key_Up, Qt.Key_Down, Qt.Key_Left, Qt.Key_Right):
                # Pass the event to the parent (table) only if read-only
                self.clearFocus()  # Remove focus from QTextEdit
                self.parent().keyPressEvent(event)
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
        # Handle the Enter key for editing mode separately
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            current_row = self.currentRow()
            current_column = self.currentColumn()
            if current_column == 2: # Index of Cloze column
                text_edit_widget = self.cellWidget(current_row, current_column)
                if isinstance(text_edit_widget, CustomTextEdit):
                    text_edit_widget.setReadOnly(False) # Make the QTextEdit editable
                    text_edit_widget.setFocus() # Set focus to the QTextEdit
        else:
            current_row = self.currentRow()
            current_column = self.currentColumn()

            if event.key() == Qt.Key_Up and current_row > 0:
                self.setCurrentCell(current_row - 1, current_column)
            elif event.key() == Qt.Key_Down and current_row < self.rowCount() - 1:
                self.setCurrentCell(current_row + 1, current_column)
            elif event.key() == Qt.Key_Left and current_column > 0:
                self.setCurrentCell(current_row, current_column - 1)
            elif event.key() == Qt.Key_Right and current_column < self.columnCount() - 1:
                self.setCurrentCell(current_row, current_column + 1)
            else:
                super().keyPressEvent(event)

# Main GUI
class ClozeTable(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.cloze_counters = {} # Dictionary to keep track of cloze counters

    def initUI(self):
        self.setWindowTitle('Anki Cloze Creator')
        self.setGeometry(100, 100, 800, 600)

        # Create table
        self.table = CustomTableWidget(self)
        self.table.setRowCount(500)  # Set this to the number of rows you want
        self.table.setColumnCount(6)  # We have 6 columns
        
        # Adjust rows widths to fit content
        self.table.resizeRowsToContents()

        # Allow users to resize columns manually
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        # Set up the table headers
        headers = ['Number', 'Title', 'Cloze Column', 'Topic', 'Back Extra', 'Back Image']
        self.table.setHorizontalHeaderLabels(headers)

        # Add a QTextEdit widget for the cloze column
        for row in range(self.table.rowCount()):
            text_edit_widget = CustomTextEdit(self)
            text_edit_widget.textChanged.connect(lambda row=row: self.update_row_height(row))
            self.table.setCellWidget(row, 2, text_edit_widget)
            # QTextEdit Read-Only
            text_edit_widget.setReadOnly(True)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.table)

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

    def update_row_height(self, row):
        text_edit_widget = self.table.cellWidget(row, 2)
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
                    cloze_text = f'{{{{c{cloze_counter - 1}::{selected_text}}}}}'
                    cursor.insertText(cloze_text)

    def export_data(self):
    # Open a file dialog to specify the path and file name for export
        path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt)")
        if not path:  # If no path is provided, return without doing anything
            return

        with open(path, 'w', encoding='utf-8') as file:
            for row in range(self.table.rowCount()):
                row_data = []
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
                # Write the tab-delimited row to the file
                file.write('\t'.join(row_data) + '\n')

    # Show a message box that the data was exported successfully
        QMessageBox.information(self, "Export Successful", f"Data exported to '{path}'")



def main():
    app = QApplication(sys.argv)
    main_window = ClozeTable()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()