def get_book(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    characters = {}
    for character in text:
        character = character.lower()

        if character in characters:
            characters[character] += 1
        else: 
            characters[character] = 1

    return characters

def sorted_characters(characters):
    chars_list = []
    for char, count in characters.items():
        chars_list.append({"char": char, "num": count})

    def sort_on(dict):
        return dict["num"]
    
    chars_list.sort(reverse = True , key = sort_on)
    
    return chars_list


    