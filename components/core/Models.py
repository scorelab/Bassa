from abc import ABC, abstractmethod

class User:
    def __init__(self, userName, password, auth, email):
        self.userName=userName
        self.password=password
        self.auth=auth
        self.email=email


class AuthLeval:
    ADMIN, STUDENT, ACADEMIC, NONACADEMIC= list(range(4))


class Download:
    def __init__(self, link, userName, id=None):
        self.link=link
        self.userName=userName
        self.id=id
        self.gid=None

    def __str__(self):
        return "id: %s, user: %s, link: %s, gid: %s" % (self.id, self.userName, self.link, self.gid)


class Status:

    DEFAULT, STARTED, DELETED, COMPLETED, ERROR= list(range(5))


class ACL:
    def __init_(self):
        self.user_id=user_id
        self.entity_type=entity_type
        self.entity_id=entity_id
        self.access=access


class EntityInterface(ABC):

    def get_all(self):
        """
        gets all entities of the parent.
        """

    @abstractmethod
    def create(self):
        """
        creates an entity to the parent.
        """

    @abstractmethod
    def delete(self):
        """
        deletes an entity from the parent.
        """

    @abstractmethod
    def update(self):
        """
        updates an entity of the parent.
        """

    @abstractmethod
    def get(self):
        """
        gets an entity of the parent.
        """

    @abstractmethod
    def move(self):
        """
        moves an entity from one parent to another.
        """
