import string  # for punctuation
import re      # for regular expressions


class Text:
    def __init__(self, text):
        self.text = text

    
    def word_frequency(self, word):
        words = self.text.lower().split()
        count = words.count(word.lower())
        if count == 0:
            return f"The word '{word}' was not found."
        return count

    
    def most_common_word(self):
        words = self.text.lower().split()
        freq = {}
        for word in words:
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1
        most_common = max(freq, key=freq.get)
        return most_common

    
    def unique_words(self):
        words = self.text.lower().split()
        unique = set(words)
        return list(unique)

    
    @classmethod
    def from_file(cls, file_path):
        with open(file_path, 'r') as file:
            content = file.read()
        return cls(content)


class TextModification(Text):
    
    
    def remove_punctuation(self):
        translator = str.maketrans('', '', string.punctuation)
        no_punct = self.text.translate(translator)
        return no_punct

    
    def remove_stop_words(self):
        
        stop_words = {"a", "an", "the", "is", "are", "and", "or", "in", "on", "of", "to", "with", "for", "that", "this"}
        words = self.text.lower().split()
        filtered = [word for word in words if word not in stop_words]
        return ' '.join(filtered)

    
    def remove_special_characters(self):
        
        cleaned = re.sub(r'[^A-Za-z0-9\s]', '', self.text)
        return cleaned



sample_text = "This is a simple test. This test is only a test!"
text_obj = Text(sample_text)

print("Word Frequency ('test'):", text_obj.word_frequency('test'))
print("Most Common Word:", text_obj.most_common_word())
print("Unique Words:", text_obj.unique_words())


mod_obj = TextModification(sample_text)
print("No Punctuation:", mod_obj.remove_punctuation())
print("No Stop Words:", mod_obj.remove_stop_words())
print("No Special Characters:", mod_obj.remove_special_characters())