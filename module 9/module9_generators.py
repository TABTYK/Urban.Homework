def all_variants(text):
    def generate(current,index):
        if index == len(text):
            yield current
            return
        yield from generate(current,index + 1) # пропустить теущий символ
        yield from generate(current + text[index], index +1) # взять текущий символ

    yield from generate('',0)

a = all_variants("abc")
for i in a:
    print(i)