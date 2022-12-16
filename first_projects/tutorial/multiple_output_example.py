def get_scores(student_gardes):
    min = student_gardes[0]
    max = student_gardes[0]
    for g in student_gardes:
        if g < min:
            min = g
    for g in student_gardes:
        if g > max:
            max = g
    return (min, max)  # Multiple output


grades = [87, 100, 99, 72]

worst, best = get_scores(grades)  # Unpacking

print('worst:', worst)
print('best:', best)
