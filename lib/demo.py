#!/usr/bin/env python3
"""Small runnable demo of the CashRegister class.

Run from the project root with:  python lib/demo.py
"""

from cash_register import CashRegister


def main():
    # Open a register with a 20% discount.
    register = CashRegister(20)

    # Ring up a few items (item, price, optional quantity).
    register.add_item("laptop", 1000)
    register.add_item("mouse", 25, 2)
    print("items:", register.items)
    print("total:", register.total)

    # Void the most recent purchase (the 2 mice).
    register.void_last_transaction()
    print("after void -> total:", round(register.total, 2), " items:", register.items)

    # Apply the register's discount to whatever remains.
    register.apply_discount()
    print("final total:", register.total)


if __name__ == "__main__":
    main()
