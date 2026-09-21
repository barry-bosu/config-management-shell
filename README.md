# Shell Emulator - Variant 2

Graphical shell emulator developed in Python using Tkinter.

## Stage 1

Implemented features:

- Graphical user interface (GUI).
- VFS name displayed in the window title.
- Basic REPL.
- Environment variable expansion, for example `$HOME`.
- Stub `ls` command.
- Stub `cd` command.
- `exit` command.
- Basic error handling for unknown commands.

## Run

On Windows:

```powershell
.\run.bat

## Examples

> ls
[ls] Comando provisional ejecutado.

> cd documentos
[cd] Directorio recibido: documentos

> cd $HOME
[cd] Directorio recibido: <HOME path>

> unknown
Error: comando desconocido: unknown

> exit
