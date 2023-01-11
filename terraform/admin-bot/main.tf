terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "3.58.0"
    }
  }
}

output "submit_url" {
  value = module.admin_bot.submit_url
}

provider "google" {
  project = "idekctf-374221"
  region  = "us-east4"
}

module "admin_bot" {
  source    = "redpwn/admin-bot/google"
  image     = "gcr.io/idekctf-374221/admin-bot"
  recaptcha = {
    site   = "REDACTED"
    secret = "REDACTED"
  }
}
