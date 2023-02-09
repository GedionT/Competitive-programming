class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        def backtrack(start):
            if len(octets) == 4 and start == len(s):
                valid_ip.append(".".join(octets))
                return
            
            for size in range(1, 4):
                octet = s[start : start+size]
                
                if len(octet) > 1 and (octet[0] == '0' or int(octet) > 255):
                    continue
                    
                if len(octets) < 4:
                    octets.append(octet)
                    backtrack(start + size)
                    octets.pop()
                    
        octets = []
        valid_ip = []

        backtrack(0)

        return valid_ip