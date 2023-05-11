#!/usr/bin/env python
from constructs import Construct
from cdk8s import App, Chart

from webservice import WebService   

class MyChart(Chart):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        WebService(self, 'hello', image='paulbower/hello-kubernetes:1.7', replicas=2)
        WebService(self, 'ghost', image='ghost', container_port=2368)

app = App()
MyChart(app, "cdk8s")

app.synth()
