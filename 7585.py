while True:
    printed=False
    s=input()
    if s=='#':break
    st=[-1]
    for i in s:
        if i=='(':
            st.append(0)
        elif i==')':
            if st[-1]!=0:
                print('Illegal')
                printed=True
                break
            else:
                st.pop()
        
            
        elif i=='{':
            st.append(1)
        elif i=='}':
            if st[-1]!=1:
                print('Illegal')
                printed=True
                break
            else:
                st.pop()
        elif i=='[':
            st.append(2)
        elif i==']':
            if st[-1]!=2:
                print('Illegal')
                printed=True
                break
            else:
                st.pop()
    if not printed and len(st)!=1:
        printed=True
        print('Illegal')
    if not printed:print('Legal')
