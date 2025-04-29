words = ["a", "an", "the"]
# with open("filestr.txt", "r") as f1:
#     Data = f1.read()


# New_data = Data.lower()

# for i in words:
#     New_data = New_data.replace(f" {i} ", " ")


# New_data = ' '.join(New_data.split())


# with open("removed.txt", "w") as f2:
#     f2.write(New_data)



with open("filestr.txt", 'r') as infile, open("removed.txt", 'w') as outfile:
    for line in infile:
        for word in words:
            line = line.replace(f' {word} ', ' ')
        outfile.write(line)