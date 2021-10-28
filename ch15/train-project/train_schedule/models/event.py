# train-project/train_schedule/models/event.py
class Event:
    """This class implements a callback mechanism for our models.

    A model can define an event by creating an `Event` instance
    attribute. Any objects that need to respond to event, can
    register callbacks using the `bind` method. When the model
    calls `emit` on the event, the callbacks will be invoked with
    any arguments passed to the `emit` method.
    """

    def __init__(self):
        self.callbacks = []

    def bind(self, listener):
        """Bind a callback to the event"""
        self.callbacks.append(listener)

    def emit(self, *args, **kwargs):
        """Emit the event"""
        for callback in self.callbacks:
            callback(*args, **kwargs)
