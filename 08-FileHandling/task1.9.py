###
# Prints employees employed in a specified position, numbered
#
job_title = 'Software Engineer'
counter = 1
with open('it_company.csv', 'r') as file:
    for line in file:
        if job_title in line:
            print(counter, line, end="")
            counter += 1