## encode-html: Takes html text and returns the encoded html for display on an html page.
import sys

if __name__ == '__main__':
    with open('infile.html', 'r') as infile:
        with open('outfile.txt', 'w') as outfile:
            content = infile.read()
            newContent = ""
            for char in content:
                if char == '<':
                    newContent+='&lt;'
                elif char == '>':
                    newContent+='&gt;'
                elif char == '"':
                    newContent+='&quot;'
                elif char == '&':
                    newContent+='&amp'
                else:
                    newContent+=char              
            outfile.write(newContent)
