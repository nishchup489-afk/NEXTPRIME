### 1) copy whole file
### 2) in separate folder : `pip install rich`
### 3) then uncomment , paste and run


# from textual.app import App, ComposeResult
# from textual.widgets import Header, Footer, Input, Button, DataTable, Static
# from textual.containers import Vertical
# from textual.reactive import reactive


# def is_prime(n):
#     if n < 2:
#         return False

#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False

#     return True


# def get_next_primes(start, limit):
#     primes = []
#     number = start

#     while len(primes) < limit:
#         if is_prime(number):
#             primes.append(number)
#         number += 1

#     return primes


# class PrimeApp(App):

#     CSS = """
#     Screen {
#         align: center middle;
#     }

#     #container {
#         width: 60;
#         border: round cyan;
#         padding: 2;
#     }

#     Input {
#         margin: 1;
#     }

#     Button {
#         margin: 1;
#     }

#     DataTable {
#         margin-top: 2;
#     }
#     """

#     def compose(self) -> ComposeResult:
#         yield Header()

#         with Vertical(id="container"):
#             yield Static("Prime Generator", classes="title")

#             yield Input(placeholder="Starting number", id="start")
#             yield Input(placeholder="How many primes", id="limit")

#             yield Button("Generate Primes", id="generate")

#             yield DataTable(id="table")

#         yield Footer()

#     def on_mount(self):
#         table = self.query_one("#table", DataTable)
#         table.add_columns("Index", "Prime")

#     def on_button_pressed(self, event: Button.Pressed):
#         start_input = self.query_one("#start", Input)
#         limit_input = self.query_one("#limit", Input)

#         table = self.query_one("#table", DataTable)

#         table.clear()

#         try:
#             start = int(start_input.value)
#             limit = int(limit_input.value)
#         except ValueError:
#             return

#         primes = get_next_primes(start, limit)

#         for i, p in enumerate(primes, 1):
#             table.add_row(str(i), str(p))


# if __name__ == "__main__":
#     PrimeApp().run()