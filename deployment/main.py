import ssh
import deployment.setup_handler as setup_handler

try:
    key_pair_name, host_name, user_name = setup_handler.get_aws_server_details()
    client = ssh.SSHClient(key_pair_name, host_name, user_name)
    client.connect()

    # setup_handler.update_get_tools(client)
    # setup_handler.clone_git_repository(client, "https://github.com/saifsabir97/Proxy-Server.git")
    # setup_handler.install_maven(client)
    setup_handler.run_application(client, "Proxy-Server")
    # setup_handler.kill_application(client)

    client.close()
except Exception as e:
    print(e)
