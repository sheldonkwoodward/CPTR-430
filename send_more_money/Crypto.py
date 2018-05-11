# sheldon woodward
# 5/10/18


class Crpyto:
    def __init__(self, w_0, w_1, w_2):
        self.stack = {}
        self.word = ''
        for i in range(len(w_0)):
            # TODO: make this universal
            self.word += w_2[i] + w_1[i] + w_0[i]
        self.word = self.word[::-1]

    def solve(self):
        print(self.word)
        self._recursive(0)

    def _recursive(self, index, carry=0):
        # print(str(self.stack) + ' ' + str(index))
        if not index < len(self.word) and carry == 0:
            print(self.stack)
            return True
        if not index < len(self.word):
            return False

        let = self.word[index]
        new_carry = 0

        if let not in self.stack:
            if index % 3 != 2:
                for val in range(10):
                    if val not in self.stack.values():
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
