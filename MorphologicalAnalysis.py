from janome.tokenizer import Tokenizer

def judgement(s):
    if s == 'たす' or s == '足す' or s == '+':
        return '+'
    elif s == 'ひく' or s == '引く' or s == '-':
        return '-'
    elif s == 'かける' or s == '掛ける' or s == '×':
        return '*'
    elif s == 'わる' or s == '割る' or s == '÷':
        return '/'
    else:
        return 0

def changevoice(voice = 'Default'):
    after = ''
    t = Tokenizer()

    if voice == 'Default':
        return '認識できなかったよ'
    else:
        for token in t.tokenize(voice):
            print(token)
            pos = token.part_of_speech.split(',')[0]
            if token.part_of_speech.split(',')[1] == '数':
                after = after + token.surface
            elif pos == '動詞' or pos == '名詞' or pos == '記号':
                if judgement(token.surface) == 0:
                    pass
                else:
                    after = after + judgement(token.surface)
        if after == '':
            return '認識できなかったよ'
        else:
            return eval(after)
