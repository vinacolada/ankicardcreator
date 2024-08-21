import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

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