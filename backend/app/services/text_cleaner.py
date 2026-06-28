class TextCleaner:
    def clean(self, text: str) -> str:
        lines = text.splitlines()

        cleaned_lines = []
        previous_blank = False

        for line in lines:
            stripped = line.strip()

            if stripped == "":
                if previous_blank:
                    continue
                previous_blank = True
            else:
                previous_blank = False

            cleaned_lines.append(stripped)

        return "\n".join(cleaned_lines).strip()