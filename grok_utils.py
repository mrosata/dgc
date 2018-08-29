from pygrok import Grok


# Filters the lines of a file based on a passed in predicate
# by default the predicate checks that the line is not None
def filter_file_with_pred(file_path, pred=lambda a: a is not None):
    h = open(file_path, 'r')
    rv = []
    num = 0
    for ln in h:
        num += 1
        if pred([num, ln]):
            rv.append([num, ln])
    return rv


def skip_lines(n):
    def rv(line):
        num, ln = line
        return num > n

    return rv


def all_pass(preds):
    def rv(v):
        for pred in preds:
            if not pred(v):
                return False
        return True

    return rv


def pattern_misses(grok, lines):
    bad_line_count = 0
    bad_lines = []
    for n, ln in lines:
        if grok.match(ln) is None:
            bad_line_count += 1
            bad_lines.append([n, ln])
    return bad_lines


# files = array<file name>
# grok_pattern = string
# custom_patterns = dict
def grok_misses_from_files(files, grok_pattern, custom_patterns={}, header_lines=0):
    grok = Grok(grok_pattern, custom_patterns=custom_patterns)
    pred = all_pass([
        skip_lines(header_lines), lambda x: grok.match(x[1]) is None
    ])
    all_misses = []
    for file in files:
        all_misses.append(filter_file_with_pred(file, pred))

    return all_misses
