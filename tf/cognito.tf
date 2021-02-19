resource "aws_cognito_user_pool_domain" "main" {
  domain       = "intelematics"
  user_pool_id = aws_cognito_user_pool.customer.id
}

resource "aws_cognito_user_pool" "customer" {
  name = "customer"

  mfa_configuration = "ON"
  software_token_mfa_configuration {
    enabled = true
  }

  account_recovery_setting {
    recovery_mechanism {
      name     = "verified_email"
      priority = 1
    }

    recovery_mechanism {
      name     = "verified_phone_number"
      priority = 2
    }
  }

  password_policy {
    minimum_length    = 6
    require_lowercase = false
    require_uppercase = false
    require_symbols = false
    require_numbers = false
  }
}
