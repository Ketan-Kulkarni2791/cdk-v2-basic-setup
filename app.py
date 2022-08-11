#!/usr/bin/env python3
import os
from configparser import ConfigParser, ExtendedInterpolation
import aws_cdk as cdk
from cdk_v2_basic_setup.cdk_v2_basic_setup_stack import CdkV2BasicSetupStack

def main() -> None:
    """main.py method that the cdk will execute."""
    config = ConfigParser(interpolation=ExtendedInterpolation())
    config.read("./config.ini")
    app = cdk.App()
    env = app.node.try_get_context("env")
    CdkV2BasicSetupStack(
        env_var=env,
        scope=app,
        app_id=config['global']['app-id'],
        config=config,
        env={
            "region": config['global']["region"],
            "account": config['global']['awsAccount']
        }
    )
    app.synth()
    
main()


