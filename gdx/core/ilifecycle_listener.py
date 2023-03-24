from abc import ABC, abstractmethod


# A LifecycleListener can be added to an Application via
# Application.addLifecycleListener(LifecycleListener). It will receive
# notification of pause, resume and dispose events. This is mainly meant
# to be used by extensions that need to manage resources based on the
# life-cycle. Normal, application level development should rely on the
# ApplicationListener interface. The methods will be invoked on the
# rendering thread. The methods will be executed before the ApplicationListener
# methods are executed.
class ILifecycleListener(ABC):

    @abstractmethod
    def pause(self):
        pass

    @abstractmethod
    def resume(self):
        pass

    @abstractmethod
    def dispose(self):
        pass
