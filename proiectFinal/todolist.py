import os

from tenacity import sleep

tasks = []
categories = ["curs", "cumparaturi", "munca", "timp liber"]

if os.path.exists("tasks.txt"):
    with open("tasks.txt", "r") as f:
        for line in f:
            nume, deadline, responsabil, categorie = line.strip().split(",")
            tasks.append({
                "nume": nume,
                "deadline": deadline,
                "responsabil": responsabil,
                "categorie": categorie
            })

def addTask():
    task = input("Nume task: ")
    responsable = input("Persoana responsabila: ")
    deadline = input("Deadline: ")
    category = input("Categorie: ")
    if category not in categories:
        print("Categorie invalida")
        sleep(1)
        return 
    task_data = {
        "nume": task,
        "deadline": deadline,
        "responsabil": responsable,
        "categorie": category
    }
    tasks.append(task_data)
    
    with open("tasks.txt", "a") as f:
        f.write(f"{task},{deadline},{responsable},{category}\n")
    print("Task adaugat")
    sleep(1)
    
def showTasks():
    if not tasks:
        print("Nu exista taskuri.")
        return
    for t in tasks:
        print(f"- {t['nume']} | {t['deadline']} | {t['responsabil']} | {t['categorie']}")
        # print(t["nume"], t["deadline"], t["responsabil"], t["categorie"])

def saveTasks():
    with open("tasks.txt", "w") as f:
        for t in tasks:
            f.write(f"{t['nume']},{t['deadline']},{t['responsabil']},{t['categorie']}\n")

def deleteTask():
    nume = input("Introdu numele taskului de sters: ")
    global tasks
    tasks = [t for t in tasks if t["nume"] != nume]
    saveTasks()
    print("Task sters (daca a existat).")
    sleep(1)

def sortByResponsabil():
    if not tasks:
        print("Nu exista taskuri.")
        return
    sorted_tasks = sorted(tasks, key=lambda task_data: task_data["responsabil"].lower())
    # sortare fara sa modifice lista initiala
    for t in sorted_tasks:
        print(f"- {t['responsabil']} | {t['nume']} | {t['deadline']} | {t['categorie']}")

if __name__ == "__main__":
    print("To do list app")
    while True:
        print("\n------------------")
        print("1. Adauga task")
        print("2. Sterge task")
        print("3. Afiseaza task-uri")
        print("4. Sortare dupa persoana responsabila")
        print("5. Quit")
        
        choice = input("Introdu optiunea (1–5): ")
        
        if choice == "1":
            addTask()
        elif choice == "2":
            deleteTask()
        elif choice == "3":
            showTasks()
        elif choice == "4":
            sortByResponsabil()
        elif choice == "5":
            break
        else:
            print("Optiune invalida.")