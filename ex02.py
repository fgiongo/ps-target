inputstr = input("> ").upper()
count = inputstr.count("A")
count += inputstr.count("Ã")
count += inputstr.count("À")
count += inputstr.count("Á")
if count == 0:
    print("A string não contém a letra 'a'")
else:
    print(f"A string contém {count} letras 'a'")
