terraform {
  backend "remote" {
    organization = "saifsabir"
    workspaces {
      name = "portfolio"
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