import tkinter as tk
import os

VFS_NAME = "test_vfs"

os.environ.setdefault("HOME", os.path.expanduser("~"))

def expand_enviroment_variables(text):
    return os.path.expandvars(text)

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

    if command == "ls":
        terminal.insert("end", "\n[ls] Comando provisional ejecutado")

    elif command == "cd":
        if arguments:
            terminal.insert(
                "end",
                 f"\n[cd] Directorio recibido: {arguments[0]}"
                 )
        else:
            terminal.insert(
                "end", 
                "\n[cd] Error: cd necesita un directorio")

    elif command == "exit":
        root.destroy()
        return "break"

    else:
        terminal.insert(
            "end", 
            f"\nError: Comando desconocido '{command}'"
        )

    terminal.insert("end", "\n>")
    terminal.see("end")

    return "break"

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
