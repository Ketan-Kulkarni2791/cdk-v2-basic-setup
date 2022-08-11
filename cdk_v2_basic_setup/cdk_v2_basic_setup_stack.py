"""Main python file_key for adding resources to the application stack."""
import aws_cdk
from constructs import Construct
from typing import Dict, Any

from .iam_construct import IAMConstruct

class CdkV2BasicSetupStack(aws_cdk.Stack):
    """Build the app stacks and its resources."""
    def __init__(self, env_var: str, scope: Construct, 
                 app_id: str, config: dict, **kwargs: Dict[str, Any]) -> None:
        """Creates the cloudformation templates for the projects."""
        super().__init__(scope, app_id, **kwargs)
        self.env_var = env_var
        self.config = config
        CdkV2BasicSetupStack.create_stack(self, self.env_var, config=config)
        
        
    @staticmethod
    def create_stack(stack: aws_cdk.Stack, env: str, config: dict) -> None:
        """Create and add the resources to the application stack"""
        CdkV2BasicSetupStack.create_iam_user_infra(
            stack=stack, env=env, config=config
        )
        
    
    @staticmethod
    def create_iam_user_infra(
        stack: aws_cdk.Stack,
        env: str,
        config: dict) -> None:
        """Create IAM user and required attributes"""
        user = IAMConstruct.create_user(stack=stack)
        group = IAMConstruct.create_group(stack=stack)
        group.add_user(user)
        access_policy = IAMConstruct.create_managed_policy(
            stack=stack,
            policy_name="cdk-v2-basic-data-access-policy",
            statements=[
                IAMConstruct.get_access_key_mgmt_polict(stack=stack)
            ]
        )
        user.add_managed_policy(access_policy)
