import sys
import subprocess
from rich.console import Console
from rich.table import Table
from rich import box
from rich.text import Text


def run_and_capture(script_path):
    try:
        # Run the script and capture stdout
        result = subprocess.run(
            [sys.executable, script_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        # Split output into lines
        output_lines = result.stdout.splitlines()
        return output_lines
    except Exception as e:
        print(f"Error: {e}")
        return []


def read_input_lines():
    input_lines = []
    while True:
        line = sys.stdin.readline()
        if not line or line.strip() == "":
            break
        input_lines.append(line.strip())
    return input_lines


def compare_outputs(res, expected):
    console = Console()
    table = Table(
        title="[bold underline green]Test Case Comparison[/]",
        show_header=True,
        header_style="bold white on dark_green",
        box=box.ROUNDED,
        show_lines=True,
        padding=(0, 1),
    )

    table.add_column("Index", justify="center", style="bold yellow", width=8)
    table.add_column(
        "Your Output", style="cyan", overflow="fold", justify="left", no_wrap=False
    )
    table.add_column(
        "Expected Output", style="green", overflow="fold", justify="left", no_wrap=False
    )
    table.add_column("Status", justify="center", width=10)

    max_len = max(len(res), len(expected))

    for i in range(max_len):
        r = res[i] if i < len(res) else "[dim]<missing>[/dim]"
        e = expected[i] if i < len(expected) else "[dim]<missing>[/dim]"

        if r == e:
            status = Text("✅ PASS", style="bold green")
        else:
            status = Text("❌ FAIL", style="bold red")

        table.add_row(str(i), str(r), str(e), status)

    console.print("\n")
    console.print(table)
    console.print(
        "\n[bold cyan]Summary:[/] [green]✓ {} passed[/], [red]✗ {} failed[/]\n".format(
            sum(
                1
                for i in range(max_len)
                if i < len(res) and i < len(expected) and res[i] == expected[i]
            ),
            sum(
                1
                for i in range(max_len)
                if i >= len(res) or i >= len(expected) or res[i] != expected[i]
            ),
        )
    )


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python runner.py <script.py>")
        sys.exit(1)

    script_file = sys.argv[1]

    Console().print("\n[bold cyan]> Enter input:[/]\n")

    result = run_and_capture(script_file)

    Console().print("\n[bold magenta]> Enter expected output:[/]\n")

    expected = read_input_lines()

    compare_outputs(result, expected)
