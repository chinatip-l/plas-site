import os

# Get the current working directory
current_directory = os.getcwd()

# List all files in the current directory
files_in_directory = os.listdir(current_directory)

# Filter out only HTML files
html_files = [file for file in files_in_directory if file.endswith('.html')]
html_files.sort()

# Print the list of HTML files


block="""
<h2 id="list">Problems</h2>

<table class="table table-striped table-bordered table-hover">

<tr><th>Problem No</th><th>ProblemName</th><th>Remark</th></tr>
"""
tail="""
</table>
<h2 id="submission">Submission</h2>
<code>1</code>
<div id="user"><input class="form-control" type="text"  placeholder="Student ID"></div>
<code>2</code>
</br><a class="btn" onclick="expression()">Show Record</a>
<textarea readonly onclick="this.focus();this.select()" class="form-control" id="show_result" value="b" placeholder="Your Record"></textarea>
<code>3</code>
</br><a class="btn btn-success" onclick="TextSave()">Save</a>
<a id='DL_link'></a>
"""

res=""
res+=block
cnt=1
for html_file in html_files:


    head=f"""
    <tr onclick="location.href='index.html?pages/{html_file}'">
    <td width="20%">{cnt}</td>
    <td width="50%">{html_file.split(".")[0]}</td>
    <td id="p0116" width="30%"></td></tr>
    """

    res+=head
    cnt+=1

res+=tail


print(res)
with open('list.txt', 'w') as file:
    file.write(res)

