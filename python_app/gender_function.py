import re

from gender_dict import gender_switch_dict

text=u''''This is of hers. She called her up and jumped. We were discussing something about firemen, and I said, “An advanced computer user knows what he needs…”, [when] a female colleague, suddenly interrupted, “Are you saying women cannot be advanced computer users?” I thought she was joking and laughed, but then realised I was the only one laughing, and she was looking at me as if I were her personal enemy'. '''

def reverse_dict(d):
    return {
        value : key
        for key, value in d.items()
    }


def capitalize_dict(d):
    return {
        key.capitalize() : value.capitalize()
        for key, value in d.items()
    }


def complete_switch_dict(d):
    rev = reverse_dict(d)
  
    return {
        **d,
        **rev,
        **capitalize_dict(d),
        **capitalize_dict(rev)
    }


def text_transformer(switch_dict):
    def possibly_replace(string):
        if string in switch_dict:
            return switch_dict[string]
        return string

    re_words = re.compile(rf"\b({'|'.join(switch_dict.keys())})\b")

    def transformer(text):
        return "".join(
            possibly_replace(part)
            for part in re_words.split(text)
        )
    
    return transformer


pre_gender_converter = text_transformer(complete_switch_dict(gender_switch_dict))

result = pre_gender_converter(text)

dict_pron = {' his ': ' her ', ' her ': ' his ',
              'His is': 'Her is', 'Her is': 'His is',
              'His was': 'His was', 'Her was': 'His was',
              'His ': 'Her ', 'Her ': 'His ', 
              ' him,': ' her,', ' her,': ' him,', 
              'Hers are': 'His are', 'His are': 'Hers are',
              'Hers were': 'His were', 'Hers are': 'His are',
              ' him out': ' her out', ' her out': ' him out', 
              ' him ': ' her ', 
              ' him.': ' her.', ' her.': ' him.',
              ' hers ': ' him ',
              ' hers.': ' his.', ' his.': ' hers.',
              ' her by': ' him by', ' him by': ' her by',
              ' her up': ' him up', ' him up': ' her up',
              ' her “that' : ' him “that', ' him “that' : ' her “that',
              ' her that' : ' him that', ' him that' : ' her that',
              ' her "that' : ' him "that', ' him "that' : ' her "that',
              ' him boy': ' her girl', ' her girl': ' him boy', 
              'takes her home': 'takes him home', 'take her home': 'take him home', 
              'takes him home': 'takes her home', 'take him home': 'take her home', 
              'from her.': 'from him.', 'From her.': 'From him.',
              'from him': 'from her', 'From him': 'From her',
              'known for her': 'known for his', 'known for his': 'known for her'
              }


#Function for determiner issue (her his, her him)
def pron_converter(string, substitutions):
    substrings = sorted(substitutions, key=len, reverse=True)
    regex = re.compile('|'.join(map(re.escape, substrings)))
    return regex.sub(lambda match: substitutions[match.group(0)], string) 

gender_converter = pron_converter(result, dict_pron)

print(gender_converter)
