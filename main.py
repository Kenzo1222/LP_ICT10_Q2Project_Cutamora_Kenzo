from pyscript import document


def candidate_checker(e):
    club_members = {
        "kenzo cutamora",
        "briel lagran",
        "kyle delacalzada",
        "nick austria",
        "kaizen sy",
    }

    first_name = document.getElementById("first_name").value.strip()
    last_name = document.getElementById("last_name").value.strip()
    candidate = " ".join(f"{first_name} {last_name}".split())
    result = document.getElementById("result")

    if not candidate:
        result.textContent = "Please enter your first and last name."
        return

    if candidate.casefold() in club_members:
        result.textContent = f"Good job, {candidate}! You got in."
    else:
        result.textContent = f"Sorry, {candidate}, you did not get in."
