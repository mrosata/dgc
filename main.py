__doc__ = """
This module is useful for debugging grok patterns. It is extremely simple.
1. Supply a list of files to read through
2. Supply a grok pattern string to use in the matches
3. Supply any custom patterns as dict { pattern_name: pattern_regex_str }
4. Supply optional number of header lines to chop out of each file 
  
  Grok implementation by: https://github.com/garyelephant/pygrok
"""
from grok_utils import grok_misses_from_files
from config import CUSTOM_PATTERNS, GROK_PATTERN, FILES, HEADER_LINES


# Pass in Array<Array<Pair<int, string>>> of misses from each file
# and it will print the results. Array of Arrays with results (which
# also happen to be arrays
def print_results(all_misses=[]):
    file_num = 0
    total_miss_count = 0

    for file_misses in all_misses:
        file_num += 1
        print(f"\n-------- FILE NUMBER {file_num} -------------")
        total_miss_count += len(file_misses)
        for line_num, line in file_misses:
            print(f"\n[ {line_num} ] - {line}")

        print(f"\nMissed {len(file_misses)} lines in file {file_num}")

    print(f"\nMissed {total_miss_count} lines total in {file_num} files")


if __name__ == '__main__':
    results = grok_misses_from_files(FILES, GROK_PATTERN, CUSTOM_PATTERNS, HEADER_LINES)
    print_results(results)
