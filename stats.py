def word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    character_dict = {}
    for character in text:
        character = character.lower()
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    return character_dict


def sort_on(items):
    return items["num"]

def print_result_dict(dict):
    list_of_dict = []
    for k, v in dict.items():
        if k.isalpha():
            list_of_dict.append({"char": k, "num": v})
        else: 
            continue
    list_of_dict.sort(reverse=True, key = sort_on)
    return list_of_dict
