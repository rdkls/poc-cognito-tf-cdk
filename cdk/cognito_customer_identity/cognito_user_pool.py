from aws_cdk import aws_cognito as cognito, cdk
from aws_cdk import core


class CognitoCustomerPool(core.Construct):
    def __init__(self, scope: core.Construct, id: str) -> None:
        super().__init__(scope, id)

        # Create chat room user pool
        customer_pool = cognito.CfnUserPool(
            self,
            "UserPool",
            admin_create_user_config={"allowAdminCreateUserOnly": False},
            policies={"passwordPolicy": {"minimumLength": 6, "requireNumbers": False}},
            schema=[{"attributeDataType": "String", "name": "email", "required": True}],
            auto_verified_attributes=["email"],
        )

        # Now for the client
        cognito.CfnUserPoolClient(
            self,
            "UserPoolClient",
            client_name="IntelematicsCustomerAuthClient",
            explicit_auth_flows=["ADMIN_NO_SRP_AUTH"],
            refresh_token_validity=30,
            user_pool_id=customer_pool.ref,
        )
