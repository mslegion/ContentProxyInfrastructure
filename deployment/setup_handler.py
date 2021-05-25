def display_logs(out, err, cmd):
    if err != "":
        print(f"Warning/Error when running {cmd} command\n: {err}")
    if out != "":
        print(f"{cmd} logs\n: {out}")


def make_project_directory(client, directory_name):
    cmd = f"mkdir {directory_name}"
    out, err = client.execute_command(cmd)
    display_logs(out, err, cmd)


def list_base_directories(client):
    cmd = "ls"
    out, err = client.execute_command(cmd)
    display_logs(out, err, cmd)


def update_get_tools(client):
    cmd = "sudo apt-get update"
    out, err = client.execute_command(cmd)
    display_logs(out, err, cmd)


def uninstall_old_docker(client):
    cmd = "sudo apt-get remove docker docker.io"
    out, err = client.execute_command(cmd, "Y")
    display_logs(out, err, cmd)


def install_new_docker(client):
    cmd = "sudo apt-get install docker.io"
    out, err = client.execute_command(cmd, "Y")
    display_logs(out, err, cmd)


def install_docker(client):
    out, err = client.execute_command("docker --version")
    if err != "":
        print(f"Docker not installed: {err}")
        update_get_tools(client)
        install_new_docker(client)
    else:
        uninstall_old_docker(client)
        install_docker(client)
        print(f"Docker version is: {out}")
