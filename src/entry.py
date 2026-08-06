from workers import Response, WorkerEntrypoint


class Default(WorkerEntrypoint):
    async def fetch(self, request):
        await self.env.MY_QUEUE.send("Hello avioforse!")
        return Response("Sent!")
