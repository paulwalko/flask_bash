from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route("/")
def show_entries():
    bash_quotes = 'bash_logs'
    bash_quotes_path = os.path.join(os.path.expanduser('~/.phenny'), bash_quotes)
    
    if not os.path.exists(bash_quotes_path):
        return

    files = os.listdir(bash_quotes_path)
    for i in range(len(files)):
        files[i] = files[i].replace('.txt', '')
        files[i] = int(files[i])

    files.sort(reverse=True)
    for i in range(len(files)):
        files[i] = ''.join([str(files[i]), '.txt'])
    
    files_contents = []
    for f in files:
        f = os.path.join(bash_quotes_path, f)
        with open(f) as fOpen:
            content = fOpen.readlines()
            files_contents.append(content)

    for files in files_contents:
        for line in files:
            line = line.replace('<', '&lt;')
            line = line.replace('>', '&gt;')

    return render_template('show_entries.html', length=len(files_contents), entries=files_contents, i=range(len(files_contents)))

if __name__ == "__main__":
    app.run()
