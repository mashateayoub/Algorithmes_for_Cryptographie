import UtilsAES


class AES:
    """
    Class for AES-128 encryption
    """

    def __init__(self, master_key):
        """
        Initializes the object with a given key.
        """
        assert len(master_key) == 16
        self.n_rounds = 10
        self._key_matrices = self._expand_key(master_key)

    def _expand_key(self, master_key):
        """
        Expands and returns a list of key matrices for the given master_key.
        """
        # Initialize round keys with raw key material.
        key_columns = UtilsAES.bytes2matrix(master_key)
        iteration_size = len(master_key) // 4

        i = 1
        while len(key_columns) < (self.n_rounds + 1) * 4:
            # Copy previous word.
            word = list(key_columns[-1])

            # Perform schedule_core once every "row".
            if len(key_columns) % iteration_size == 0:
                # Circular shift.
                word.append(word.pop(0))
                # Map to S-BOX.
                word = [UtilsAES.s_box[b] for b in word]
                # XOR with first byte of R-CON, since the others bytes of R-CON are 0.
                word[0] ^= UtilsAES.r_con[i]
                i += 1
            elif len(master_key) == 32 and len(key_columns) % iteration_size == 4:
                # Run word through S-box in the fourth iteration when using a
                # 256-bit key.
                word = [UtilsAES.s_box[b] for b in word]

            # XOR with equivalent word from previous iteration.
            word = UtilsAES.xor_bytes(word, key_columns[-iteration_size])
            key_columns.append(word)

        # Group key words in 4x4 byte matrices.
        return [key_columns[4 * i : 4 * (i + 1)] for i in range(len(key_columns) // 4)]

    def encrypt(self, plaintext):
        """
        Encrypts a single block of 16 byte long plaintext.
        """
        assert len(plaintext) == 16

        plain_state = UtilsAES.bytes2matrix(plaintext)

        UtilsAES.add_round_key(plain_state, self._key_matrices[0])

        for i in range(1, self.n_rounds):
            UtilsAES.sub_bytes(plain_state)
            UtilsAES.shift_rows(plain_state)
            UtilsAES.mix_columns(plain_state)
            UtilsAES.add_round_key(plain_state, self._key_matrices[i])

        UtilsAES.sub_bytes(plain_state)
        UtilsAES.shift_rows(plain_state)
        UtilsAES.add_round_key(plain_state, self._key_matrices[-1])

        return UtilsAES.matrix2bytes(plain_state)

    def decrypt(self, ciphertext):
        """
        Decrypts a single block of 16 byte long ciphertext.
        """
        assert len(ciphertext) == 16

        cipher_state = UtilsAES.bytes2matrix(ciphertext)

        UtilsAES.add_round_key(cipher_state, self._key_matrices[-1])
        UtilsAES.inv_shift_rows(cipher_state)
        UtilsAES.inv_sub_bytes(cipher_state)

        for i in range(self.n_rounds - 1, 0, -1):
            UtilsAES.add_round_key(cipher_state, self._key_matrices[i])
            UtilsAES.inv_mix_columns(cipher_state)
            UtilsAES.inv_shift_rows(cipher_state)
            UtilsAES.inv_sub_bytes(cipher_state)

        UtilsAES.add_round_key(cipher_state, self._key_matrices[0])

        return UtilsAES.matrix2bytes(cipher_state)
