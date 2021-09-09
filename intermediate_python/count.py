import collections
import operator


def count_unique_words(filename):
    with open(filename, 'r') as f:
        content = f.read()
        words = content.split()
        lowercase_words = []
        for word in words:
            lowercase_words.append(word.lower())
        cnt = collections.Counter(lowercase_words)
        cnt = dict(sorted(cnt.items(), key=operator.itemgetter(1), reverse=True)[:10])
    return cnt


if __name__ == '__main__':
    top_lines = count_unique_words('hamlet.txt')
    for index, (key, value) in enumerate(top_lines.items()):
        print(f"{index +1}: '{key}' with {value} occurrences")