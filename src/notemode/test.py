note_titles = []

def create_blank_note():
    title = input("Type in title: ")
    
    if title != "show":
        note_titles.append(title)
        print(f"Note created with title: {title}")
        create_blank_note()
    elif title == "show":
        print("All note titles:")
        for note_title in note_titles:
            print(note_title)
# Call the function to start the process
create_blank_note()