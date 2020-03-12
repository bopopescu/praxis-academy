class TestApi(Api):
    def fetch_remote_data(self):
        print('Demo Api called')
        return 24

        class TestAppModule(Module):

    @singleton
    @provider
    def provide_api(self) -> Api:
        return TestApi()

        if __name__ == '__main__':
    real_injector = Injector(AppModule())
    test_injector = Injector([AppModule(), TestAppModule()])

    real_logic = real_injector.get(BusinessLogic)
    real_logic.do_stuff()

    test_logic = test_injector.get(BusinessLogic)
    test_logic.do_stuff()