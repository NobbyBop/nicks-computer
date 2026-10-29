# encode-html.py
Takes html text and returns the encoded html for display on an html page. It 
also omits code blocks so that if (like me) you are inserting the output back 
into the original page it is encoding, it is idempotent.

### **UPDATE**: now injects the output directly back into the source HTML file.

- Ex: `python encode-html.py index.html`
    - encodes all characters of `index.html` except within `<code></code>`
    - takes the encoding, injects it to replace whatever is in `<code></code>` 
of the original `index.html` file
    
- Ex: `python encode-html.py index.html output.txt`
    - encodes all characters of `index.html` except within `<code></code>`
    - outputs that to output.txt

- Encodings:
	- `<` -> `&lt;`
	- `>` -> `&gt;`
	- `"` -> `&quot;`
	- `&` -> `&amp;`