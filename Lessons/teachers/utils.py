def format_records(lst):
    if len(lst) == 0:
        return '(Emtpy recordset)'

    result = []

    for elem in lst:
        formatted_elem = f'<a href="/teachers/update/{elem.id}">EDIT</a> {elem}'
        result.append(formatted_elem)

    return '<br>'.join(result)
