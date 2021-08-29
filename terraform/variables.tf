variable "aws_region" {
  type    = string
  default = "Ohio"
}

variable "proxy_tag" {
  type    = string
  default = "DjangoServer"
}

variable "images" {
  type = map(string)

  default = {
    us-east-2 = "ami-00399ec92321828f5" // Ohio
    eu-west-2 = "ami-0194c3e07668a7e36" // London
    ca-central-1 = "ami-0801628222e2e96d6" // Canada
    eu-north-1 = "ami-0ff338189efb7ed37" // Stockholm
    ap-northeast-1 = "ami-0df99b3a8349462c6" // Tokyo
    sa-east-1 = "ami-054a31f1b3bf90920" // SaoPaulo
    eu-central-1 = "ami-05f7491af5eef733a" // Germany
  }
}

variable "locations" {
  type = map(string)

  default = {
    Ohio = "us-east-2"
    London =  "eu-west-2"
    Canada = "ca-central-1"
    Stockholm = "eu-north-1"
    Tokyo = "ap-northeast-1"
    SaoPaulo = "sa-east-1"
    Germany = "eu-central-1"
  }
}

variable "server_port" {
  description = "The port that proxy server will use for web traffic"
  type        = number
  default     = 80
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