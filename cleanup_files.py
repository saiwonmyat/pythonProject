import os

def destroyfile(d_filename):
    with open(d_filename) as password_file:
    text = d_filename.read()
    lentext = len(text)
    zero_fill_line_length = 40
    zero_fill = ['0' * zero_fill_line_length
                      for _
                      in range(lentext // zero_fill_line_length + 1)]
    zero_fill = os.linesep.join(zero_fill)
    with open(d_filename, 'w') as password_file:
        password_file.write(zero_fill)