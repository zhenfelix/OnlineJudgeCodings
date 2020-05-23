# class Solution:
#     def isNumber(self, s: str) -> bool:
#         INVALID, SPACE, DIGIT, SIGN, DOT, EXP = 0, 1, 2, 3, 4, 5
#         transfer = [[-1,0,2,1,9,-1],
#                     [-1,-1,2,-1,9,-1],
#                     [-1,8,2,-1,3,4],
#                     [-1,8,5,-1,-1,4],
#                     [-1,-1,7,6,-1,-1],
#                     [-1,8,5,-1,-1,4],
#                     [-1,-1,7,-1,-1,-1],
#                     [-1,8,7,-1,-1,-1],
#                     [-1,8,-1,-1,-1,-1],
#                     [-1,-1,3,-1,-1,-1]
#                    ]
#         state = 0
#         for ch in s:
#             transit = INVALID
#             if ch == ' ':
#                 transit = SPACE
#             elif ord(ch) >= ord('0') and ord(ch) <= ord('9'):
#                 transit = DIGIT
#             elif ch in ['+', '-']:
#                 transit = SIGN
#             elif ch == '.':
#                 transit = DOT
#             elif ch in ['e', 'E']:
#                 transit = EXP
#             else:
#                 pass
#             state = transfer[state][transit]
#             if state == -1:
#                 return False
#         return state in [2,3,5,7,8]

class Solution(object):
  def isNumber(self, s):
      """
      :type s: str
      :rtype: bool
      """
      #define a DFA
      state = [{}, 
              {'blank': 1, 'sign': 2, 'digit':3, '.':4}, 
              {'digit':3, '.':4},
              {'digit':3, '.':5, 'e':6, 'blank':9},
              {'digit':5},
              {'digit':5, 'e':6, 'blank':9},
              {'sign':7, 'digit':8},
              {'digit':8},
              {'digit':8, 'blank':9},
              {'blank':9}]
      currentState = 1
      for c in s:
          if c >= '0' and c <= '9':
              c = 'digit'
          if c == ' ':
              c = 'blank'
          if c in ['+', '-']:
              c = 'sign'
          if c not in state[currentState].keys():
              return False
          currentState = state[currentState][c]
      if currentState not in [3,5,8,9]:
          return False
      return True
    

class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        transfer = \
        [[2,-1,1,3],\
        [2,-1,-1,3],\
        [2,5,-1,4],\
        [4,-1,-1,-1],\
        [4,5,-1,-1],\
        [7,-1,6,-1],\
        [7,-1,-1,-1],\
        [7,-1,-1,-1]]
        state = 0
        for ch in s:
            col = -1
            if '0' <= ch <= '9':
                col = 0
            elif ch == 'e':
                col = 1
            elif ch in "+-":
                col = 2
            elif ch == '.':
                col = 3
            if col == -1:
                return False
            state = transfer[state][col]
            if state == -1:
                return False
        if state in [2,4,7]:
            return True
        return False


# return s.matches("(\\s*)[+-]?((\\.[0-9]+)|([0-9]+(\\.[0-9]*)?))(e[+-]?[0-9]+)?(\\s*)");
# https://zhuanlan.zhihu.com/p/20042325



# class Solution:
#     # @param {string} s
#     # @return {boolean}
#     def isNumber(self, s):
#         INVALID=0; SPACE=1; SIGN=2; DIGIT=3; DOT=4; EXPONENT=5;
#         #0invalid,1space,2sign,3digit,4dot,5exponent,6num_inputs
#         transitionTable=[[-1,  0,  3,  1,  2, -1],    #0 no input or just spaces 
#                          [-1,  8, -1,  1,  4,  5],    #1 input is digits 
#                          [-1, -1, -1,  4, -1, -1],    #2 no digits in front just Dot 
#                          [-1, -1, -1,  1,  2, -1],    #3 sign 
#                          [-1,  8, -1,  4, -1,  5],    #4 digits and dot in front 
#                          [-1, -1,  6,  7, -1, -1],    #5 input 'e' or 'E' 
#                          [-1, -1, -1,  7, -1, -1],    #6 after 'e' input sign 
#                          [-1,  8, -1,  7, -1, -1],    #7 after 'e' input digits 
#                          [-1,  8, -1, -1, -1, -1]]    #8 after valid input input space
#         state = 0
#         for c in s:
#             inputtype = INVALID
#             if c == ' ': inputtype = SPACE
#             elif c == '-' or c == '+': inputtype = SIGN
#             elif c.isdigit(): inputtype = DIGIT
#             elif c == '.': inputtype = DOT
#             elif c.upper() == 'E': inputtype = EXPONENT
#             state = transitionTable[state][inputtype]
#             if state == -1: return False
#         return state == 1 or state == 4 or state == 7 or state == 8
