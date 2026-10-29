# encode-html.py

import sys

if __name__ == '__main__':
    if len(sys.argv) != 2 and len(sys.argv) != 3:
        print("""Usage: python encode-html.py <infile_path> [<outfile_path>]
    - infile is html
    - outfile is txt; omitted it injects output into <code> of infile html""")
        exit(1)
    infile_path =  sys.argv[1]
    if len(sys.argv) == 3:
        outfile_path = sys.argv[2]
        inject = False
    else:
        inject = True
    
    with open(infile_path, 'r') as infile:
        content = infile.read()
        htmlMinusCodeBlock = ""
        encodedHtml = ""
        halt=False
        for idx in range(len(content)):
            char = content[idx]
            str_to_add = ''
            if char == '<':
                if content[idx:idx+6] == '<code>':
                    halt=True
                    # <code> block in the orignal HTML starts here, so save it.
                    injectIdx = idx+5
                    encodedHtml+='&lt;code&gt;[omitted for idempotency]'
                    htmlMinusCodeBlock+='<code>'
                elif content[idx:idx+7] == '</code>':
                    halt=False
                    str_to_add='&lt;'
                else:
                    str_to_add='&lt;'
            elif char == '>':
                str_to_add='&gt;'
            elif char == '"':
                str_to_add='&quot;'
            elif char == '&':
                str_to_add='&amp'
            else:
                str_to_add=char   
            if not halt:
                htmlMinusCodeBlock += char
                encodedHtml+=str_to_add
                
    # now the encoding is in encodedHtml
    # original HTML minus whatever is in the code block is in htmlMinusCodeBlock
    
    if inject:
        newContent = ""
        for idx in range(len(htmlMinusCodeBlock)):
            newContent+=htmlMinusCodeBlock[idx]
            if idx == injectIdx:
                newContent+=encodedHtml.strip()
        with open(infile_path, 'w') as infile:
            infile.write(newContent)
            
    else:
        with open(outfile, 'w') as outfile:
            outfile.write(encodedHtml)