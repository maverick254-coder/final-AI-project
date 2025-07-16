[Setup]
AppName=Homework Helper
AppVersion=1.0
DefaultDirName={autopf}\Homework Helper
DefaultGroupName=Homework Helper
OutputDir=.
OutputBaseFilename=HomeworkHelperInstaller
Compression=lzma
SolidCompression=yes

[Files]
Source: "HomeworkHelper.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "install.bat"; DestDir: "{app}"
Source: "OllamaSetup.exe"; DestDir: "{app}"
Source: "README.txt"; DestDir: "{app}"
Source: "app.py"; DestDir: "{app}"
Source: "model_utils.py"; DestDir: "{app}"
Source: "launcher.py"; DestDir: "{app}"
Source: "requirements.txt"; DestDir: "{app}"

[Icons]
Name: "{group}\Homework Helper"; Filename: "{app}\HomeworkHelper.exe"
Name: "{commondesktop}\Homework Helper"; Filename: "{app}\HomeworkHelper.exe"

[Run]
Filename: "{app}\install.bat"; Description: "Run setup to install dependencies"; Flags: shellexec postinstall
