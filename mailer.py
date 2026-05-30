#Use for educational purposes 
   #~Akaza

import requests
import sys
import time
from colorama import init
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import pyfiglet

# Initialize
init(autoreset=True)
console = Console()
API_URL = "https://api.proxynova.com/v1/send_email"

def slow_type(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def banner():
    ascii_banner = pyfiglet.figlet_format("AKAZA", font="slant")
    console.print(Panel.fit(Text(ascii_banner, style="bold yellow"), 
                            title="", border_style="green"))

def loading(text, dots=4, delay=0.15):
    console.print(f"[yellow]{text}[/yellow]", end="")
    for _ in range(dots):
        sys.stdout.flush()
        time.sleep(delay)
        console.print("[yellow].[/yellow]", end="")
    print()

def send_mail(to, sender_name, subject, message):
    payload = {
        "to": to,
        "from": sender_name,
        "subject": subject,
        "message": message
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "/"
    }

    loading("loading mail transfer")  
    try:  
        resp = requests.post(API_URL, data=payload, headers=headers)  
        time.sleep(0.5)  

          
        status_text = f"[cyan]Status Code:[/cyan] [white]{resp.status_code}[/white]\n"  
        status_text += f"[cyan]Server Reply:[/cyan] [white]{resp.text}[/white]\n"  

        if resp.status_code == 200:  
            status_text += "\n[bold green]EMAIL SENT SUCCESSFULLY ✅[/bold green]"  
        else:  
            status_text += "\n[bold red]FAILED TO SEND EMAIL 📨 [/bold red]"  

        console.print(Panel.fit(status_text, title="STATUS PANEL", 
                                border_style="green" if resp.status_code == 200 else "red"))  
    except Exception as e:  
        console.print(Panel.fit(f"[bold red]Error:[/bold red] {str(e)}", border_style="red"))

if __name__ == "__main__":
    banner()
    try:
        console.print(Panel.fit("Enter the email details below:", border_style="magenta"))
        to = console.input("[cyan bold]Target Email : [/cyan bold]")
        sender_name = console.input("[cyan bold]Target Name    : [/cyan bold]")
        subject = console.input("[cyan bold]Mail Subject        : [/cyan bold]")
        message = console.input("[cyan bold]Write message here       : [/cyan bold]")

        send_mail(to, sender_name, subject, message)  

        console.print(Panel.fit("[bold red] BY AKAZA | @akazatec •[/bold red]", border_style="red"))  
    except KeyboardInterrupt:  
        console.print("\n[bold red][!] Exiting... Thank u for using![/bold red]\n")