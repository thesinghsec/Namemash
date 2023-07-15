# UserNamify - Generate list of usernames from a person's first and last name.
#!/usr/bin/env python
import sys
import os.path

def sanitize_name(name):
    return ''.join([c for c in name if c.isalpha() or c.isspace()])

if __name__ == '__main__': 
    if len(sys.argv) != 2:
        print(f'usage: {sys.argv[0]} names.txt')
        sys.exit(0)

    file_name = sys.argv[1]

    if not os.path.exists(file_name): 
        print(f'{file_name} not found')
        sys.exit(0)

    with open(file_name) as file:
        for line in file:
            name = sanitize_name(line)
            tokens = name.lower().split()

            if len(tokens) < 2: 
                # Skip lines without both first and last name
                continue
            
            first_name = tokens[0]
            last_name = ' '.join(tokens[1:])

            # Create possible usernames
            usernames = [
                first_name + last_name,          
                last_name + first_name,          
                first_name + '.' + last_name,    
                last_name + '.' + first_name,    
                last_name + first_name[0],       
                first_name[0] + last_name,       
                last_name[0] + first_name,       
                first_name[0] + '.' + last_name, 
                last_name[0] + '.' + first_name, 
                first_name,                      
                last_name                        
            ]

            # Print the generated usernames
            for username in usernames:
                print(username)

