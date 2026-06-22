#!/usr/bin/env python3


class CashRegister:
    """A simple cash register that tracks a running total, the items rung up,
    and a history of transactions so they can be discounted or voided."""

    def __init__(self, discount=0):
        # discount is an optional percentage off the total (0 by default).
        # Routing through the property setter validates the supplied value.
        self._discount = 0
        self.discount = discount
        # Running total of every item's price * quantity.
        self.total = 0
        # Flat list of item names (one entry per unit purchased).
        self.items = []
        # Receipt-style history used to apply discounts / void purchases.
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        # A discount must be a whole-number percentage between 0 and 100.
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    def add_item(self, item, price, quantity=1):
        """Ring up an item: grow the total, record one entry per unit in
        items, and log the purchase in previous_transactions."""
        self.total += price * quantity
        for _ in range(quantity):
            self.items.append(item)
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity,
        })

    def apply_discount(self):
        """Reduce the total by the discount percentage, or report that no
        discount is set."""
        if self.discount:
            self.total -= self.total * (self.discount / 100)
            # Drop the trailing decimal so the total prints as a whole dollar.
            self.total = int(self.total)
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        """Undo the most recent purchase, restoring the total and items, or
        report that there is nothing to void."""
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return
        last_transaction = self.previous_transactions.pop()
        # Subtract the voided purchase from the total (never below zero).
        self.total -= last_transaction["price"] * last_transaction["quantity"]
        if self.total < 0:
            self.total = 0.0
        # Remove the corresponding item entries so items stays accurate.
        for _ in range(last_transaction["quantity"]):
            self.items.remove(last_transaction["item"])
