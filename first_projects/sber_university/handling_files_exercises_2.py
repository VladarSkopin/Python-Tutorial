def email_gen(list_of_names):
    emails = []
    for i in list_of_names:
        letter = 1
        while i[1] + '.' + i[0][0:letter] + '@company.io' in emails:
            letter += 1
        emails.append(i[1] + '.' + i[0][0:letter] + '@company.io')
    return emails


print(email_gen([['Ivan', 'Petrov'], ['Ivan', 'Petrov'], ['Ivan', 'Petrov']]))
# -> ['Petrov.I@company.io', 'Petrov.Iv@company.io', 'Petrov.Iva@company.io']

f = open('task_file.txt')
output_file = open('task_file_output.txt', 'w')
output_text = ''
for line in f:
    line_array = line.split(',')
    if line_array[1].strip() != '' and line_array[2].strip() != '' and line_array[3].strip() != '' and line_array[4] != '' and line_array[0] != 'EMAIL' and len(line_array[3].strip()) == 7:
        name = line_array[1].strip()
        surname = line_array[2].strip()
        output_line = email_gen([[name, surname]])
        output_text += output_line[0]
        output_text += '\n'
output_file.write(output_text)
f.close()
output_file.close()
