import tkinter as tk
from tkinter import filedialog, messagebox
from packager import generate_cmake_package
from github_uploader import upload_to_github
import os

# ---- Interface graphique ----
def show_gui():
    root = tk.Tk()
    root.title("Boîte magique de Severus Rogue")
    root.geometry("800x500")
    root.configure(bg="#F4F4F4")

    title = tk.Label(
        root,
        text="🧙‍♂️ Boîte Magique de Severus Rogue",
        font=("Segoe UI", 18, "bold"),
        bg="#F4F4F4",
        fg="#222"
    )
    title.pack(pady=15)

    log_box = tk.Text(root, height=15, width=95, bg="#fff", fg="#000", relief="solid", borderwidth=1)
    log_box.pack(padx=10, pady=10)

    selected_folder = tk.StringVar()

    # ---- Actions ----
    def select_folder():
        folder = filedialog.askdirectory()
        if folder:
            selected_folder.set(folder)
            log_box.insert(tk.END, f"📁 Dossier sélectionné : {folder}\n")

    def generate_package():
        folder = selected_folder.get()
        if not folder:
            messagebox.showwarning("Attention", "Veuillez sélectionner un dossier avant de générer le package.")
            return

        result = generate_cmake_package(folder)
        log_box.insert(tk.END, f"{result}\n")

    def send_to_github():
        folder = selected_folder.get()
        if not folder:
            messagebox.showwarning("Attention", "Veuillez sélectionner un dossier avant d'envoyer sur GitHub.")
            return

        # Fenêtre popup pour saisir l’URL GitHub
        popup = tk.Toplevel(root)
        popup.title("Envoyer sur GitHub")
        popup.geometry("400x200")

        tk.Label(popup, text="URL du dépôt GitHub :", font=("Segoe UI", 10)).pack(pady=10)
        entry_url = tk.Entry(popup, width=50)
        entry_url.pack(pady=5)
        entry_url.insert(0, "https://github.com/jawharmanal/boite-magique-test.git")

        def confirm_upload():
            repo_url = entry_url.get().strip()
            if not repo_url:
                messagebox.showwarning("Attention", "Veuillez saisir une URL GitHub valide.")
                return

            log_box.insert(tk.END, f"☁️ Envoi du projet sur GitHub...\n")
            result = upload_to_github(folder, repo_url)
            log_box.insert(tk.END, f"{result}\n")
            popup.destroy()

        tk.Button(popup, text="Envoyer", command=confirm_upload, bg="#4CAF50", fg="white", font=("Segoe UI", 10)).pack(pady=10)

    # ---- Boutons ----
    frame_buttons = tk.Frame(root, bg="#F4F4F4")
    frame_buttons.pack(pady=15)

    tk.Button(frame_buttons, text="📁 Sélectionner un dossier", command=select_folder, bg="#E0E0E0", width=25).grid(row=0, column=0, padx=10)
    tk.Button(frame_buttons, text="⚙️ Générer le package (CMake)", command=generate_package, bg="#E0E0E0", width=25).grid(row=0, column=1, padx=10)
    tk.Button(frame_buttons, text="☁️ Envoyer sur GitHub", command=send_to_github, bg="#E0E0E0", width=25).grid(row=0, column=2, padx=10)

    root.mainloop()


if __name__ == "__main__":
    show_gui()
