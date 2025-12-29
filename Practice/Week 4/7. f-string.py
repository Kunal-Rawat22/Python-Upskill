# Padding {variable:xy} x-> value to inserted, y -> digits to for padding

for n in range(1,11):
    print(f'{n:02}')

# Precision
pi = 323.12356567876
sentence = f'PI is equal to {pi:.4f}'
print(sentence)

# Date Time formatting
from datetime import datetime

birthday = datetime(1990, 1, 1)
sentence = f"Your birthday is on {birthday: %B %d, %Y}"
print(sentence)