from nltk.tokenize import sent_tokenize

def lines(a, b):
    """Return lines in both a and b"""

    a_lines = []
    a_lines = a.split('\n')

    b_lines = []
    b_lines = b.split('\n')

    i_lines = []

    for index, a_line in enumerate(a_lines):
        for b_line in b_lines:
            if a_line == b_line:
                duplicate = 0
                for i_line in i_lines:
                    if a_line == i_line:
                        duplicate = 1
                if duplicate == 0:
                    i_lines.append(a_line)

    return i_lines


def sentences(a, b):
    """Return sentences in both a and b"""
    a_sents = sent_tokenize(a)
    b_sents = sent_tokenize(b)

    i_sents = []

    for a_sent in a_sents:
        for b_sent in b_sents:
            if a_sent == b_sent:
                duplicate = 0
                for i_sent in i_sents:
                    if a_sent == i_sent:
                        duplicate = 1
                if duplicate == 0:
                    i_sents.append(a_sent)
    return i_sents


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    a_subs = []
    b_subs = []
    i_subs = []

    a_subs = substring(a, n)
    b_subs = substring(b, n)

    for a_sub in a_subs:
        for b_sub in b_subs:
            if a_sub == b_sub:
                duplicate = 0
                for i_sub in i_subs:
                    if a_sub == i_sub:
                        duplicate = 1
                if duplicate == 0:
                    i_subs.append(a_sub)

    return i_subs

def substring(a, n):

    substrings = []

    for i in range(len(a)):

        # slices a into length n substrings and buffers them
        if (i <= len(a)-n):
            substrings.append(a[i:n + i])

    return substrings
