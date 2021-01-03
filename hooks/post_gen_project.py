import os


def init_git_repository():
    os.system("git init")


def first_commit():
    os.system("git add --all")
    os.system("git commit -m 'First commit'")


def init_project():
    os.system("make init")
    os.system("make format")


def create_migrations():
    os.system("make migrations")
    os.system("make migrate")


def lock_dependencies():
    os.system("make lock")


def run_project():
    print("Run the following to run the project: make run")


if __name__ == "__main__":
    init_git_repository()
    init_project()
    create_migrations()
    lock_dependencies()
    first_commit()
    print("Project successfully created.")
