from pyscript import document
from pyodide.ffi import create_proxy


non_metals = {
    "Hydrogen": ("H", "1", "1.008"),
    "Carbon": ("C", "6", "12.011"),
    "Nitrogen": ("N", "7", "14.007"),
    "Oxygen": ("O", "8", "15.999"),
    "Phosphorus": ("P", "15", "30.974"),
    "Sulfur": ("S", "16", "32.06"),
    "Selenium": ("Se", "34", "78.971"),
    "Fluorine": ("F", "9", "18.998"),
    "Chlorine": ("Cl", "17", "35.45"),
    "Bromine": ("Br", "35", "79.904"),
    "Iodine": ("I", "53", "126.90"),
    "Astatine": ("At", "85", "210"),
    "Helium": ("He", "2", "4.0026"),
    "Neon": ("Ne", "10", "20.180"),
    "Argon": ("Ar", "18", "39.948"),
    "Krypton": ("Kr", "36", "83.798"),
    "Xenon": ("Xe", "54", "131.29"),
    "Radon": ("Rn", "86", "222"),
}

elements_by_input = {}
for name, details in non_metals.items():
    element = (name, *details)
    elements_by_input[details[0].casefold()] = element
    elements_by_input[name.casefold()] = element

input_field = document.getElementById("element_input")
result_card = document.getElementById("result-card")
message = document.getElementById("lookup-message")


def search():
    symbol_or_name = input_field.value.strip()
    element = elements_by_input.get(symbol_or_name.casefold())

    if element is None:
        result_card.hidden = True
        message.textContent = (
            "Enter a valid non-metal symbol or name."
            if symbol_or_name
            else "Please enter an element symbol or name."
        )
        return

    name, symbol, number, mass = element
    document.getElementById("result-symbol").textContent = symbol
    document.getElementById("result-name").textContent = name
    document.getElementById("result-number").textContent = number
    document.getElementById("result-mass").textContent = mass
    result_card.hidden = False
    message.textContent = ""


def handle_submit(event):
    event.preventDefault()
    search()


submit_handler = create_proxy(handle_submit)
document.getElementById("lookup-form").addEventListener("submit", submit_handler)
