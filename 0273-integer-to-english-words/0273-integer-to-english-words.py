class Solution:
    def numberToWords(self, num: int) -> str:  
        if num == 0:
            return 'Zero'

        billion, million, thousand, hundred = 10 ** 9, 10 ** 6, 10 ** 3, 10 ** 2

        mapping = {
            0: '',
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine',
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen',
            20: 'Twenty',
            30: 'Thirty',
            40: 'Forty',
            50: 'Fifty',
            60: 'Sixty',
            70: 'Seventy',
            80: 'Eighty',
            90: 'Ninety',
            billion: 'Billion', 
            million: 'Million', 
            thousand: 'Thousand', 
            hundred: 'Hundred',
        }
        
        for unit in [billion, million, thousand, hundred]:
            if num >= unit:
                if num % unit:
                    return f"{self.numberToWords(num // unit)} {mapping[unit]} {self.numberToWords(num % unit)}"
                return f"{self.numberToWords(num // unit)} {mapping[unit]}"

        res = ''
        for i in range(99, 0, -1):
            if num // i > 0 and i in mapping:
                res = f"{mapping[i]} {mapping[num % i]}".strip()
                break
        return res 