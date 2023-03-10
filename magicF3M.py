
import openai
import tkinter as tk
from  pynput.keyboard  import  Key ,  Listener

openai.api_key = str(input())


def send_query():
    query = query_box.get()
    
    def limpiarCajas():
        query_box.delete(0,10)
        
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=query,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    
    lines = []
    current_line = ""
    for char in response.choices[0].text:
        limpiarCajas()
        if char == '.':
            lines.append(current_line)
            current_line = char
        else:
            current_line += char
    lines.append(current_line)
    
    answer_label.config(text="\n".join(lines))
    

window = tk.Tk()
window.config(bg='lavender')
window.title("F3M")

query_box = tk.Entry(window, width=50)
query_box.pack()
send_button = tk.Button(window, text="Enviar", command=send_query)
send_button.pack()
answer_label = tk.Label(window, text="        Bienvenido a <magicF3M>, preguntame lo que quieras       ", background="lavender")
answer_label.pack()

window.mainloop()

    