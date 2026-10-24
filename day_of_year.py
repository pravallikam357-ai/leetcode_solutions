class Solution:
    def dayOfYear(self, date: str) -> int:
        y,m,d=map(int,date.split("-"))
        a=0
        m_d=[31,28,31,30,31,30,31,31,30,31,30,31]
        if y%400==0 or (y%4==0 and y%100!=0):
            m_d[1]=29
        else:
            m_d[1]=28
        for i in range(m-1):
            a=a+m_d[i]
        f=a+d  
        return f
