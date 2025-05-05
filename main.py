import time
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.progress import track
from questions import questions

console = Console()
print("[bold blue]Tests![/bold blue]")

def calculate_score(start, end):
    elapsed = end - start
    score = max(0, int(1000 - elapsed * 50))
    return score

def simulate_timer(seconds):
    for _ in track(range(seconds), description="[yellow]Laiks domāt...[/yellow]"):
        time.sleep(1)

def start_quiz():
    total_score = 0
    question_count = len(questions)

    for index, q in enumerate(questions, start=1):
        console.rule(f"[bold yellow]Jautājums {index} no {question_count}[/bold yellow]")
        print(f"[bold]{q['question']}[/bold]")

        for key, value in q["options"].items():
            print(f"[cyan]{key}:[/cyan] {value}")

        # Simulē vizuālu taimeri (dekoratīvi)
        simulate_timer(2)

        start_time = time.time()
        answer = input("\nTava atbilde (A/B/C/D): ").strip().upper()
        end_time = time.time()

        if answer in "ABCD":
            print("[green]Atbilde ir pieņemta![/green]")
        else:
            print("[red]Atbilde nav pieņemta![/red]")

        if answer == q["correct"]:
            score = calculate_score(start_time, end_time)
            print(f"[bold green]Pareizi! Tu nopelnīji {score} punktus.[/bold green]")
            total_score += score
        else:
            print(f"[bold red]Nepareizi. Pareizā atbilde bija: {q['correct']}[/bold red]")

        print(f"[bold blue]Tavs kopējais rezultāts: {total_score} punkti.[/bold blue]\n")

    console.rule("[bold magenta]Tests pabeigts![/bold magenta]")
    print(f"[bold white on green]Kopējais rezultāts: {total_score} punkti[/bold white on green]")

if __name__ == "__main__":
    start_quiz()
