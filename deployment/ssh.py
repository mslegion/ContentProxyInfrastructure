import time

import paramiko


def get_client():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    return client


class SSHClient:

    def __init__(self, private_key_file, host_name, username):
        self.private_key_file = private_key_file
        self.client = get_client()
        self.host_name = host_name
        self.username = username

    def connect(self):
        try:
            private_key = paramiko.RSAKey.from_private_key_file(self.private_key_file)
            self.client.connect(hostname=self.host_name, username=self.username, pkey=private_key)
        except Exception as e:
            raise Exception(f"Trouble connecting to server: {e}")

    def execute_command(self, cmd, prompt=None, timeout=5):
        stdin, stdout, stderr = self.client.exec_command(cmd)
        if prompt:
            stdin.write(f"{prompt}\n")
            stdin.flush()
            time.sleep(timeout)
        out, err = stdout.read().decode("utf-8"), stderr.read().decode("utf-8")
        return out, err

    def close(self):
        self.client.close()
