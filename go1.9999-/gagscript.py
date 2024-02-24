# a script that will animate in several loading bars

import rich
from rich.console import Console
from rich.progress import Progress
from rich.panel import Panel
import time
import random
import webbrowser

rng = random.Random(0)
console = Console()


with Progress() as progress:

    task1 = progress.add_task("Building Go Binary...", total=100)

    for i in range(3):
        progress.update(task1, advance=rng.randint(0,5))
        time.sleep(.75)

    time.sleep(1.5)

console.print(Panel.fit("[bold red]PWNED[/bold red]", border_style="yellow", title_align="left", padding=(1, 2), title="You've been hacked!"))

with Progress() as progress:

    task1 = progress.add_task("[red]Downloading Trojan...", total=20)

    while not progress.finished:
        progress.update(task1, advance=0.5)
        time.sleep(.02)

# with Progress() as progress:

    task2 = progress.add_task("[blue]Exfiltrating Banking Information...", total=20)
    task3 = progress.add_task("[green]Stealing Coinye...", total=20)
    task5 = progress.add_task("[yellow]Installing Ransomware...", total=20)
    task4 = progress.add_task("[purple]Rickrolling...", total=20)
    task6 = progress.add_task("[cyan]Installing Keylogger...", total=20)
    rickrollProgress = 0

    while not progress.finished:
        progress.update(task2, advance=0.7)
        progress.update(task3, advance=0.5)
        progress.update(task4, advance=1.2)
        rickrollProgress += 1.2
        progress.update(task5, advance=0.3)
        progress.update(task6, advance=0.9)
        time.sleep(.1)

        if rickrollProgress > 20:
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
            rickrollProgress = -10000

console.print(Panel(title="Psych", border_style="red", title_align="left", padding=(1, 2), renderable="You've been rickrolled!\n"
                                                                                                      "Don't trust software on the internet."))
