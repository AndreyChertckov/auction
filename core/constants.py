class AuctionStatus:
    """
    All posible statuses of the auction
    """

    ACTIVE = 1
    FINISHED = 0

    CHOICES = (
        (ACTIVE, "Active"),
        (FINISHED, "Finished"),
    )
