def word_count(text):
    word_count = 0
    text_string = text.split()
    for i in range(len(text_string)):
        word_count += 1
    return word_count

def character_count(text):
    text_string = text.split()
    text_list = list(text_string)
    
    character_count = {}

    for i in text_list:     
        text_list = list(i)
        for i in text_list:     
            i = str.lower(i)        
            if i in character_count:
                character_count[i] += 1
            else:
                character_count[i] = 1
    return character_count
        
def sort_on(number_characters):
    character_list =[]

    for char in number_characters:
        character_list.append({"character": char, "count": number_characters[char]})
    
    def sort(dict):
        return dict["count"]
    
    character_list.sort(reverse=True, key=sort)
    return character_list
    
