def grades(*n, sit=False):

    r = {'total': len(n), 'max': max(n), 'min': min(n), 'average': sum(n) / len(n)}
    if sit:
        if r['average'] >= 7:
            r['situation'] = 'Good'
        elif r['average'] >= 5:
            r['situation'] = 'Average'
        else:
            r['situation'] = 'Bad'
    return r


help(grades)


#  program
resp = grades(5.5, 2.5, 9, 8, 5, 9, 10, sit=True)
print(resp)

