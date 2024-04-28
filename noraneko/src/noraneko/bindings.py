from blacksheep import FromHeader


class FromLastEventIDHeader(FromHeader[str | None]):
    name = "Last-Event-ID"


class FromIDHeader(FromHeader[str]):
    name = "Client-ID"
