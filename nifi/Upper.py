from nifiapi.flowfiletransform import FlowFileTransform, FlowFileTransformResult

class Upper(FlowFileTransform):
    class Java:
        implements = ['org.apache.nifi.python.processor.FlowFileTransform']
    class ProcessorDetails:
        version = '2.0.0-M2'
        dependencies = ['numpy==1.20.0']

    def __init__(self, **kwargs):
        pass

    def transform(self, context, flowfile):
        import numpy as np
        result = flowfile.getContentsAsBytes().decode('utf-8').upper()
        return FlowFileTransformResult(relationship = "success", contents = result, attributes={"mime.type": "application/json"})

