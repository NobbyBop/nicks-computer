# build-table.py

import sys
import os
from functools import cmp_to_key

class Date:
    def __init__(self, m, d, y):
        self.m = m
        self.d = d
        self.y = y
            
    def toStr(self):
        return f"{self.m}-{self.d}-{self.y}"

def compareWorksByDate(work1, work2):
        """ 
        Compares the works by their date attribute.
        """
        a = work1["date"]
        b = work2["date"]
        
        if a.y > b.y:
            return -1
        if a.y < b.y:
            return 1
        if a.m > b.m:
            return -1
        if a.m < b.m:
            return 1
        if a.d > b.d:
            return -1
        if a.d < b.d:
            return 1
        return 0
        
def extractDate(string):
    """ of format mmddyyyy, return None if invalid"""
    if len(string) != 8:
        return None
    try:
        int(string)
    except:
        return None
    m = string[0:2]
    d = string[2:4]
    y = string[4:8]
    return Date(int(m), int(d), int(y))
    
if __name__ == "__main__":
    ## Naming format: type-mmddyyy-title_with_underscores
    html_files = [file for file in os.listdir() if ".html" in file]
    valid_types = {"exp": "Experiment", "proj": "Project", "blog":"Blog"}
    
    """
    list of
    {
        filename: str
        title: str
        date: Date
        type: str
    }
    """
    works = []
    
    ## Collect works from folder.
    for file in html_files:
        file_pieces = file.split("-")
        if len(file_pieces) != 3:
            continue
        typ = file_pieces[0]
        if typ not in valid_types.keys():
            continue
        date = extractDate(file_pieces[1])
        if date is None:
            continue
        title = file_pieces[2].replace("_"," ")[:-5]
        work = {"filename":file, "title":title, "type":typ, "date":date}
        works.append(work)
    
    works = sorted(works, key=cmp_to_key(compareWorksByDate))
    
    ## Build the HTML table to inject.
    htmlTable = """<table>
        <tr>
            <th>Title</th>
            <th>Date</th>
            <th>Type</th>
        </tr>
"""
    
    for work in works:
        htmlTable += f"""
        <tr>
            <td><a href="{work["filename"]}">
            {work["title"]}</a></td>
            <td>{work["date"].toStr()}</td>
            <td>{valid_types[work["type"]]}</td>
        </tr>
"""
    
    htmlTable += "\t</table>"
    
    with open("index.html", 'r') as infile:
        content = infile.read()
        tableStartIdx = content.find("<table>")
        tableEndIdx = content.find("</table>") + 8
        newHtml = content[:tableStartIdx] + htmlTable + content[tableEndIdx:]
    
    with open("index.html", 'w') as outfile:
        outfile.write(newHtml)
    """
    <table>
		<tr>
			<th>Title</th>
			<th>Date</th>
			<th>Type</th>
		</tr>
		<tr>
			<td><a href="experiment-01-html-encoding-and-injecting.html">
			Encoding and Injecting HTML with GitHub Pre-Commit</a></td>
			<td>10/25/2026 - 10/27/2026</td>
			<td>Experiment</td>
		</tr>
		<tr>
			<td><a href="project-01-peanut.html">
			peanut: the tiny agent harness</a></td>
			<td>09/27/2026 - 10/25/2026</td>
			<td>Project</td>
		</tr>
	</table>
    """