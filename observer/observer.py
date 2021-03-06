from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List, Optional


class Subject(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def attach(self, o: Observer) -> None:
        """Attach an observer to the subject"""
        ...

    @abstractmethod
    def detach(self, o: Observer) -> None:
        """Detach an observer from the subject"""
        ...

    @abstractmethod
    def notify(self) -> None:
        """Notify all observer about an event"""
        ...


class ConcreteSubject(Subject):
    """The Subject ows some important state and notifies observers when the
    state changes"""

    _state: Optional[int] = None
    """
    For the sake of simplicity, the Subject's state, essential to all
    subscribers, is stored in this variable.
    """

    _observers: List[Observer] = []

    """
    List of subscribers. In real life, the list of subscribers can be stored
    more comprehensively (categorized by event type, etc.)
    """
    @property
    def state(self) -> Optional[int]:
        return self._state

    def attach(self, o: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(o)

    def detach(self, o: Observer) -> None:
        self._observers.remove(o)

    """
    the subscription management methods.
    """

    def notify(self) -> None:
        """
        Trigger an update in each subscriber.
        """

        print("Subject: Notifying observers...")
        for observers in self._observers:
            observers.update(self)

    def some_business_logic(self) -> None:
        """
        Usually, the subscription logic is only a fraction of what a Subject
        can really do. Subject commonly hold some important business logic,
        that triggers a notification method whenever something important is
        about to happen (or after it).
        """

        print("\nSubject: I'm doing something important.")
        self._state = randrange(0, 10)

        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()


class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        Receive update from subject.
        """
        ...

    """
    Concrete Observers react to the updates issued by the Subject they had been
    attach to.
    """


def main():

    class ConcreteObserverA(Observer):
        def update(self, subject: Subject) -> None:
            if subject.state < 3:
                print("ConcreteObserverA: React to the event")

    class ConcreteObserverB(Observer):
        def update(self, subject: Subject) -> None:
            if subject.state == 0 or subject.state >= 2:
                print("ConcreteObserverB: React to the event")

    subject = ConcreteSubject()

    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    subject.some_business_logic()
    subject.some_business_logic()

    subject.detach(observer_a)

    subject.some_business_logic()


if __name__ == "__main__":
    main()
