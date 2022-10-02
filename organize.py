
import re
import sys

lines = [line for line in sys.stdin]

# go through lines, identify commit message vs file
commit_regex = r"^\w{7,10} "

# grouped_by_commit will be a list of tuples; tuples will be (commit line, list of file paths)
grouped_by_commit = []
filenames = []

for line in lines:
    # remove newline at end of each line
    line = line[:-1]
    if re.findall(commit_regex, line):
        grouped_by_commit.append((line, []))
    else:
        if grouped_by_commit:
            grouped_by_commit[-1][1].append(line)
        filenames.append(line)

filenames = set(filenames)

grouped_by_filename = {}

for commit, files in grouped_by_commit:
    for filename in files:
        if filename not in grouped_by_filename:
            grouped_by_filename[filename] = []
        grouped_by_filename[filename].append(commit)

def styleAsCode(s):
    return f"<code>{s}</code>"

def strip_amp(s):
    regex = r"AMP-\d{5}"
    return re.sub(regex, '', s)

def printableVersion(grouping, use_detail=True, file_path=False, showCommitNum=True):
    for filename, commits in grouping:
        if not file_path:
            filename = filename.split("/")[-1]

        filename = styleAsCode(filename)

        commit_num_message = ''
        if showCommitNum:
            commit_num_message = f' with {styleAsCode(len(commits))} commits'

        if use_detail:
            print(f"<details><summary>{filename}{commit_num_message}</summary>\n")
        else:
            print(f"- {filename}")
        for commit in commits:
            _s = '' if use_detail else '\t'
            commit = strip_amp(commit)
            print(f"{_s}- {commit}")
        if use_detail:
            print("\n</details>")

printableVersion(sorted(grouped_by_filename.items(), key=lambda x: -len(x[1])))
