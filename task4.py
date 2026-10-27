import re
from functools import wraps

PHONE_PATTERN = re.compile(r'^\d+$')

def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, IndexError, KeyError) as e:
            return str(e)

    return inner

@input_error
def parse_input(user_input: str) -> tuple[str, list[str]]:
    parts = user_input.strip().split()
    if len(parts) == 0:
        return '', []
    return parts[0].lower(), parts[1:]

@input_error
def add_contact(args: list[str], contacts: dict[str, str]) -> str:
    if len(args) != 2 or not PHONE_PATTERN.match(args[1]):
        raise ValueError('Invalid input format. Please use "add <name> <phone>".')
    name, phone = args
    if name in contacts:
        raise KeyError('Contact {name} already exists. Use "change <name> <phone>" to update the phone number.')
    contacts[name] = phone
    return f'Contact {name} with phone {phone} added successfully.'

@input_error
def change_contact(args: list[str], contacts: dict[str, str]) -> str:
    if len(args) != 2 or not PHONE_PATTERN.match(args[1]):
        raise ValueError('Invalid input format. Please use "change <name> <phone>".')
    name, phone = args
    if name not in contacts:
        raise KeyError(f'Contact {name} does not exist. Use "add <name> <phone>" to add a new contact.')
    contacts[name] = phone
    return f'Contact {name} with phone {phone} updated successfully.'

@input_error
def show_phone(args: list[str], contacts: dict[str, str]) -> str:
    if len(args) != 1:
        raise ValueError('Invalid input format. Please use "phone <name>".')
    name = args[0]
    if name not in contacts:
        raise KeyError(f'Contact {name} does not exist. Use "add <name> <phone>" to add a new contact.')
    return f'{name}: {contacts[name]}'

@input_error
def show_all(args: list[str], contacts: dict[str, str]) -> str:
    if args:
        raise ValueError('Invalid input format. Please use "all".')
    if not contacts:
        raise KeyError('No contacts found.')
    return '\n'.join(f'{name}: {phone}' for name, phone in contacts.items())


def hello(args: list[str], contacts: dict[str, str]) -> str:
    return 'How can I help you?'


HANDLERS = {
    'hello': hello,
    'add': add_contact,
    'change': change_contact,
    'phone': show_phone,
    'all': show_all,
}


def main() -> None:
    contacts: dict[str, str] = {}
    print('Welcome to the assistant bot!')
    while True:
        try:
            user_input = input('Enter a command: ')
        except SystemExit, KeyboardInterrupt, EOFError:
            print('\nGood bye!')
            break

        command, args = parse_input(user_input)
        if command in ('close', 'exit'):
            print('Good bye!')
            break
        if not command:
            continue
        handler = HANDLERS.get(command)
        if handler is None:
            print('Invalid command. Please try again.')
        else:
            print(handler(args, contacts))


if __name__ == "__main__":
    main()
