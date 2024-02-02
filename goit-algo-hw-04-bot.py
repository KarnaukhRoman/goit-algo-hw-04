

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return "Contact already exists"
    else:
        contacts[name] = phone
        return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact successfully changed"
    else:
        return "Contact not found"

def show_phone(name, contacts):
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found"

def show_all(contacts):
    all_contacts = ''
    for name, phone in contacts.items():
        all_contacts+=name+' '+phone+'\n'
    return all_contacts

def main():
    print("Welcome to the assistant bot!")
    contacts = {}

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ['close','exit']:
            print('Good by!')
            break

        elif command == 'hello':
            print('How can I help you?')

        elif command == 'add':
            print(add_contact(args, contacts))
        
        elif command == 'change':
            print(change_contact(args, contacts))
        
        elif command == 'phone':
            if contacts:
                print(show_phone(args[0], contacts))
            else:
                print('Contacts is empty')

        elif command == 'all':
            if contacts:
                print(show_all(contacts))
            else:
                print('Contacts is empty')
        else:
            print('Invalid command.')


if __name__=="__main__":
    main()
