from modules import scripts
from rich import print
import yaml
import json
import os


SETTINGS = os.path.join(scripts.basedir(), "config.json")
OPTIONS = os.path.join(os.path.dirname(os.path.realpath(__file__)), "config.yaml")


def config():
    try:
        assert os.path.isfile(SETTINGS)
        assert os.path.isfile(OPTIONS)
    except AssertionError:
        return

    with open(OPTIONS, "r", encoding="utf-8") as stream:
        options: dict = yaml.safe_load(stream)

    if len(options.keys()) == 0:
        return

    with open(SETTINGS, "r", encoding="utf-8") as stream:
        settings: dict = json.load(stream)

    print("\n\n\n===== Launch Options =====")

    for key, option in options.items():

        if key not in settings.keys():
            print(f"\nInvalid Option: [bold red]{key}[/bold red] - Skipping...")
            continue

        print(
            f"\nSetting: [bold cyan]{key}[/bold cyan] (current: [dark_green]{settings[key]}[/dark_green])"
        )

        if len(option) == 1:
            if os.path.isdir(option[0]):
                option = os.listdir(option[0])
            else:
                continue

        for i, opt in enumerate(option):
            print(f"    [{i}]: {opt}")

        try:
            opt = input("  > ").strip()
        except KeyboardInterrupt:
            raise SystemExit
        except EOFError:
            raise SystemExit

        if not opt:
            continue

        try:
            settings[key] = option[int(opt)]
            print(
                f"\n[bright_blue]{key}[/bright_blue] -> [light_green]{option[int(opt)]}[/light_green]"
            )
        except ValueError:
            print("\nInvalid Input - Skipping...")
            continue
        except IndexError:
            print("\nInvalid Index - Skipping...")
            continue

    with open(SETTINGS, "w", encoding="utf-8") as stream:
        stream.write(json.dumps(settings))

    print("\n===== Launch Options =====\n\n\n")


config()
