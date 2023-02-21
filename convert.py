# convert surge files to clash files
import os

dir_path = '.'
surge_files = [f for f in os.listdir(dir_path) if f.startswith('surge') and f.endswith('.txt')]
for surge_file in surge_files:
    clash_file = surge_file.replace('surge', 'clash')
    print('converting {} to {}'.format(surge_file, clash_file))

    with open(surge_file, 'r') as f, open(clash_file, 'w') as out_file:
        out_file.write('payload:\n')

        # Read the domain names line by line
        for line in f:
            # Strip any whitespace from the line
            line = line.strip()

            if 'cidr' in surge_file:
                line = line.split(',')[1]
                symbol = ''
            else:
                symbol = '+'

            parts = line.split(' ')
            # Prepend chars to the domain name
            new_line = "  - '{}{}' {}".format(symbol, parts[0], ' '.join(parts[1:]))
            # Write the new line to the output file
            out_file.write(new_line + '\n')