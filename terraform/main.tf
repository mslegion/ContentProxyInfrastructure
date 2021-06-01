provider "aws" {
  region = var.aws_region
}

resource "aws_security_group" "proxy" {
  name = "allow-proxy-connections"

  ingress {
    from_port   = var.server_port
    to_port     = var.server_port
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_security_group" "ssh" {
  name = "allow-ssh-connections"

  ingress {
    from_port   = var.ssh_port
    to_port     = var.ssh_port
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_security_group" "all_outbound" {
  name = "allow-all-outbound-connections"

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_key_pair" "deployer" {
  key_name   = var.key_pair_name
  public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDDxPB9iOo3mlvBcLbvPXSWZZFskU4Ryv4ZuSuNeym406ZPcFdZw5WqjwMQvO6b3ga+ZMssjjv6wcImcaGT7gtnkWSN6SLv/ilFG19klcOne+1MjzNPpg/DZgdufnJhVa27c14I90NqEL9LqqJQzO1SP7umfkgcwg/dOR8P2oB4sgjzTGu5sJ1T18mmsqR1vWakp44JernQB5PktZPqWJydRaMp0ccbplirwXsoP75RC2oIb/j3cJTBnL1oNwZ/aT6C7gSH2GqMbUN9LzgKv9/tXGI46xvIKaVuodWsfvjkFoNYe1Ehaml/hT2WBpaiP80jZeFrUVb57lJ/dWRb5Kvb"
}

resource "aws_instance" "ubuntu_server" {
  ami = lookup(var.images, var.aws_region)
  instance_type = "t2.micro"
  key_name = aws_key_pair.deployer.key_name
  security_groups = [aws_security_group.proxy.name, aws_security_group.ssh.name, aws_security_group.all_outbound.name]

  tags = {
    Name = var.proxy_tag
  }
}