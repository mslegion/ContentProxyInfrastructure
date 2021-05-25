variable "aws_region" {
  type    = string
  default = "us-east-2"
}

variable "images" {
  type = map(string)

  default = {
    us-east-2 = "ami-00399ec92321828f5"
  }
}

variable "server_port" {
  description = "The port the proxy server will use for web traffic"
  type        = number
  default     = 8080
}

variable "ssh_port" {
  description = "The ssh port"
  type        = number
  default     = 22
}
