# -*- coding: utf-8 -*-

"""This is the entry point of the program."""
def detect_language(text, languages):
    """Returns the detected language of given text."""
    # implement your solution here
    lang_sums = {}
    for language in languages
        lang_sums[sum([text.count(" %s " %x) for x in language['common_words']])] = language['name']
    return lang_sums[max(lang_sums.keys())]
    #return lang_sums
