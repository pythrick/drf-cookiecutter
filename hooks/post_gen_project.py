import random
import string

from shutil import copyfile


def create_random_secret_key():
    chars = string.ascii_letters + string.digits
    secret_key = "".join(random.choice(chars) for _ in range(32))
    with open(".secrets.yaml", "w+") as secrets_file:
        secrets_file.write("default:\n")
        secrets_file.write(f"  SECRET_KEY: {secret_key}")


def creating_env_file():
    copyfile('.env.template', '.env')


def copy_dot_secrets():
    copyfile('.secrets.template.yaml', '.secrets.yaml')


if __name__ == "__main__":
    create_random_secret_key()
    creating_env_file()
    copy_dot_secrets()
