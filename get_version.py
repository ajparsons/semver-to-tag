from ruamel.yaml import YAML

def add_to_step_output(**kwargs):
    """
    Add kwargs to the step outputs
    """
    with open(os.environ["GITHUB_OUTPUT"], 'a') as f:
        for k, v in kwargs.items():
            f.write(f'\n{k}={v}')

def get_version():

    yaml=YAML(typ='safe')

    with open("action.yaml") as stream:
        try:
            data = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    version = data["version"]
    add_to_step_output(action_version=version)

if __name__ == "__main__":
    get_version()

