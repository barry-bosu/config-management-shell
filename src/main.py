import tkinter as tk
import os
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Graphical Shell Emulator - Variant 2"
    )

    parser.add_argument(
        "--vfs",
        required=True,
        help="Physical path to the virtual file system (VFS) directory"
    )

    parser.add_argument(
        "--script",
        required=True,
        help="Path to the startup script"
    )

    return parser.parse_args()


def validate_configuration(vfs_path, script_path):
    if not os.path.isdir(vfs_path):
        raise ValueError(
            f"VFS directory does not exist: {vfs_path}"
        )

    if not os.path.isfile(script_path):
        raise ValueError(
            f"Startup script does not exist: {script_path}"
        )


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
            f"\nComando: ls\nArgumentos: {arguments}"
        )

    elif command == "cd":
        terminal.insert(
            "end",
            f"\nComando: cd\nArgumentos: {arguments}"
        )

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

    process_command(command_line)

    if root.winfo_exists():
        terminal.insert("end", "\n> ")
        terminal.see("end")

    return "break"


def run_startup_script(script_path):
    with open(script_path, "r", encoding="utf-8") as script:
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


def create_interface(vfs_path, script_path):
    global root, terminal

    vfs_name = os.path.basename(vfs_path)

    root = tk.Tk()
    root.title(f"Graphical Shell Emulator - VFS: {vfs_name}")
    root.geometry("800x500")

    terminal = tk.Text(
        root, bg="black", fg="white",
        insertbackground="white", font=("Courier", 12)
    )

    terminal.pack(
        fill="both", expand=True,
        padx=10, pady=10
    )

    terminal.bind("<Return>", execute_command)
    terminal.focus_set()

    terminal.insert(
        "end",
        f"[DEBUG] VFS path: {vfs_path}\n"
        f"[DEBUG] Startup script: {script_path}\n\n"
    )

    root.after(
        100,
        lambda: run_startup_script(script_path)
    )

    root.mainloop()


def main():
    args = parse_arguments()

    vfs_path = os.path.abspath(args.vfs)
    script_path = os.path.abspath(args.script)

    validate_configuration(
        vfs_path,
        script_path
    )

    create_interface(
        vfs_path,
        script_path
    )


if __name__ == "__main__":
    main()