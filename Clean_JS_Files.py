import jsbeautifier

def beautify_javascript(input_file, output_file):
    # Read the content of the input file
    with open(input_file, 'r') as f:
        messy_js = f.read()

    # Beautify the javascript code
    res = jsbeautifier.beautify(messy_js)

    # Write the beautified code to the output file
    with open(output_file, 'w') as f:
        f.write(res)

# Use the function
beautify_javascript('input.js', 'output.js')

