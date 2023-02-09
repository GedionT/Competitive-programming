class Solution:
    def reformatDate(self, date: str) -> str:
        
        monthToNum = {
            "Jan": '01',
            "Feb": '02',
            "Mar": '03',
            "Apr": '04',
            "May": '05',
            "Jun": '06',
            "Jul": '07',
            "Aug": '08',
            "Sep": '09',
            "Oct": '10',
            "Nov": '11',
            "Dec": '12'
        }
        
        date, month, year = date.split(" ")
        
        date = date[:-2]
        if len(date) == 1:
            date = '0'+date
        
        month = monthToNum[month]
        
        return f'{year}-{month}-{date}'