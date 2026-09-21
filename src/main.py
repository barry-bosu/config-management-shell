import tkinter as tk
import os
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Graphical Shell Emulator -Variant 2"
        )
    
    parser.add_argument(
        "--vfs", 
        required=True, 
        help="Phisical path to the virtual file system (VFS) directory"
    )

    parser.add_argument(
        "--script",
        required=True,
        help="Path to the startup script"
    )

    return parser.parse_args()

args = parse_arguments()
VFS_PATH = os.path.abspath(args.vfs)
SCRIPT_PATH = os.path.abspath(args.script)
VFS_NAME = os.path.basename(VFS_PATH)

def validate_configuration():
    if not os.path.isdir(VFS_PATH):
        raise ValueError(
            f"VFS directory does not exist: {VFS_PATH}")

    if not os.path.isfile(SCRIPT_PATH):
        raise ValueError(
            f"Startup script does not exist: {SCRIPT_PATH}")

validate_configuration()

os.environ.setdefault("HOME", os.path.expanduser("~"))

def expand_environment_variables(text):
    return os.path.expandvars(text)

def process_command(command_line):
    command_line = expand_environment_variables(command_line)

    parts = command_line.split()

    if not parts:
        return True

    command = parts[0]
    arguments = parts[1:]

    if command == "ls":
        terminal.insert(
            "end",
            "\n[ls] Comando provisional ejecutado."
        )

    elif command == "cd":
        if arguments:
            terminal.insert(
                "end",
                f"\n[cd] Directorio recibido: {arguments[0]}"
            )
        else:
            terminal.insert(
                "end",
                "\nError: cd necesita un directorio."
            )
            return False

    elif command == "exit":
        root.destroy()
        return True

    else:
        terminal.insert(
            "end",
            f"\nError: comando desconocido: {command}"
        )
        return False

    return True


def execute_command(event):
    command_line = terminal.get(
        "insert linestart",
        "insert lineend"
    ).strip()

    if command_line.startswith(">"):
        command_line = command_line[1:].strip()

    success = process_command(command_line)

    if root.winfo_exists():
        terminal.insert("end", "\n> ")
        terminal.see("end")

    return "break"

def run_startup_script():
    with open(SCRIPT_PATH, "r", encoding="utf-8") as script:
        for line in script:
            command_line = line.strip()

            if not command_line:
                continue

            terminal.insert("end", f"> {command_line}")

            success = process_command(command_line)

            terminal.insert("end", "\n")

            if not success:
                terminal.insert(
                    "end",
                    "Startup script stopped because of an error.\n"
                )
                break

    terminal.insert("end", "> ")
    terminal.see("end")


root = tk.Tk()
root.title(f"Graphical Shell Emulator - VFS: {VFS_NAME}")

root.geometry("800x500")

terminal = tk.Text(
    root, 
    bg="black", 
    fg="white", 
    insertbackground="white",
    font=("Courier", 12)
)
terminal.pack(
    fill="both", 
    expand=True,
    padx=10,
    pady=10
    )

terminal.bind("<Return>", execute_command)
terminal.focus_set()
root.after(100, run_startup_script)

root.mainloop()
