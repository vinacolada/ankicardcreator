from ACCImport import *

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