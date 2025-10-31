output_format = 'Decimals'

def selected_format():
    return output_format

def set_format(value: str):
    global output_format
    if value in ('Decimals', 'Fractions'):
        output_format = value

def get_format():
    return output_format
