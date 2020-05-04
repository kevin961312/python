import sys
from notebook import Notebook, Note
print(__name__)
class Menu:
    '''Display a menu and respond to choices when run.'''
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
                        '1': self.show_notes,
                        '2': self.search_notes,
                        '3': self.add_notes,
                        '4': self.modify_notes,
                        '5': self.quit,
                       }

    def diplay_menu(self):
        print("""
        Notebook Menu

        1. Show all Notes
        2. Search Notes
        3. Add Notes 
        4. Modify Notes
        5. Quit

        """)

    def run(self):
        '''Display the menu and respond to choices.'''
        while True:
            self.diplay_menu()
            choice = input("\n\tEnter Option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("\n\t{0} is not a valid choice.".format(choice))

    def show_notes(self, note = None):
        if not note:
            notes = self.notebook.notes
        for note in notes:
            print("{0}: {1}\n {2}".format(note.id, note.tags, note.memo))

    def search_notes(self):
        filter = input("\n\tSearch for: \n\t")
        notes = self.notebook.search(filter)
        self.show_notes(notes)

    def add_notes(self):
        memo = input("\n\tEnter a memo: \n\t")
        self.notebook.new_note(memo)
        print("Your note has been added")

    def modify_notes(self):
        id = input("\n\tEnter a note id: ")
        memo = input("\n\tEnter a memo: \n\t")
        tags = input("\n\tEnter tags: \n\t")
        if memo:
            self.notebook.modify_memo(id, memo)
        elif tags:
            self.notebook.modify_tags(id,tags)
    
    def quit(self):
        print("\n\tThank you for using your notebook today.")
        sys.exit(0)


if __name__== "__main__":
    Menu().run()