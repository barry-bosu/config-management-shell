import tkinter as tk
import os

VFS_NAME = "test_vfs"

os.environ.setdefault("HOME", os.path.expanduser("~"))

def expand_enviroment_variables(text):
    return os.path.expandvars(text)

def process_command(command, arguments):
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
        return False

    else:
        terminal.insert(
            "end",
            f"\nError: comando desconocido: {command}"
        )

    return True

def execute_command(event):
    command_line = terminal.get(
        "insert linestart",
        "insert lineend"
    ).strip()

    if command_line.startswith(">"):
        command_line = command_line[1:].strip()

    command_line = expand_enviroment_variables(command_line)
    parts = command_line.split()

    if not parts:
        terminal.insert("end", "\n>")
        return "break"

    command = parts[0]
    arguments = parts[1:]

    if not process_command(command, arguments):
        return "break"

    terminal.insert("end", "\n>")
    terminal.see("end")

    return "break"

def main():
    global root, terminal

    root = tk.Tk()
    root.title(f"Sell Emulator - VFS: {VFS_NAME}")
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

    terminal.insert("end", ">")
    terminal.bind("<Return>", execute_command)
    terminal.focus_set()

    root.mainloop()

if __name__ == "__main__":
    main()
