# sheldon woodward
# 5/10/18


class Crpyto:
    def __init__(self, w_0, w_1, w_2):
        self.stack = {}
        self.word = ''
        word_length = 0
        if len(w_0) > word_length:
            word_length = len(w_0)
        if len(w_1) > word_length:
            word_length = len(w_1)
        if len(w_2) > word_length:
            word_length = len(w_2)

        w_0 = w_0[::-1]
        w_1 = w_1[::-1]
        w_2 = w_2[::-1]
        for i in range(word_length - len(w_0)):
            w_0 += ' '
        for i in range(word_length - len(w_1)):
            w_1 += ' '
        for i in range(word_length - len(w_2)):
            w_2 += ' '

        for a, b, c in zip(w_0, w_1, w_2):
            self.word += a
            self.word += b
            self.word += c

        self.stack[' '] = 0

    def solve(self):
        # print(self.word)
        self._recursive(0)

    def _recursive(self, index, carry=0):
        # print(str(self.stack) + ' ' + str(index))
        if not index < len(self.word) and carry == 0:
            print(self._without_space())
            return False
        if not index < len(self.word):
            return False

        let = self.word[index]
        new_carry = 0

        if let not in self.stack:
            if index % 3 != 2:
                for val in range(10):
                    if val not in self._without_space().values():
                        self.stack[let] = val
                        # print('push: ' + str(self.stack))
                        if self._recursive(index + 1, carry):
                            return True
                        else:
                            self.stack.pop(list(self.stack.keys())[-1])
                            # print(' pop: ' + str(self.stack))
                else:
                    return False

            else:
                val = self.stack[self.word[index - 2]] + self.stack[self.word[index - 1]] + carry
                if val > 9:
                    # print('CARRY: ' + str(val))
                    new_carry = int(val / 10)
                    val = val % 10
                if val not in self.stack.values():
                    self.stack[let] = val
                    # print('push: ' + str(self.stack))
                    if self._recursive(index + 1, new_carry):
                        return True
                    else:
                        self.stack.pop(list(self.stack.keys())[-1])
                        # print(' pop: ' + str(self.stack))
                        return False
                else:
                    return False

        else:
            if index % 3 != 2:
                if self._recursive(index + 1, carry):
                    return True
                else:
                    return False

            else:
                val = self.stack[self.word[index - 2]] + self.stack[self.word[index - 1]] + carry
                if val > 9:
                    # print('CARRY: ' + str(val))
                    new_carry = int(val / 10)
                    val = val % 10
                if val == self.stack[let]:
                    if self._recursive(index + 1, new_carry):
                        return True
                    else:
                        return False
                else:
                    return False

    def _without_space(self):
        r = dict(self.stack)
        del r[' ']
        return r
