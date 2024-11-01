import pathlib
import sys


file_extensions = ['.rex', '.rexx', '.cls', '.testGroup']


def lint(filepath):
    with open(filepath) as f:
        lines = f.readlines()

    error_found = False

    for i in range(0, len(lines)):
        line = lines[i]

        # Rule: First line
        if i == 0:
            if line.strip() == '':
                error_found = True
                print_message(filepath, 0, 'First line should not be blank.')

        # Rule: Leading spaces
        if not line.strip() == '' and (has_tab_indentation(line) or has_wrong_spaces_count(line)):
            error_found = True
            print_message(filepath, i, 'Incorrect indentation.')

        # Rule: Trailing spaces
        if has_trailing_whitespace(line):
            error_found = True
            print_message(
                filepath, i, 'Line should not have trailing whitespaces.')

        # Rule: Redundant blank line
        if i > 0:
            if lines[i-1].strip() == '' and line.strip() == '':
                error_found = True
                print_message(filepath, i, 'Redundant blank line.')

        # Rule: Last line
        if i == len(lines) - 1:
            if not (len(line) > 1 and line.endswith('\n')):
                error_found = True
                print_message(
                    filepath, i, 'File should end with one empty line.')

    if not error_found:
        print(f'{filepath}: Ok')

    print()


def has_tab_indentation(line):
    return '\t' in get_leading_whitespace(line)


def get_leading_whitespace(line):
    return line[0:len(line) - len(line.lstrip())]


def has_wrong_spaces_count(line):
    return len(get_leading_whitespace(line)) % 4 != 0


def has_trailing_whitespace(line):
    # because very last line has no line break
    return line.rstrip() != line and line.rstrip() + '\n' != line


def print_message(filepath, line, message):
    line += 1

    padding = ' ' * (4 - len(str(line)))

    print(f'{filepath}:{line}:{padding} {message}')


file_extensions = [str.lower(file_extension)
                   for file_extension in file_extensions]

path = pathlib.Path(sys.argv[1])

if path.is_file():
    lint(path)
elif path.is_dir():
    filepaths = [p for p in path.glob(
        '**/*') if p.suffix.lower() in file_extensions]

    for filepath in filepaths:
        lint(filepath)
else:
    print('Error: Path not found.')
