from django.db.models import QuerySet

from db.models import Order, User, MovieSession, Ticket


def create_order(tickets: list, username: str, date: int = None) -> None:
    created_order = Order.objects.create(
        user=User.objects.get(username=username),
        created_at=date if date else None
    )
    for ticket_data in tickets:
        Ticket.objects.create(
            order=created_order,
            row=ticket_data["row"],
            seat=ticket_data["seat"],
            movie_session=MovieSession.objects.get(
                id=ticket_data["movie_session"])
        )


def get_orders(username: str = None, ) -> QuerySet:
    if username:
        return Order.objects.all().filter(user__username=username)
    return Order.objects.all()
