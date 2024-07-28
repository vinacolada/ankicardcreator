from ACCImport import *

class CustomTableWidget(QTableWidget):
    def keyPressEvent(self, event):
        current_row = self.currentRow()
        current_column = self.currentColumn()

        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            if current_column == 2 or current_column == 4:  # Index of Cloze column and Back Exta
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