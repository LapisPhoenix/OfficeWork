# TODO: Remake this to use curses instead.

from random import uniform
from time import sleep
from sys import stdout


class Typewriter:
    """Type like a human
    
    # Methods
      - backspace(length: int) -> None
        - Deletes a certain amount of characters
      - sentence(text: str, wpm: int) -> None
        - Writes a sentence with animation
      - paragraph(lines: list[str], wpm: int, delay: int | float) -> None
        - Writes a sentences one after the other, with a delay."""

    def _delay(self, wpm: int) -> float:
        calculated_delay_time_base = 1 / (wpm / 60)
        return 0.2 * uniform(calculated_delay_time_base * 0.9, calculated_delay_time_base * 1.1)

    def _write(self, string: str) -> None:
        for character in string:
            stdout.write(character)
        stdout.flush()

    def backspace(self, length: int) -> None:
        """Deletes a certain amount of characters"""
        for _ in range(length):
            self._write('\b \b')
            sleep(self._delay(300))

    def sentence(self, text: str, wpm: int) -> None:
        """Writes a sentence with animation"""
        for character in text:
            self._write(character)
            sleep(self._delay(wpm))

    def paragraph(self, lines: list[str], wpm: int, delay: int | float) -> None:
        """Writes a sentences one after the other, with a delay."""   
        for line in lines:
            self.sentence(line, wpm)

            sleep(delay)

            self.backspace(len(line))


if __name__ == "__main__":
    def tests(typewriter: Typewriter):
        sentences = [
            "She had a habit of taking showers in lemonade.",
            "He said he was not there yesterday; however, many people saw him there.",
            "Sarah ran from the serial killer holding a jug of milk.",
            "She was the type of girl who wanted to live in a pink house.",
            "She found his complete dullness interesting."
        ]

        wpm = 90
        delay = 1

        typewriter.paragraph(sentences, wpm, delay)

        typewriter.sentence(sentences[0], wpm)

    tw = Typewriter()

    tests(tw)