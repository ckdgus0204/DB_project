import pymysql
 
# MySQL Connection 연결
conn = pymysql.connect(host='192.168.119.3',port=4567, user='root', password='data1234',db='bookstore', charset='utf8')
 
# Connection 으로부터 Cursor 생성
curs = conn.cursor()
c_id=1
while True:
    print("서점 DB")
    print("1. 로그인 2. 회원가입 3. 회원 전체 출력 4. 회원 검색 5. 회원 탈퇴 6. 회원 정보 변경 7. 책 찾기 8. 책 추가 9. 책 정보 변경 10. 책 삭제 11. ")
    
    a=int(input())
    # SQL문 실행
    if a==1:
        curs = conn.cursor()
        c_id=input()
        pw=input()

        sql = "select password from Customer where id=%s"
        curs.execute(sql,c_id)
        rs=curs.fetchall()
        if rs == pw:
            print('로그인성공')
        else:
            print('로그인실패')
        conn.close()

    elif a==2:
        curs = conn.cursor()
        print('ID:')
        c_id=input()
        print('name:')
        name=input()
        print('phone_number:')
        phone_number=int(input())
        print('address:')
        address=input()
        print('password:')
        password=input()

        sql ='insert into Customer values(%s,%s,%s,%s,%s)'
        curs.execute(sql,(c_id,name,phone_number,address,password))
        conn.commit()
        conn.close()

    elif a==3:
        sql = "select * from Customer"
        curs.execute(sql)
        rows = curs.fetchall()
        print(row)

    elif a==4:
        sql = "select * from Customer"
        curs.execute(sql)

    elif a==5:
        sql = "select * from Customer"
        curs.execute(sql)

    elif a==6:
        sql = "select * from Customer"
        curs.execute(sql)    
    elif a==6:
        sql = "select * from Customer"
        curs.execute(sql)
    elif a==6:
        sql = "select * from Customer"
        curs.execute(sql)




    # 데이타 Fetch

        # 전체 rows
    # print(rows[0])  # 첫번째 row: (1, '김정수', 1, '서울')
    # print(rows[1])  # 두번째 row: (2, '강수정', 2, '서울')
    
    # Connection 닫기
conn.close()