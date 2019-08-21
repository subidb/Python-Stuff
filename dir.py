from pathlib import Path

# p1 = Path("ManualDir")
# p1.mkdir()

path = Path()
for file in path.glob('*'):
    print(file)