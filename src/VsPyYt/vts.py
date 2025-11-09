import asyncio
import PyTubeStudio.client as pts
import VtsModels.models as models

vts = pts.PyTubeStudio()

async def connect():
    await vts.connect()
    await vts.authenticate()
    answer = await vts.request(models.APIStateRequest())
    print(answer)
    await vts.close()

def connect_vtube_studio():
    asyncio.run(connect())

async def send_request_async(id, value):
    await vts.request(models.InjectParameterDataRequest(
        data=models.InjectParameterDataRequestData(
            parameter_values=[
                models.ParameterValue(
                    id=id,
                    value=value
                )
            ]
        )
    ))

def send_request(id, value):
    asyncio.run(send_request_async(id, value))