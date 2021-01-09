from threading import Thread


class Runnable(Thread):
    do_run = False

    def __init__(self, **kwargs):
        Thread.__init__(self)
        if kwargs is not None:
            self.__dict__.update(kwargs)
        self.do_run = True

    async def run(self) -> None:
        await self.on_start()
        while self.do_run:
            await self.work()
        await self.on_stop()

    async def stop(self):
        self.do_run = False

    async def on_start(self):
        pass

    async def on_stop(self):
        pass

    async def work(self):
        pass
