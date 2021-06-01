import json
import boto3
import hcl2


def display_logs(out, err, cmd):
    if err != "":
        print(f"Warning/Error when running {cmd} command:\n{err}")
    if out != "":
        print(f"{cmd} command output:\n{out}")


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


def clone_git_repository(client, repo_url):
    cmd = f"git clone {repo_url}"
    out, err = client.execute_command(cmd)
    display_logs(out, err, cmd)


def install_new_maven(client, prompt=None):
    cmd = "sudo apt-get install maven"
    out, err = client.execute_command(cmd, prompt, 10)
    display_logs(out, err, cmd)


def step_inside_directory(client, dir):
    cmd = f"cd {dir}; ls"
    out, err = client.execute_command(cmd)
    display_logs(out, err, cmd)


def compile_maven(client, project_dir):
    cmd = f"cd {project_dir}; mvn compile"
    out, err = client.execute_command(cmd)
    display_logs(out, err, cmd)


def run_maven(client, project_dir):
    cmd = f"cd {project_dir}; mvn exec:java -Dexec.mainClass=Main"
    out, err = client.execute_command(cmd)
    display_logs(out, err, cmd)


def run_application(client, project):
    compile_maven(client, project)
    run_maven(client, project)


def kill_application(client):
    cmd = f"sudo kill -9 $(sudo lsof -t -i:8080)"
    out, err = client.execute_command(cmd)
    display_logs(out, err, cmd)


def uninstall_old_maven(client):
    cmd = "sudo apt-get purge maven"
    out, err = client.execute_command(cmd, "Y", 10)
    display_logs(out, err, cmd)


def install_maven(client):
    out, err = client.execute_command("version")
    if err != "":
        print(f"Maven not installed:\n {err}")
        install_new_maven(client, "Y")
    else:
        uninstall_old_maven(client)
        install_new_maven(client)
        print(f"Maven version is: {out}")


def install_docker(client):
    out, err = client.execute_command("docker --version")
    if err != "":
        print(f"Docker not installed: {err}")
        install_new_docker(client)
    else:
        uninstall_old_docker(client)
        install_docker(client)
        print(f"Docker version is: {out}")


def get_terraform_variable_value(var_name):
    with open('../terraform/variables.tf', 'r') as file:
        var_dict = hcl2.load(file)
    value = None
    for variable in var_dict["variable"]:
        if var_name in variable:
            value = variable[var_name]["default"][0]
    return value


def get_aws_server_details():
    region = get_terraform_variable_value("aws_region")
    proxy_server_tag = get_terraform_variable_value("proxy_tag")

    with open('secrets.json') as json_file:
        secrets = json.load(json_file)

    ec2 = boto3.resource(
        "ec2",
        aws_access_key_id=secrets["aws_access_key_id"],
        aws_secret_access_key=secrets["aws_secret_access_key"],
        region_name=region
    )

    instances = ec2.instances.filter(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    for instance in instances:
        name = None
        for tag in instance.tags:
            if tag["Key"] == "Name":
                name = tag["Value"]

        if name == proxy_server_tag:
            key_pair_name = instance.key_name+".pem"
            host_name = instance.public_dns_name
            user_name = "ubuntu"
            return key_pair_name, host_name, user_name
