from pathlib import Path

path = Path('guest.txt') 
guest = input("Whats your name?")
path.write_text(guest)
