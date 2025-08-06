import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox

def get_weather():
    country = country_entry.get().lower().replace(" ", "-")
    city = city_entry.get().lower().replace(" ", "-")
    url = f"https://www.timeanddate.com/weather/{country}/{city}"
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            weather = soup.find('div', class_='bk-focus__qlook')
            if weather:
                temperature = weather.find('div', class_='h2').text.strip().replace('\xa0', '')
                result_label.config(text=f"🌡️ Temperature: {temperature}", fg="white")
            else:
                result_label.config(text="❌ Weather data not found.", fg="red")
        else:
            result_label.config(text="⚠️ Failed to fetch data.", fg="red")
    except Exception as e:
        messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("🌤️ Weather Finder")
root.geometry("400x300")
root.configure(bg="#6b6bf1")

frame = tk.Frame(root, bg="#606075", padx=20, pady=20)
frame.pack(expand=True, fill="both", padx=20, pady=20)

tk.Label(frame, text="Enter Country:", font=("Helvetica", 12), bg="#606075", fg="white").pack()
country_entry = tk.Entry(frame, font=("Helvetica", 12), width=30)
country_entry.pack(pady=5)

tk.Label(frame, text="Enter City:", font=("Helvetica", 12), bg="#606075", fg="white").pack()
city_entry = tk.Entry(frame, font=("Helvetica", 12), width=30)
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", font=("Helvetica", 12, "bold"),
    bg="#89CF81", relief="raised", command=get_weather).pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12) ,bg="#6b6bf1", fg="white")
result_label.pack(pady=10)

root.mainloop()
