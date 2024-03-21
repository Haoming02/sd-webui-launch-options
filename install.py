import launch

try:
    import yaml
except ModuleNotFoundError:
    launch.run_pip("install PyYAML")

try:
    import rich
except ModuleNotFoundError:
    launch.run_pip("install rich")
