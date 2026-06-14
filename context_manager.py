import json
import os


class ContextManager:

    def __init__(self):

        self.file_name = "context.json"

        self.context = {}

        self.load()

    def load(self):

        if os.path.exists(
            self.file_name
        ):

            with open(
                self.file_name,
                "r",
                encoding="utf-8"
            ) as file:

                self.context = json.load(
                    file
                )

    def save(self):

        with open(
            self.file_name,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                self.context,
                file,
                indent=4
            )

    def update_context(
        self,
        key,
        value
    ):

        self.context[
            key.lower()
        ] = value

        self.save()

    def get_context(
        self,
        key
    ):

        return self.context.get(
            key.lower()
        )

    def get_all_context(self):

        return self.context