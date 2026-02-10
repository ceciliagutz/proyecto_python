from typing import Dict, Optional, Protocol

# Domain model


class User:
    def __init__(self, user_id: int, name: str):
        self.user_id = user_id
        self.name = name

    def __repr__(self) -> str:
        return f"User(id={self.user_id}, name '{self.name}')"


# Port (Protocol)


class UserRepository(Protocol):
    def add(self, user: User) -> None: ...
    def get(self, user_id: int) -> Optional[User]: ...


# Service


class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def register_user(self, user_id: int, name: str) -> User:
        user = User(user_id, name)
        self.repo.add(user)
        return user

    def get_user(self, user_id: int) -> Optional[User]:
        return self.repo.get(user_id)


# In-memory implementation


class InMemoryUserRepository:
    def __init__(self):
        self.users: Dict[int, User] = {}

    def add(self, user: User) -> None:
        self.users[user.user_id] = user

    def get(self, user_id: int) -> Optional[User]:
        return self.users.get(user_id)


# Fake SQL implementation


class SQLUserRepository:
    def __init__(self):
        self._table: Dict[int, User] = {}

    def add(self, user: User) -> None:
        print("Saving user to SQL database")
        self._table[user.user_id] = user

    def get(self, user_id: int) -> Optional[User]:
        print("Fetching user from SQL database")
        return self._table.get(user_id)


# LSP demostration
def demo(service: UserService) -> None:
    service.register_user(1, "Cecilia")
    user = service.get_user(1)
    print(user)


if __name__ == "__main__":
    print("Using InMemory repository:")
    memory_repo = InMemoryUserRepository()
    service1 = UserService(memory_repo)
    demo(service1)

    print("\nUsing SQL repository:")
    sql_repo = SQLUserRepository()
    service2 = UserService(sql_repo)
    demo(service2)
