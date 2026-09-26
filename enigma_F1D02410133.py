import string

ALPHABET = string.ascii_uppercase

ROTORS = {
    "I": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
    "II": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
    "III": "BDFHJLCPRTXVZNYEIWGAKMUSQO"
}

NOTCHES = {
    "I": "Q",
    "II": "E",
    "III": "V"
}

REFLECTOR_B = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

CIPHERTEXT = (
    "IGSLGGHXWYRZGSHUCOHYXGCPJKYVVFDZIBYNXYFFSJ"
)


class Rotor:
    def __init__(self, name, ring_setting, position):
        self.name = name
        self.wiring = ROTORS[name]

        self.ring = ALPHABET.index(ring_setting)
        self.position = ALPHABET.index(position)

        self.notch = ALPHABET.index(NOTCHES[name])

    def forward(self, signal):
        index = (
            signal
            + self.position
            - self.ring
        ) % 26

        output = ALPHABET.index(
            self.wiring[index]
        )

        return (
            output
            - self.position
            + self.ring
        ) % 26

    def backward(self, signal):
        index = (
            signal
            + self.position
            - self.ring
        ) % 26

        wiring_index = self.wiring.index(
            ALPHABET[index]
        )

        return (
            wiring_index
            - self.position
            + self.ring
        ) % 26


class Enigma:
    def __init__(self):

        self.right = Rotor("II", "P", "L")
        self.middle = Rotor("III", "M", "G")
        self.left = Rotor("I", "H", "F")

        self.plugboard = {
            "R": "X",
            "X": "R",
            "G": "A",
            "A": "G"
        }

    def plug(self, signal):
        letter = ALPHABET[signal]

        if letter in self.plugboard:
            letter = self.plugboard[letter]

        return ALPHABET.index(letter)

    def step_rotors(self):

        right_at_notch = (
            self.right.position ==
            self.right.notch
        )

        middle_at_notch = (
            self.middle.position ==
            self.middle.notch
        )

        if middle_at_notch:
            self.left.position = (
                self.left.position + 1
            ) % 26

            self.middle.position = (
                self.middle.position + 1
            ) % 26

        elif right_at_notch:
            self.middle.position = (
                self.middle.position + 1
            ) % 26

        self.right.position = (
            self.right.position + 1
        ) % 26

    def encrypt_character(self, character):

        self.step_rotors()

        signal = ALPHABET.index(character)
        signal = self.plug(signal)
        signal = self.right.forward(signal)
        signal = self.middle.forward(signal)
        signal = self.left.forward(signal)

        signal = ALPHABET.index(
            REFLECTOR_B[signal]
        )

        signal = self.left.backward(signal)
        signal = self.middle.backward(signal)
        signal = self.right.backward(signal)

        signal = self.plug(signal)

        return ALPHABET[signal]

    def decrypt(self, ciphertext):

        plaintext = ""

        for character in ciphertext:
            plaintext += self.encrypt_character(
                character
            )

        return plaintext


machine = Enigma()
plaintext = machine.decrypt(CIPHERTEXT)
print("Ciphertext:")
print(CIPHERTEXT)
print("\nPlaintext:")
print(plaintext)