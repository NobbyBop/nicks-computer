## encode-html: Takes html text and returns the encoded html for display on an 
## html page. It also omits code blocks so that if (like me) you are inserting
## the output back into the original page it is encoding, it is idempotent.
import sys

if __name__ == '__main__':
    with open('infile.html', 'r') as infile:
        with open('outfile.txt', 'w') as outfile:
            content = infile.read()
            newContent = ""
            halt=False
            for idx in range(len(content)):
                char = content[idx]
                str_to_add = ''
                if char == '<':
                    print(content[idx:idx+6])
                    if content[idx:idx+6] == '<code>':
                        halt=True
                        newContent+='&lt;code&gt;[omitted for idempotency]'
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
                    newContent+=str_to_add
            outfile.write(newContent)
