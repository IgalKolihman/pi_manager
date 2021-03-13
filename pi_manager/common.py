import subprocess


def exec_command(args: list):
    out = subprocess.run(args, stdout=subprocess.PIPE, shell=True)
    return out.stdout.strip().decode("utf-8")
