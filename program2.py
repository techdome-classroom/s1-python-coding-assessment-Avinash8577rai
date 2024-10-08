def decode_message( s: str, p: str) -> bool:

# write your code here
        m,n = len(s), len(p)
        
        table = [[False]*(n+1) for _ in range(m+1)]
        
        #Base Case
        table[0][0]=True
        
        for j in range(1,n+1):
                if p[j-1]=='*':
                        table[0][j]=table[0][j-1]
                        
        for i in range(1,m+1):
                for j in range(1,n+1):
                        if p[j-1]==s[i-1] or p[j-1]=='?':
                                table[i][j]=table[i-1][j-1]
                        elif p[j-1]=='*':
                                table[i][j]=table[i][j-1] or table[i-1][j]
        return table[m][n]