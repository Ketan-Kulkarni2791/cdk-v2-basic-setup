"""Module to hold helper methods for CDK IAM creation"""
from typing import Dict, Any, List
from aws_cdk import Stack
import aws_cdk.aws_iam as iam

class IAMConstruct:
    """Class holds methods for IAM resource creation"""
    
    @staticmethod
    def create_group(
        stack: Stack) -> None:
        """Group for CDK Basic Setup IAM user"""
        user_group = iam.Group(
            scope=stack,
            id="cdk-v2-basic-group-id",
            group_name="cdk-v2-basic-iam-group"
        )
        return user_group
    
    @staticmethod
    def create_user(
        stack: Stack) -> None:
        """Create user utilized for CDK Basic Setup data access"""
        user = iam.User(
            scope=stack,
            id="cdk-v2-basic-user-id",
            user_name="cdk-v2-basic-iam-user"
        )
        return user
    
    @staticmethod
    def create_managed_policy(stack: Stack, policy_name: str,
                              statements: List[iam.PolicyStatement]) -> iam.PolicyStatement:
        """Create managed policy for IAM users"""
        policy = iam.ManagedPolicy(
            scope=stack,
            id=f"{policy_name}-id",
            statements=statements
        )
        return policy
    
    @staticmethod
    def get_access_key_mgmt_polict(stack: Stack) -> iam.PolicyStatement:
        """To generate secrets using secrets admin role, below permissions needed."""
        policy_statement = iam.PolicyStatement()
        policy_statement.effect = iam.Effect.ALLOW
        policy_statement.add_actions("iam:DeleteAccessKey")
        policy_statement.add_actions("iam:GetAccessKeyLastUsed")
        policy_statement.add_actions("iam:UpdateAccessKey")
        policy_statement.add_actions("iam:CreateAccessKey")
        policy_statement.add_actions("iam:ListAccessKey")
        policy_statement.add_resources(
            f"arn:aws:iam::{stack.account}:user/${{aws:username}}"
        )
        policy_statement.add_resources(
            f"arn:aws:iam::{stack.account}:user/cdk_basic/${{aws:username}}"
        )
        return policy_statement