import re

from gender_dict import gender_switch_dict


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


gender_converter = text_transformer(complete_switch_dict(gender_switch_dict))
