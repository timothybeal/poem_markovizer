
import markovbot
from random import choice
import itertools

def poem_markovize():
    markovizer = markovbot.Markovizer("Dickinson_Poems.txt")
    line_start = choice(["I", "You", "And", "Then", "If", "Oh", "We", "But", "Our", "He", "How", "Who", "When"])
    line = markovizer.create_utterance(line_start, char_limit=50)
    print(line[:-1])

for num_lines in itertools.repeat(None, 4):
    poem_markovize()


