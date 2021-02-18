from aws_cdk import core
from cognito_user_pool import CognitoCustomerPool


class CognitoCustomerIdentityStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        CognitoCustomerPool(self, "UserPool")
