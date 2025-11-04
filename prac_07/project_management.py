from prac_07.project import Project

FILENAME = "projects.txt"
MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""


def main():
    projects, count = load_projects(FILENAME)
    print(f"Welcome to Pythonic Project Management\nLoaded {count} projects from {FILENAME}\n" + MENU)
    user_choice = input(">>>").upper()
    while user_choice != "Q":
        if user_choice == "L":
            filename = input("Please enter the filename of your projects you would like to load: ")
            projects,count = load_projects(filename)
        elif user_choice == "S":
            save_projects(projects)
        elif user_choice == "D":
            display_projects(projects)
        elif user_choice == "F":
            pass
        elif user_choice == "A":
            add_project(projects)
        elif user_choice == "U":
            pass
        else:
            print("Invalid menu choice")
        user_choice = input(">>>").upper()
        print(MENU)


def load_projects(filename=FILENAME):
    projects = []
    count = 0
    with (open(filename, 'r') as in_file):
        in_file.readline()
        for line in in_file:
            name, start_date, priority, cost_estimate, completion_percentage = line.strip().split("\t")
            project = Project(name, start_date, priority, cost_estimate, completion_percentage)
            projects.append(project)
            count += 1
    return projects, count


def display_projects(projects):
    #TODO: DATE SORTING
    print("Incomplete projects:")
    for i, project in enumerate(projects):
        if int(project.completion_percentage) < 100:
            print(f"{i} {project}")

    print("Complete projects:")
    for i, project in enumerate(projects):
        if int(project.completion_percentage) == 100:
            print(f"{i} {project}")


def add_project(projects):
    #TODO:ERROR CHECKING
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))
    project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(project)

def save_projects(projects):
    filename = input("Please enter the filename of your projects you would like to save: ")
    with open(filename, 'w') as out_file:
        for project in projects:
            print(project.name, project.start_date, project.priority, project.cost_estimate, project.completion_percentage, sep="\t", file=out_file)
    print(f"{len(projects)} projects saved to {filename}")


main()
