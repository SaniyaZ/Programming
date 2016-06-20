from codecs import open as cdopen
import os
os.chdir('/Users/ilyamelnikov/Dropbox/Work/Freelance/06.18_Sania/amhar')
file_name = 'test.txt'  # insert input file name here
lines = []
transl_file = cdopen('amhar_alph.txt', 'r', 'utf-8')
for sec in transl_file:
    lines.append(sec.strip('\r\n'))

vowels = lines[0].split('\t')
alph = {}
for l in lines[1:]:
    new = l.split('\t')
    alph[new[1]] = vowels[1] + new[0]
    alph[new[2]] = vowels[2] + new[0]
    alph[new[3]] = vowels[3] + new[0]
    alph[new[4]] = vowels[4] + new[0]
    alph[new[5]] = vowels[5] + new[0]
    alph[new[6]] = vowels[6] + new[0]
    alph[new[7]] = vowels[7] + new[0]


def amhar_translit(filename):
    text = cdopen(filename, 'r', 'utf-8')
    out_name = filename[:-4]+'_out.txt'
    output = cdopen(out_name, 'w', 'utf-8')
    for line in text:
        for letter in line:
            if letter in alph:
                line = line.replace(letter, alph[letter])
        output.write(line)
    output.close()

amhar_translit(file_name)