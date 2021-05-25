import ssh
import deployment.setup_handler as setup_handler

try:
    client = ssh.SSHClient("ubuntu_server_kp.pem", "ec2-3-17-154-48.us-east-2.compute.amazonaws.com", "ubuntu")
    client.connect()

    # setup_handler.make_project_directory(client, "projects")
    # setup_handler.list_base_directories(client)
    setup_handler.update_get_tools(client)
    # setup_handler.install_docker(client)
    setup_handler.clone_git_repository(client, "https://github.com/mslegion/BasicFilterProxy.git")
    setup_handler.install_maven(client)
    setup_handler.run_application(client, "BasicFilterProxy")
    setup_handler.kill_application(client)

    client.close()
except Exception as e:
    print(e)
