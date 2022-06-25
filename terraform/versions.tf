terraform {
  # provide your own terraform state storage details
  backend "remote" {
    organization = ""
    workspaces {
      name = ""
    }
  }
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.28.0"
    }
  }

  required_version = "0.15.2"
}
