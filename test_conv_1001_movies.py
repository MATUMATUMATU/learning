def compare_files(file1_path, file2_path):
    try:
        with open(file1_path, 'r', encoding='utf-8') as file1, open(file2_path, 'r', encoding='utf-8') as file2:
            lines1 = file1.readlines()
            lines2 = file2.readlines()

            if len(lines1) != len(lines2):
                return "Files have different number of lines."

            for line_num, (line1, line2) in enumerate(zip(lines1, lines2), start=1):
                if line1 == line2:
                    pass
#                    print(f"Line {line_num}: Similar")
                else:
                    print(f"Line {line_num}: Not similar")

    except FileNotFoundError:
        return "One or both files do not exist."

# Provide the file paths of the files to compare
file1_path = 'imdb/data/1001_movies.csv'
file2_path = 'imdb/data/1001_movies_ok.csv'

compare_files(file1_path, file2_path)