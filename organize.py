
import re
my_filename = 'log.txt'

# if __name__ == "__main__":
with open(my_filename) as f:
    lines = f.readlines()

# go through lines, identify commit message vs file
commit_regex = r"^\w{10} "
# I want a list of tuples
    # tuples will be (commit line, list of file paths)

grouped_by_commit = []
filenames = []

for line in lines:
    # remove newline at end of each line
    line = line[:-1]
    if re.findall(commit_regex, line):
        # print(f"commit line found: {line}")
        grouped_by_commit.append((line, []))
    else:
        if grouped_by_commit:
            grouped_by_commit[-1][1].append(line)
        filenames.append(line)

filenames = set(filenames)
# print(*grouped_by_commit, sep="\n")
# print(filenames)

grouped_by_filename = {}

for commit, files in grouped_by_commit:
    for filename in files:
        if filename not in grouped_by_filename:
            grouped_by_filename[filename] = []
        grouped_by_filename[filename].append(commit)

# print(*grouped_by_filename.items(), sep="\n")

# printable version

def printableVersion(grouping, use_detail=True, file_path=False):
    for filename, commits in grouping.items():
        if not file_path:
            filename = filename.split("/")[-1]
        if use_detail:
            print(f"<details><summary>{filename}</summary>\n")
        else:
            print(f"- {filename}")
        for commit in commits:
            _s = '' if use_detail else '\t'
            print(f"{_s}- {commit}")
        if use_detail:
            print("\n</details>")

printableVersion(grouped_by_filename)
