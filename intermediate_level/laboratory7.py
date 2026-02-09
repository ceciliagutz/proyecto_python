# Modulo. Acceso a datos y ORM

from typing import List

from sqlalchemy import Float, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship


# Base
class Base(DeclarativeBase):
    pass


# Models


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)

    orders: Mapped[List["Order"]] = relationship(back_populates="user")


class Order(Base):
    __tablename__ = "orders"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_ide: Mapped[int] = mapped_column(ForeignKey("users.id"))

    user: Mapped["User"] = relationship(back_populates="orders")
    items: Mapped[List["OrderItem"]] = relationship(back_populates="order")


class OrderItem(Base):
    __tablename__ = "order_items"
    id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"))

    product_name: Mapped[str] = mapped_column(String)
    price: Mapped[float] = mapped_column(Float)
    quantity: Mapped[int] = mapped_column(Integer)

    order: Mapped["Order"] = relationship(back_populates="items")


# Database setup
engine = create_engine("sqlite:///:memory:", echo=False)
Base.metadata.create_all(engine)


# CRUD
def create_sample_data(session: Session) -> None:
    user = User(name="Cecilia")
    order = Order(user=user)
    OrderItem(product_name="Light stick", price=1700, quantity=2, order=order)
    OrderItem(product_name="Cradle Light stick", price=550, quantity=2, order=order)

    session.add(user)
    session.commit()


def get_users(session: Session) -> List[User]:
    return session.query(User).all()


# Test

if __name__ == "__main__":
    with Session(engine) as session:
        create_sample_data(session)
        users = get_users(session)
        for user in users:
            print(f"User:{user.name}")
            for order in user.orders:
                for item in order.items:
                    print(f" - {item.product_name} x {item.quantity}")
