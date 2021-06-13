variable "aws_region" {
  type    = string
  default = "eu-west-2"
}

variable "proxy_tag" {
  type    = string
  default = "ProxyServer"
}

variable "images" {
  type = map(string)

  default = {
    us-east-2 = "ami-00399ec92321828f5" // Ohio
    eu-west-2 = "ami-0194c3e07668a7e36" // London
  }
}

variable "server_port" {
  description = "The port that proxy server will use for web traffic"
  type        = number
  default     = 8080
}

variable "ssh_port" {
  description = "The ssh port"
  type        = number
  default     = 22
}

variable "key_pair_name" {
  description = "The ssh key pair name used to connect to server"
  type = string
  default = "ubuntu_server_kp"
}