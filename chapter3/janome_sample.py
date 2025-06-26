from janome.tokenizer import Tokenizer


t = Tokenizer()
for token in t.tokenize("吾輩は猫である。"):
    print(token)
