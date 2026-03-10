from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import IntPrompt
from rich.progress import track
import time

console = Console()


console.print(
    Panel.fit(
        "[bold cyan]Prime Generator[/bold cyan]\nFind the next N prime numbers",
        border_style="bright_blue",
    )
)


number = IntPrompt.ask("[yellow]Enter starting number")
limit = IntPrompt.ask("[yellow]How many primes to generate")


def isPrime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def getNextPrime(number, limit):
    primeList = []

    for _ in track(range(limit), description="Calculating primes..."):
        while True:
            if isPrime(number):
                primeList.append(number)
                number += 1
                break
            number += 1
        time.sleep(0.1)

    return primeList


primes = getNextPrime(number, limit)


table = Table(title="Prime Numbers")

table.add_column("Index", style="cyan")
table.add_column("Prime", style="green")

for i, p in enumerate(primes, 1):
    table.add_row(str(i), str(p))


console.print(table)

console.print("\n[bold green]Done generating primes.[/bold green]")