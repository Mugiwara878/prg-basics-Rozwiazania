###
# Saves employees working at a specified position to a file
#
employees_file = 'it_company.csv'
position_file = 'software_engineer.txt'
job_title = 'Software Engineer'

with open(employees_file, 'r') as in_file:
    with open(position_file, 'w') as out_file:   # dwa pliki otwarte NARAZ (zagnieżdżone with)
        for line in in_file:
            if job_title in line:
                out_file.write(line)