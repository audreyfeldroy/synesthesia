from string import ascii_lowercase

COLORS = {
    "a": "red",
    "b": "darkblue",
    "c": "gold"
}

def generate_alphabet_css():
    """Generate the CSS for each letter/color pair in `COLORS` dict"""
    css = ""
    for char in ascii_lowercase:
        css += ".{} {{color: {};}}".format(char, COLORS.setdefault(char, "black"))
    return css

def process_file(filename):
    """Read a file and print each char"""
    html = ""
    with open(filename) as f:
        content = f.readlines()
        for line in content:
            for i, char in enumerate(line):
                html += '<span class="{}">{}</span>'.format(char, char)
            html += "<br/>"
    return html

def write_html(css, text):
    """Write index.html with `css` and `text`"""
    content = """<html>
<head></head>
<body>
<style type="text/css">{css}</style>
{text}
</body>
</html>
""".format(css=css, text=text)
    outfile = open("index.html", 'w')
    outfile.write(content)
    outfile.close()


if __name__ == "__main__":
    write_html(generate_alphabet_css(), process_file('text.txt'))
