import tkinter as tk
import json

app = tk.Tk()

text = tk.Text(app)

text.pack()

json_val = json.loads('{"a": 5, "b": 7}')

for k in json_val:
    text.insert(tk.END, '{} = {}\n'.format(k,json_val[k]))
text.config(state = tk.DISABLED)
app.mainloop()