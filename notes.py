import json
import os

FILE_NAME = 'notes.json'

def load_notes():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, 'r', encoding='utf-8') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error reading the file. The file is not formatted correctly.")
            return []
    return []

def save_notes(notes):
    try:
        with open(FILE_NAME, 'w', encoding='utf-8') as file:
            json.dump(notes, file, ensure_ascii=False)
    except Exception as e:
        print(f"Error saving notes: {e}")

notes = load_notes()

def display_notes():
    if not notes:
        print("There are no notes.")
    else:
        print("Your notes:")
        for i, note in enumerate(notes, 1):
            print(f"{i}: {note}")

def add_note():
    note = input("Enter your new note: ")
    if note.strip():  
        notes.append(note)
        save_notes(notes)  
        print("Note added successfully!")
    else:
        print("Note cannot be empty.")

def delete_note():
    display_notes()
    try:
        note_index = int(input("Enter the number of the note you want to delete: ")) - 1
        if 0 <= note_index < len(notes):
            removed_note = notes.pop(note_index)
            save_notes(notes)  
            print(f"Note '{removed_note}' deleted successfully!")
        else:
            print("The number entered is invalid.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\nMain page of the note-taking app:")
        print("1. Display notes")
        print("2. Add note")
        print("3. Delete note")
        print("4. Exit")
        
        choice = input("Please enter your choice: ")
        
        if choice == '1':
            display_notes()
        elif choice == '2':
            add_note()
        elif choice == '3':
            delete_note()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
