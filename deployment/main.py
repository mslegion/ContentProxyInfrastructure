import ssh
import deployment.setup_handler as setup_handler

try:
    key_pair_name, host_name, user_name = setup_handler.get_aws_server_details()
    client = ssh.SSHClient(key_pair_name, host_name, user_name)
    client.connect()

    setup_handler.update_get_tools(client)
    setup_handler.make_project_directory(client, "projects")
    setup_handler.list_base_directories(client)
    # setup_handler.install_docker(client)
    setup_handler.clone_git_repository(client, "https://github.com/mslegion/BasicFilterProxy.git")
    setup_handler.install_maven(client)
    setup_handler.run_application(client, "BasicFilterProxy")
    setup_handler.kill_application(client)

    client.close()
except Exception as e:
    print(e)
