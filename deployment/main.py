import ssh
import deployment.setup_handler as setup_handler

try:
    key_pair_name, host_name, user_name = setup_handler.get_aws_server_details()
    github_token = setup_handler.get_github_token()
    client = ssh.SSHClient(key_pair_name, host_name, user_name)
    client.connect()

    setup_handler.update_get_tools(client)
    setup_handler.install_docker(client)
    setup_handler.clone_git_repository(client, f"https://{github_token}@github.com/saifsabir97/portfolio.git")
    setup_handler.run_docker_app(client, "portfolio")

    client.close()
except Exception as e:
    print(e)
