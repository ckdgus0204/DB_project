import pymysql
 
# MySQL Connection 연결
 
# Connection 으로부터 Cursor 생성

login_id=''
login=False
while True:
    print("서점 DB")
    print("1. 로그인 2. 회원가입 3. 회원 전체 출력 4. 회원 검색 5. 회원 탈퇴 6. 회원 정보 변경 7. 책 찾기 8. 책 추가 9. 책 정보 변경 10. 책 삭제 11. ")
    
    a=int(input())
    # SQL문 실행
    if a==1:
        conn = pymysql.connect(host='192.168.119.3',port=4567, user='root', password='data1234',db='bookstore', charset='utf8')
        curs = conn.cursor()
        print('id:')
        c_id=input()
        print('password:')
        pw=input()

        sql = "select password from Customer where id=%s"
        curs.execute(sql,(c_id))
        rs=curs.fetchone()

        if rs[0] == pw:
            print('로그인성공')
            login=True
            login_id=c_id
        else:
            print('로그인실패')
            login=False

        conn.close()

    elif a==2:
        conn = pymysql.connect(host='192.168.119.3',port=4567, user='root', password='data1234',db='bookstore', charset='utf8')

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
        conn = pymysql.connect(host='192.168.119.3',port=4567, user='root', password='data1234',db='bookstore', charset='utf8')

        curs = conn.cursor()
        sql ='select * from Customer '
        curs.execute(sql)
        rows=curs.fetchall()
        for row in rows:
            print(row)
        conn.commit()
        conn.close()

    elif a==4:
        conn = pymysql.connect(host='192.168.119.3',port=4567, user='root', password='data1234',db='bookstore', charset='utf8')

        curs = conn.cursor()
        print('검색 종목 1. id 2. name 3. phone_number 4. address 5. password')
        b=int(input())
        if b==1:
            print('id:')
            c_id=input()
            sql ='select * from Customer where id=%s'
            curs.execute(sql,(c_id))
            rows=curs.fetchall()
            for row in rows:
                print(row)
        elif b==2:
            print('name:')
            name=input()
            sql ='select * from Customer where name=%s'
            curs.execute(sql,(name))
            rows=curs.fetchall()
            for row in rows:
                print(row)
        
        elif b==3:
            print('phone_number:')
            phone_number=int(input())
            sql ='select * from Customer where phone_number=%s'
            curs.execute(sql,(phone_number))
            rows=curs.fetchall()
            for row in rows:
                print(row)

        elif b==4:
            print('address:')
            address=input()
            sql ='select * from Customer where address=%s'
            curs.execute(sql,(address))
            rows=curs.fetchall()
            for row in rows:
                print(row)

        elif b==5:
            print('password:')
            password=input()
            sql ='select * from Customer where password=%s'
            curs.execute(sql,(password))
            rows=curs.fetchall()
            for row in rows:
                print(row)
        conn.commit()
        conn.close()
    elif a==5:
        conn = pymysql.connect(host='192.168.119.3',port=4567, user='root', password='data1234',db='bookstore', charset='utf8')
        if login==False:
            print('로그인 먼저 하고 오 십시오')
        
        else:
            curs = conn.cursor()
            print('id:%s'%login_id)

            sql ='delete from Customer where id=%s'
            curs.execute(sql,(login_id))
            conn.commit()
            login_id=''
        conn.close()

    elif a==6:
        sql = "select * from Customer"
        curs.execute(sql)    

    elif a==7:
        conn = pymysql.connect(host='192.168.119.3',port=4567, user='root', password='data1234',db='bookstore', charset='utf8')

        curs = conn.cursor()
        print('책 검색 종목 1. book_num 2. author 3. book_name 4. stock 5. price 6. publisher')
        b=int(input())
        if b==1:
            print('book_num:')
            book_num=int(input())
            sql ='select * from Book where book_num=%s'
            curs.execute(sql,(book_num))
            rows=curs.fetchall()
            for row in rows:
                print(row)
                sql ='INSERT into Search values(%s,%s,%s)'
                curs.execute(sql,(rows[0],login_id,book_num))
                conn.commit()

        elif b==2:
            print('author:')
            author=input()
            sql ='select * from Book where author=%s'
            curs.execute(sql,(author))
            rows=curs.fetchall()
            for row in rows:
                print(row)
                sql ='INSERT into Search values(%s,%s,%s)'
                curs.execute(sql,(rows[0],login_id,author))
                conn.commit()
        
        elif b==3:
            print('book_name:')
            book_name=int(input())
            sql ='select * from Book where book_name=%s'
            curs.execute(sql,(book_name))
            rows=curs.fetchall()
            for row in rows:
                print(row)
                sql ='INSERT into Search values(%s,%s,%s)'
                curs.execute(sql,(rows[0],login_id,book_name))
                conn.commit()

        elif b==4:
            print('stock:')
            stock=input()
            sql ='select * from Book where stock=%s'
            curs.execute(sql,(stock))
            rows=curs.fetchall()
            for row in rows:
                print(row)
                sql ='INSERT into Search values(%s,%s,%s)'
                curs.execute(sql,(rows[0],login_id,stock))
                conn.commit()

        elif b==5:
            print('price:')
            price=int(input())
            sql ='select * from Book where price=%s'
            curs.execute(sql,(price))
            rows=curs.fetchall()
            for row in rows:
                print(row)
                sql ='INSERT into Search values(%s,%s,%s)'
                curs.execute(sql,(rows[0],login_id,price))
                conn.commit()
        elif b==5:
            print('publisher:')
            publisher=input()
            sql ='select * from Book where publisher=%s'
            curs.execute(sql,(publisher))
            rows=curs.fetchall()
            for row in rows:
                print(row)
                sql ='INSERT into Search values(%s,%s,%s)'
                curs.execute(sql,(rows[0],login_id,publisher))
                conn.commit()
        conn.close()

    elif a==8:
        conn = pymysql.connect(host='192.168.119.3',port=4567, user='root', password='data1234',db='bookstore', charset='utf8')

        curs = conn.cursor()
        print('book_num:')
        book_num=int(input())
        print('author:')
        author=input()
        print('book_name:')
        book_name=input()
        print('publisher:')
        publisher=input()
        print('stock:')
        stock=input()
        print('price:')
        price=input()

        sql ='insert into Customer values(%s,%s,%s,%s,%s,%s)'
        curs.execute(sql,(book_num,author,book_name,publisher,stock,price))
        conn.commit()

        
        conn.close()




    # 데이타 Fetch

        # 전체 rows
    # print(rows[0])  # 첫번째 row: (1, '김정수', 1, '서울')
    # print(rows[1])  # 두번째 row: (2, '강수정', 2, '서울')
    
    # Connection 닫기
