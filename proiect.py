import tkinter 
import customtkinter
import random
import time

# Setari app
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Baza aplicatiei
app = customtkinter.CTk()
app.geometry("1000x700")
app.title("Vizualizare tipuri sortari")

#afara functie
def afara():
    app.quit()
#buton de iesire
iesire=customtkinter.CTkButton(app,text="iesire",command=afara)
iesire.place(x=850,y=25)

# Variabile pentru radio buttons
elem_var = tkinter.StringVar(value="")
elem_sort = tkinter.StringVar(value="")

# Canvas pentru vizualizare
lungime_canvas = 600
inaltime_canvas = 300
canvas = tkinter.Canvas(app, width=lungime_canvas, height=inaltime_canvas, bg="black")
canvas.place(x=250, y=400)

is_paused = False
current_speed = 0.1
sorting_in_progress = False
data = []
initial_data = []  


# Functie pentru desenarea liniilor in canvas
def draw_lines(data, color_array):
    canvas.delete("all")  
    bar_width = lungime_canvas / len(data)
    max_height = max(data)  

    for i, value in enumerate(data):
        x1 = i * bar_width  
        y1 = inaltime_canvas - (value / max_height * inaltime_canvas) 
        x2 = x1 + bar_width  
        y2 = inaltime_canvas 
        canvas.create_rectangle(x1, y1, x2, y2, fill=color_array[i], outline=color_array[i])

    app.update_idletasks()

# butoane pauza si reluare
def toggle_pause():
    global is_paused
    is_paused = not is_paused
    pause_button.configure(text="Reluare" if is_paused else "Pauza")

# modificare viteza
def set_speed(speed):
    global current_speed
    current_speed = speed
    speed_label.configure(text=f"Viteza: {speed} sec")

# Check pause state
def check_pause():
    while is_paused:
        app.update()  
        time.sleep(0.1)  

# Bubble sort
def bubble_sort_visual_step(i, j):
    global is_paused, sorting_in_progress
    if i < len(data):
        if j < len(data) - i - 1:
            check_pause()  

            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]  
                draw_lines(data, ["red" if x == j or x == j + 1 else "blue" for x in range(len(data))])

            app.after(int(current_speed * 1000), bubble_sort_visual_step, i, j + 1)
        else:
            app.after(int(current_speed * 1000), bubble_sort_visual_step, i + 1, 0)
    else:
        draw_lines(data, ["green" for _ in range(len(data))])  
        on_sorting_complete()

# Insertion sort
def insertion_sort_visual_step(i):
    global is_paused, sorting_in_progress
    if i < len(data):
        check_pause() 

        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
        draw_lines(data, ["red" if x == j or x == j + 1 else "blue" for x in range(len(data))])
        app.after(int(current_speed * 1000), insertion_sort_visual_step, i + 1) 
    else:
        draw_lines(data, ["green" for _ in range(len(data))])
        on_sorting_complete() 

# Selection sort
def selection_sort_visual_step(i, _=None): 
    global is_paused, sorting_in_progress
    if i < len(data) - 1:
        min_index = i
        for j in range(i + 1, len(data)):
            check_pause() 

            if data[j] < data[min_index]:
                min_index = j

        if min_index != i:
            data[i], data[min_index] = data[min_index], data[i]  
            # Vizualizarea schimbului
            draw_lines(data, ["red" if x == i or x == min_index else "blue" for x in range(len(data))])

        app.after(int(current_speed * 1000), selection_sort_visual_step, i + 1, 0)  
    else:
        draw_lines(data, ["green" for _ in range(len(data))])  
        on_sorting_complete()  

# Merge Sort
def merge_sort_visual_step(arr):
    global is_paused, sorting_in_progress
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort_visual_step(left_half)
        merge_sort_visual_step(right_half)

        # imbina cele doua jumatati
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            check_pause()  # verifica daca s a pus pauza
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

        draw_lines(arr, ["red" for _ in range(len(arr))])

        app.after(int(current_speed * 1000), draw_lines, arr, ["green" for _ in range(len(arr))])
    else:
        draw_lines(arr, ["green" for _ in range(len(arr))])
        on_sorting_complete()

# dupa sortare butonul rulare va putea fi apasat
def on_sorting_complete():
    global sorting_in_progress
    sorting_in_progress = False
    run_butt.configure(state=tkinter.NORMAL)

