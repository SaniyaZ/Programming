f = open('ამერიკის.txt', 'r', encoding = 'utf-8')
text = f.read()
letters = {
'ა' : 'a',
'ბ' : 'b',
'გ' : 'g',
'დ': 'd',
'ე': 'ɛ',
'ვ': 'v',
'ზ': 'z',
'თ': 'tʰ',
'ი': 'ɪ',
'კ': 'k\'',
'ლ': 'l',
'მ' : 'm',
'ნ' : 'n',
'ო': 'ɔ',
'პ': 'p\'',
'ჟ': 'ʒ',
'რ': 'r',
'ს': 's',
'ტ': 't\'',
'ჳ': 'wi',
'უ': 'u',
'ფ': 'pʰ',
'ქ': 'kʰ',
'ღ': 'ʁ',
'ყ': 'q\'',
'შ': 'ʃ',
'ჩ': 'tʃ',
'ც': 'ts',
'ძ': 'dz',
'წ': 'ts\ʼ',
'ჭ': 'tʃ\ʼ',
'ხ': 'χ',
'ჴ': 'q',
'ჯ': 'dʒ',
'ჰ': 'h',
}
for b in letters:
    text = text.replace(b, letters[b])
f.close()
f = open('Transliteration.txt', 'w', encoding = 'utf-8')
f.write(text)
f.close()
