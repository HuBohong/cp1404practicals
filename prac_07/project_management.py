from prac_07.project import Project

FILENAME = "project.txt"


def main():
    projects = load_projects()


def load_projects():
    projects = []
    with (open('projects.txt', 'r') as in_file):
        in_file.readline()
        for line in in_file:
            name, start_date, priority, cost_estimate, completion_percentage = line.strip().split("\t")
            project = Project(name, start_date, priority, cost_estimate, completion_percentage)
            projects.append(project)
    return projects


main()
