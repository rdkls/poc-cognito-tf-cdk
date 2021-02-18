resource "aws_cognito_user_pool_domain" "main" {
  domain       = "intelematics"
  user_pool_id = aws_cognito_user_pool.customer.id
}

resource "aws_cognito_user_pool" "customer" {
  name = "customer"
}
