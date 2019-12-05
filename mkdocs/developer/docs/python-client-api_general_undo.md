# undo

**undo(transaction\_ticket=None, transaction\_id=None, ignore\_files=False)**

undo an operation. If no transaction id is given, then the last
operation of this user on this project is undone

**keyparam:**

**transaction\_ticket** - explicitly undo a specific transaction

**transaction\_id** - explicitly undo a specific transaction by id

**ignore\_files** - flag which determines whether the files should

also be undone. Useful for large preallcoated checkins.
