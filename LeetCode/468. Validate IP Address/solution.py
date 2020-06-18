# class Solution:
#     def ip4(self, item):
#         if len(item) > 3 or len(item) == 0 or (item[0] == '0' and len(item) > 1):
#             return False
#         sums = 0
#         for i in item:
#             if i < '0' or i > '9':
#                 return False
#             sums *= 10
#             sums += ord(i)-ord('0')
#         if sums >= (1<<8):
#             return False
#         return True

#     def ip6(self, item):
#         if len(item) > 4 or len(item) == 0:
#             return False
#         sums = 0
#         for i in item.lower():
#             sums *= 16
#             if '0' <= i <= '9':
#                 sums += ord(i)-ord('0')
#             elif 'a' <= i <= 'f':
#                 sums += ord(i)-ord('a')+10
#             else:
#                 return False
#         if sums >= (1<<16):
#             return False
#         return True



#     def validIPAddress(self, IP: str) -> str:
#         if '.' in IP:
#             items = IP.split('.')
#             if len(items) != 4:
#                 return 'Neither'
#             if any(not self.ip4(item) for item in  items):
#                 return 'Neither'
#             return 'IPv4'
#         else:
#             items = IP.split(':')
#             if len(items) != 8:
#                 return 'Neither'
#             if any(not self.ip6(item) for item in items):
#                 return "Neither"
#             return 'IPv6'


class Solution:
    def validIPAddress(self, IP):
            
            def isIPv4(s):
                try: return str(int(s)) == s and 0 <= int(s) <= 255
                except: return False
                
            def isIPv6(s):
                if len(s) > 4: return False
                try: return int(s, 16) >= 0 and s[0] != '-'
                except: return False

            if IP.count(".") == 3 and all(isIPv4(i) for i in IP.split(".")): 
                return "IPv4"
            if IP.count(":") == 7 and all(isIPv6(i) for i in IP.split(":")): 
                return "IPv6"
            return "Neither"