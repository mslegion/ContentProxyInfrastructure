import ssh
import deployment.setup_handler as setup_handler

try:
    key_pair_name, host_name, user_name = setup_handler.get_aws_server_details()
    client = ssh.SSHClient(key_pair_name, host_name, user_name)
    client.connect()

    # setup_handler.update_get_tools(client)
    # setup_handler.install_docker(client)
    # setup_handler.delete_directory(client, "sitevisitor")
    # setup_handler.clone_git_repository(client, "https://github.com/mslegion/sitevisitor.git")
    # set up info token in remote
    # setup_handler.run_docker_app(client, "sitevisitor")

    client.close()
except Exception as e:
    print(e)
