import sys
from cx_Freeze import setup, Executable

# Dependências
build_exe_options = {
    "packages": ["tkinter", "pytube", "PIL", "requests", "io", "customtkinter"],
    "include_files": [("C:\\Users\\HP\\Desktop\\projectos\\programas\\ferramenta V4 Update\\icon1.ico")],  # Inclua o ícone na pasta do executável
}

# Script principal
base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Use Win32GUI para criar um aplicativo sem console no Windows

executables = [
    Executable("main7.py", base=base, icon="C:\\Users\\HP\\Desktop\\projectos\\programas\\ferramenta V4 Update\\icon1.ico"),
]

setup(
    name="YoutubeDownloader",
    version="1.0",
    description="Youtube Downloader",
    options={"build_exe": build_exe_options},
    executables=executables,
)
