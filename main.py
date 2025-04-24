import time
import random
from questions import questions

print("Tests!")

def calculate_score(start, end):
   elapsed = end - start
   score = max(0, int(1000 - elapsed * 50))
   return score

def start_quiz():
   total_score = 0

   for q in questions:
      print("\n" + q["question"])

      for key, value in q["options"].items():
         print(f"{key}: {value}")
      start_time = time.time()
      answer = input("Tava atbilde (A/B/C/D): ").strip().upper()

      if answer == "A" or "B" or "C" or "D":
         print("Atbilde ir pieņemta!")
         end_time = time.time()

      else:
         print("Atbilde nav pieņemta!")
         end_time = time.time()

      if answer == q["correct"]:
         score = calculate_score(start_time, end_time)
         print(f"Pareizi! Tu nopelnīji {score} punktus.")
         total_score += score
         print(f"\nTavs kopējais rezultāts: {total_score} punkti.")

      else:
         print(f"Nepareizi. Pareizā atbilde bija: {q['correct']}")
         print(f"\nTavs kopējais rezultāts: {total_score} punkti.")




if __name__ == "__main__":
   start_quiz()

