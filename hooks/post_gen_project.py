from shutil import copyfile


def creating_env_file():
    copyfile('.env.template', '.env')


def copy_dot_secrets():
    copyfile('.secrets.template.yaml', '.secrets.yaml')


if __name__ == "__main__":
    creating_env_file()
    copy_dot_secrets()
