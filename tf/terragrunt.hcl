# Assume role to security account
iam_role = "arn:aws:iam::107483165697:role/intelematics/Administrator"

inputs = {
  environment = "dev-alfonso"
}

remote_state {
  backend = "s3"
  config = {
    bucket                          = "107483165697-tfstate"
    dynamodb_table                  = "107483165697-tfstate-locktable"
    region                          = "ap-southeast-2"
    key                             = "cognito-customer-identity"
    skip_bucket_accesslogging       = true
    skip_bucket_root_access         = true
  }
}
