def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter the argument for the command"
        except Exception:
            return "Something went wrong."

    return inner


def parse_input(user_input: str) -> tuple[str, list[str]]:
    parts = user_input.strip().split()
    if not parts:
        return "", []
    cmd = parts[0].lower()
    args = parts[1:]
    return cmd, args


@input_error
def add_contact(args: list[str], contacts: dict) -> str:
    name, phone = args[0], args[1]
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args: list[str], contacts: dict) -> str:
    name, phone = args[0], args[1]
    if name not in contacts:
        raise KeyError()
    contacts[name] = phone
    return "Contact updated."


@input_error
def show_phone(args: list[str], contacts: dict) -> str:
    name = args[0]
    return contacts[name]


@input_error
def show_all(args: list[str], contacts: dict) -> str:
    if not contacts:
        return "No contacts saved."
    lines = [f"{name}: {phone}" for name, phone in contacts.items()]
    return "\n".join(lines)


def main() -> None:
    contacts = {}
    handlers = {
        "hello": lambda a, c: "How can I help you?",
        "add": add_contact,
        "change": change_contact,
        "phone": show_phone,
        "all": show_all,
    }

    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ("close", "exit"):
            print("Good bye!")
            break

        if command in handlers:
            print(handlers[command](args, contacts))
        elif command:
            print("Invalid command.")


if __name__ == "__main__":
    main()
