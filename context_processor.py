from context_manager import (
    ContextManager
)


manager = ContextManager()

print(
    "\n======================"
)

print(
    "    CONTEXT ENGINE"
)

print(
    "======================"
)

while True:

    command = input(
        "\n> "
    )

    if command.lower() == "exit":

        break

    if "=" in command:

        key, value = (
            command.split(
                "=",
                1
            )
        )

        manager.update_context(
            key.strip(),
            value.strip()
        )

        print(
            "\n✓ Context Updated"
        )

    elif command.lower() == "show":

        print(
            "\nCurrent Context:\n"
        )

        for key, value in (
            manager
            .get_all_context()
            .items()
        ):

            print(
                f"{key}: {value}"
            )

    else:

        result = (
            manager
            .get_context(
                command
            )
        )

        if result:

            print(
                f"\n{command}: "
                f"{result}"
            )

        else:

            print(
                "\nNo Context Found"
            )