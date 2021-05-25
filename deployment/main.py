import ssh
import deployment.setup_handler as setup_handler

try:
    client = ssh.SSHClient("ubuntu_server_kp.pem", "ec2-3-17-162-73.us-east-2.compute.amazonaws.com", "ubuntu")
    client.connect()

    setup_handler.make_project_directory(client, "projects")
    setup_handler.list_base_directories(client)
    setup_handler.install_docker(client)
    # TODO: Pull git repository
    # TODO: Run docker container

    client.close()
except Exception as e:
    print(e)
