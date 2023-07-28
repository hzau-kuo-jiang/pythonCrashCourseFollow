name1 = 'eric'
print(f'Hello {name1.title()}, would you like to learn some Python today?')
print(f'Hello {name1.upper()}, would you like to learn some Python today?')
print(f'Hello {name1.lower()}, would you like to learn some Python today?')
famous_person = 'Albert Einstein'
message = 'A person who never made a mistake never tried anything new.'
print(f'{famous_person} once said, "{message}"')
name2 = '\tEric Matthes\n'
print(f'Unmodified: {name2}')
print(f'Using lstrip(): {name2.lstrip()}')
print(f'Using rstrip(): {name2.rstrip()}')
print(f'Using strip(): {name2.strip()}')
file_name = 'learning_python.txt'
print(f'File name without extension: {file_name.split(".")[0]}')
print(f'File name without extension: {file_name.removesuffix(".txt")}')
