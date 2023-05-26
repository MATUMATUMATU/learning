#------------------------------------------------------------------------------
# IMDb keeps a list of 1001 Movies to See Before you Die:
#  https://www.imdb.com/list/ls060338474
#
# The list has been web scraped and stored in:
#  1001_movies_2023-03-28.txt
#
# Create a program which creates tidy csv file from the txt file:
#  1001_movies.csv
#------------------------------------------------------------------------------

# Open the input text file for reading (use UTF-8 encoding)
input_file = open ("1001_movies_2023-03-28.txt", "r", encoding="utf-8")

lines = input_file.readlines()
# Create a list to store the extracted movie data
movies = []
# Iterate over the lines of the text file

for idx in range(0, len(lines), 3):
  
    first_line = lines[idx]
    second_line = lines[idx+1]
    second_line_split = second_line.split("\t")
    # Fetch the title from first line
    title = first_line.strip()
    title = title.replace('"','')
    # Fetch year from second line. Use first date in case of range (e.g. Dekalog (1989–1990))
    year = second_line_split[0].split()[-1][1:5]
    
    
   
    # Fetch ratings from second line and use the dot as decimal separator
    rating = second_line_split[1].replace(',', '.')
    # Append to movie list
    
    output_line ='"' + title + '"'+','+ year + ',' + rating + "\n"
    movies.append(output_line)
# Write the movie data to the CSV file (with header "title,year,rating\n", use UTF-8 encoding)
header = "title,year,rating\n"
with open("1001_movies.csv", "w", encoding="utf-8") as aaa:
    aaa.write(header)
    for i in movies:
        aaa.write(i)
