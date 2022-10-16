import sys, os

def add_to_step_output(**kwargs):
    """
    Add kwargs to the step outputs
    """
    with open(os.environ["GITHUB_OUTPUT"], 'a') as f:
        for k, v in kwargs.items():
            f.write(f'\n{k}="{v}"')

sem_ver = os.environ["INPUT_SEMVER"]
tags = []

if "-" not in sem_ver:
    if "+" in sem_ver:
        sem_ver = sem_ver.split("+", maxsplit=1)[0]

    if "." in sem_ver:
        major, minor, patch = sem_ver.split(".")

        tags.append(f"v{major}")
        tags.append(f"v{major}.{minor}")
        tags.append(f"v{major}.{minor}.{patch}")

if (v := f"v{sem_ver}") not in tags and sem_ver:
    tags.append(v)

print("Tags that apply to this version: " +",".join(tags))
space_seperated_tags = " ".join(tags)

add_to_step_output(tags=space_seperated_tags)