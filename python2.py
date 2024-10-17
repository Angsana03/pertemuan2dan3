import PySimpleGUI as sg
sg.theme("dark magenta")
sg.theme_text_color("#006400")
window = sg.Window(title="Profile",
layout=[[sg.Text("SELAMAT DATANG DI KELAS",
font=("Arial",25,"italic","bold","underline"))],
[sg.Text("NPM : 2210010319")],
[sg.Text("Nama : MUHAMMAD BAGUS MAULANA ")],
[sg.Text("Kelas : 5M Reguler Banjarmasin")],
[sg.Text("Matkul : Pemrograman berbasis objek 2 ")]],
size=(510,200),
font=("Times", 18))
window()
window.close()
