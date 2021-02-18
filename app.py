#!/usr/bin/env python3

from aws_cdk import core

from cognito_customer_identity.cognito_customer_identity_stack import CognitoCustomerIdentityStack


app = core.App()
CognitoCustomerIdentityStack(app, "cognito-customer-identity")

app.synth()