# Algoritm rulare
def ruleaza_algortim():
    global data, initial_data, sorting_in_progress
    sort_alg = elem_sort.get()
    elem_v = elem_var.get()

    if sorting_in_progress:
        return

    # sa nu ruleze butonul "rulare" in timpul sortarii
    run_butt.configure(state=tkinter.DISABLED)

    if not sort_alg:
        rezultat.configure(text="Eroare, alegeti un algoritm de sortare")
        run_butt.configure(state=tkinter.NORMAL)
        return
    if not elem_v:
        rezultat.configure(text="Eroare, alegeti numarul de elemente care vor fi sortate")
        run_butt.configure(state=tkinter.NORMAL)
        return

    try:
        num_elem = int(elem_v)  
        data = [random.randint(10, 100) for _ in range(num_elem)]
        initial_data = data.copy()  
        rezultat.configure(text="Prelucrare in vizualizare")
        sorting_in_progress = True

        # care algoritm este folosit
        if sort_alg == "bubble_sort":
            bubble_sort_visual_step(0, 0)
        elif sort_alg == "insertion_sort":
            insertion_sort_visual_step(0)
        elif sort_alg == "selection_sort":
            selection_sort_visual_step(0, 0)
        elif sort_alg == "merge_sort":
            data = [random.randint(10, 100) for _ in range(num_elem)]
            merge_sort_visual_step(data)

    except ValueError:
        rezultat.configure(text="Eroare, valoare invalida pentru elemente")
        run_butt.configure(state=tkinter.NORMAL)
        return

# resetare la datele initiale
def reset_data():
    global data
    data = initial_data.copy() 
    draw_lines(data, ["blue" for _ in range(len(data))]) 

# Elemente UI
algo = customtkinter.CTkLabel(app, text="Alegeti algoritmul de sortare")
algo.place(x=50, y=10)
nr_elem = customtkinter.CTkLabel(app, text="Alegeti numarul de elemente")
nr_elem.place(x=300, y=10)

# Buton de rulare
run_butt = customtkinter.CTkButton(app, text="Rulare", command=ruleaza_algortim)
run_butt.place(x=550, y=50)

# Butoane pentru controlul vitezei si  pauzei

pause_button = customtkinter.CTkButton(app, text="Pauza", command=toggle_pause)
pause_button.place(x=550, y=100)

speed_ultra_slow=customtkinter.CTkButton(app,text="Foarte lent",command=lambda:set_speed(2))
speed_ultra_slow.place(x=750,y=100)
speed_label = customtkinter.CTkLabel(app, text="Viteza: 0.1 sec")
speed_label.place(x=750, y=50)

speed_slow = customtkinter.CTkButton(app, text="Lent", command=lambda: set_speed(0.3))
speed_slow.place(x=750, y=150)

speed_medium = customtkinter.CTkButton(app, text="Mediu", command=lambda: set_speed(0.05))
speed_medium.place(x=750, y=200)

speed_fast = customtkinter.CTkButton(app, text="Rapid", command=lambda: set_speed(0.001))
speed_fast.place(x=750, y=250)

speed_ultrafast = customtkinter.CTkButton(app, text="Ultra rapid", command=lambda: set_speed(0.0001))
speed_ultrafast.place(x=750, y=300)

# Reset button
reset_button = customtkinter.CTkButton(app, text="Reset", command=reset_data)
reset_button.place(x=750, y=350)

# Label pentru rezultate
rezultat = customtkinter.CTkLabel(app, text="", text_color="red")
rezultat.place(x=550, y=150)

# Butoane algoritmi sort
bubble_sort = customtkinter.CTkRadioButton(app, text="Bubble Sort", variable=elem_sort, value="bubble_sort")
bubble_sort.place(x=50, y=50)
insertion_sort = customtkinter.CTkRadioButton(app, text="Insertion Sort", variable=elem_sort, value="insertion_sort")
insertion_sort.place(x=50, y=100)
selection_sort = customtkinter.CTkRadioButton(app, text="Selection Sort", variable=elem_sort, value="selection_sort")
selection_sort.place(x=50, y=150)
merge_sort = customtkinter.CTkRadioButton(app, text="Merge Sort", variable=elem_sort, value="merge_sort")
merge_sort.place(x=50, y=200)

# Butoane numar de elemente
e_10 = customtkinter.CTkRadioButton(app, text="10", variable=elem_var, value="10")
e_10.place(x=300, y=50)
e_30 = customtkinter.CTkRadioButton(app, text="30", variable=elem_var, value="30")
e_30.place(x=300, y=100)
e_64 = customtkinter.CTkRadioButton(app, text="64", variable=elem_var, value="64")
e_64.place(x=300, y=150)
e_100 = customtkinter.CTkRadioButton(app, text="100", variable=elem_var, value="100")
e_100.place(x=300, y=200)

# Rulare aplicatie
app.mainloop()
