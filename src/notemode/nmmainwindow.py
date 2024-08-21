from nmui import *
from nmaccquestions import *

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.model = QtGui.QStandardItemModel(self.allNoteListView)
        self.allNoteListView.setModel(self.model)

        self.placeholder = "New Note"
        self.notes = []  # List to store note dictionaries
        self.next_note_id = 1  # ID for the next note to be created
        self.currently_editing_id = None  # ID of the note currently being edited

        # Load notes from file during initialization
        self.load_notes_from_file()

        # Initially create a blank note
        self.create_blank_note()

        # Install event filter to detect focus out event on QTextEdits
        self.titleTextEdit.installEventFilter(self)
        self.notesTextEdit.installEventFilter(self)
        self.topicTextEdit.installEventFilter(self)

        # Connect the selectionChanged signal to save the content when another note is selected
        self.allNoteListView.selectionModel().currentChanged.connect(self.on_note_selection_changed)
        # Connect the textChanged signal of the titleTextEdit to the update_note_title method
        self.titleTextEdit.textChanged.connect(self.update_note_title)

        # Modify the table setup in the first column of the splitter
        self.setupFirstColumn()

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.FocusOut and source in [self.titleTextEdit, self.notesTextEdit, self.topicTextEdit]:
            self.on_editing_finished()
        return super(MainWindow, self).eventFilter(source, event)

    def create_blank_note(self):
        # Create a new note dictionary with a unique ID and placeholder values
        note = {
            'id': self.next_note_id,
            'title': self.placeholder,
            'content': '',
            'topic': ''
        }
        self.notes.append(note)
        self.next_note_id += 1

        # Add a placeholder item to the QListWidget
        item = QtGui.QStandardItem(self.placeholder)
        self.model.appendRow(item)
        # Do not change the current selection or focus

    def on_editing_finished(self):
        # Find the note by ID
        note = next((note for note in self.notes if note['id'] == self.currently_editing_id), None)
        if note:
            # Get the new title and content from the text edits
            new_title = self.titleTextEdit.toPlainText().strip()
            new_content = self.notesTextEdit.toPlainText()
            new_topic = self.topicTextEdit.toPlainText()

            # Update the note's title, content, and topic
            note['title'] = new_title
            note['content'] = new_content
            note['topic'] = new_topic

            # Update the QListWidget with the new title
            current_index = self.allNoteListView.currentIndex()
            current_item = self.model.itemFromIndex(current_index)
            current_item.setText(new_title)

            # Save notes to file after editing is finished
            self.save_notes_to_file()

            # Reset the currently_editing_id as we've finished editing the note
            self.currently_editing_id = None

            # If there isn't a placeholder present, create a new blank note placeholder
            if not self.is_placeholder_present():
                self.create_blank_note()

    def is_placeholder_present(self):
        # Check if the last note in the list is a placeholder
        return self.notes and self.notes[-1]['title'] == self.placeholder

    def on_note_selection_changed(self, current, previous):
        if previous.isValid():
            # Save the previous note's content
            prev_note_id = self.notes[previous.row()]['id']
            self.save_note(prev_note_id)

        if current.isValid():
            # Load the selected note's content
            self.currently_editing_id = self.notes[current.row()]['id']
            self.load_note_content(self.currently_editing_id)

        # Save notes to file when the selection changes
        self.save_notes_to_file()

    def update_note_title(self):
        # Only update the title of an existing note (ignore placeholder)
        if self.currently_editing_id and self.currently_editing_id != 1:
            current_index = self.allNoteListView.currentIndex()
            if not current_index.isValid():
                return

            # Get the new title from the text edit
            new_title = self.titleTextEdit.toPlainText().strip()

            # Find the note by ID and update its title
            note = next((note for note in self.notes if note['id'] == self.currently_editing_id), None)
            if note:
                note['title'] = new_title

                # Update the QListWidget with the new title
                current_item = self.model.itemFromIndex(current_index)
                current_item.setText(new_title)

                # Save notes to file after title update
                self.save_notes_to_file()

    def save_note(self, note_id):
        note = next((note for note in self.notes if note['id'] == note_id), None)
        if note and note['title'] != self.placeholder:
            note['content'] = self.notesTextEdit.toPlainText()
            note['topic'] = self.topicTextEdit.toPlainText()

    def load_note_content(self, note_id):
        note = next((note for note in self.notes if note['id'] == note_id), None)
        if note:
            self.titleTextEdit.setText(note['title'])
            self.notesTextEdit.setText(note['content'])
            self.topicTextEdit.setText(note['topic'])

    def save_notes_to_file(self):
        # Prepare data for JSON serialization
        data = []
        for note in self.notes:
            if note['title'] != self.placeholder:  # Exclude placeholder notes
                data.append({
                    'id': note['id'],
                    'title': note['title'],
                    'content': note['content'],
                    'topic': note['topic']
                })

        # Write JSON data to file
        with open('notes.json', 'w') as file:
            json.dump(data, file, indent=4)

    def load_notes_from_file(self):
        try:
            with open('notes.json', 'r') as file:
                data = json.load(file)
            for note_data in data:
                note = {
                    'id': note_data['id'],
                    'title': note_data['title'],
                    'content': note_data['content'],
                    'topic': note_data['topic']
                }
                self.notes.append(note)
                self.model.appendRow(QtGui.QStandardItem(note['title']))
            self.next_note_id = max(note['id'] for note in self.notes) + 1
        except (FileNotFoundError, json.JSONDecodeError):
            pass  # File not found or JSON decode error, start with an empty notes list