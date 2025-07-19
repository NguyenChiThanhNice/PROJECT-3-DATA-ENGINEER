import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import pandas as pd
import os

class TMDBAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PROJECT 3 - Analyse TMDB avec Pandas")
        self.root.geometry("900x600")

        self.file_path = ""
        self.df = None

        self.create_widgets()

    def create_widgets(self):
        # Boutons de chargement de fichier
        tk.Button(self.root, text="📂 Charger CSV", command=self.load_csv).pack(pady=10)
                  
        # Frame de boutons d'analyse
        frame = tk.Frame(self.root)
        frame.pack(pady=5)

        actions = [
            ("1. Trier par date", self.sort_by_release),
            ("2. Vote > 7.5", self.filter_high_votes),
            ("3. Revenu Max/Min", self.revenue_extremes),
            ("4. Total revenue", self.total_revenue),
            ("5. Top 10 profits", self.top10_profits),
            ("6. Réalisateurs / Acteurs actifs", self.frequent_people),
            ("7. Statistiques genres", self.genre_stats)
        ]

        for label, action in actions:
            tk.Button(frame, text=label, width=20, command=action).pack(pady=3)

        # Journal de sortie
        self.output = scrolledtext.ScrolledText(self.root, width=100, height=20)
        self.output.pack(padx=10, pady=10)

    def log(self, message):
        self.output.insert(tk.END, message + "\n")
        self.output.see(tk.END)

    def load_csv(self):
        path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if path:
            self.file_path = path
            try:
                self.df = pd.read_csv(path)
                self.log(f"✅ Fichier chargé : {os.path.basename(path)}")
            except Exception as e:
                messagebox.showerror("Erreur", f"Erreur de chargement: {e}")

    def sort_by_release(self):
        if self.df is not None:
            df_sorted = self.df.sort_values(by="release_date", ascending=False)
            df_sorted.to_csv("sorted_by_date.csv", index=False)
            self.log("✅ Films triés par date décroissante → saved to sorted_by_date.csv")
        else:
            self.log("❌ Aucune donnée chargée.")

    def filter_high_votes(self):
        if self.df is not None:
            df_filtered = self.df[self.df["vote_average"] > 7.5]
            df_filtered.to_csv("filtered_vote_gt_7.5.csv", index=False)
            self.log("✅ Films avec vote > 7.5 → {len(df_filtered)} films → saved to filtered_vote_gt_7.5.csv")
        else:
            self.log("❌ Aucune donnée chargée.")

    def revenue_extremes(self):
        if self.df is not None:
            df_max_revenue = self.df[self.df["revenue"] == self.df["revenue"].max()]
            df_min_revenue = self.df[self.df["revenue"] == self.df["revenue"].min()]
            self.log(f"🎬 Revenu max :{df_max_revenue.iloc[0]["original_title"]} - {df_max_revenue.iloc[0]["revenue"]}")
            self.log(f"🎬 Revenu min :{df_min_revenue.iloc[0]["original_title"]} - {df_min_revenue.iloc[0]["revenue"]}")
        else:
            self.log("❌ Aucune donnée chargée.")

    def total_revenue(self):
        if self.df is not None:
            total = self.df["revenue"].sum()
            self.log(f"💰 Revenu total de tous les films : {total:,}")
        else:
            self.log("❌ Aucune donnée chargée.")

    def top10_profits(self):
        if self.df is not None:
            df_profit = self.df.copy()
            df_profit["profit"] = df_profit["revenue"] - df_profit["budget"]
            df_top10 = df_profit.sort_values(by="profit", ascending=False).head(10)
            df_top10.to_csv("top10_profit.csv", index=False)
            self.log("🏆 Top 10 films par profit → saved to top10_profit.csv")
        else:
            self.log("❌ Aucune donnée chargée")

    def frequent_people(self):
        if self.df is not None:
            directors = self.df["director"].dropna().str.split("|").explode()
            actors = self.df["cast"].dropna().str.split("|").explode()
            top_dir = directors.value_counts().idxmax()
            top_act = actors.value_counts().idxmax()
            self.log(f"🎬 Réalisateur le plus prolifique : {top_dir}")
            self.log(f"🎭 Acteur le plus présent : {top_act}")
        else:
            self.log("❌ Aucune donnée chargée")

    def genre_stats(self):
        if self.df is not None:
            df_genres = self.df["genres"].dropna().str.split("|").explode()
            df_stats = df_genres.value_counts()
            df_stats.to_csv("genres_stats.csv")
            self.log(f"📊 Statistiques des genres → saved to genre_stats.csv")
            self.log(str(df_stats.head(10)))

        else:
            self.log("❌ Aucune donnée chargée")

if __name__ == "__main__":
    root = tk.Tk()
    app = TMDBAnalyzerApp(root)
    root.mainloop()
    