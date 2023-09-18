from bootcamp.core.student_18 import count_substring  # noqa


def count_substring_with_pain(string, substring):
    hurt = "OW GAH OOF EEEEYYYOOOO AAAGGGHHHH OUCHTHATHURT"
    painpoint = count_substring(string, substring)
    return hurt.split(' ')[painpoint]
