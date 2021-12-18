def sentence_parse(sentence):
    parsed_sentence = sentence.split()
    return parsed_sentence


sentence = input()
parsed_sentence = sentence_parse(sentence)

for word in parsed_sentence:
    print(word)
