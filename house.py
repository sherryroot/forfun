import math
import csv
#A是每期打入的钱
#year是贷款的年限
#r是年利率 本文设置的是0.03
class House_invest():
    def __init__(self,A,B,X,year):
        self.A=A#房子标价
        self.B=B#首付
        self.X=X#租售比
        self.year=year#贷款年限



    def get_pv(self,a):#得到后面每一期的现值
        temp=[]
        i=1
        r=0.03
        rate=1/(1+r)
        while(i<=self.year):
            pv_i=math.pow(rate,i)*a
            i=i+1
            temp.append(pv_i)
        return temp

    def sum_pv(self,temp):#所有现值进行总和
        sum=0
        for i in temp:
            sum=sum+i
        return sum

    def get_loan(self):#这套房子每个月要还的贷款
        m_loan=(self.A-self.B)
        rate = 0.049/12
        #等额本息：〔贷款本金×月利率×（1＋月利率）＾还款月数〕÷〔（1＋月利率）＾还款月数－1〕
        num=self.year*12
        loan=m_loan*rate*pow((1+rate),num)/(pow((1+rate),num)-1)

        return loan

    def real_value(self):
        year=self.year
        loan=House_invest.get_loan(self)
        rent=self.A/self.X
        cost=self.B*0.03
        pv_loan=House_invest.get_pv(self,loan)
        pv_rent=House_invest.get_pv(self,rent)
        pv_cost=House_invest.get_pv(self,cost)
        #print(pv_rent)
        #print(pv_loan)
        real_price=self.B+sum(pv_loan)-sum(pv_rent)
        money=self.A-real_price-sum(pv_cost)#投资价值=市场价格-实际该项目的现值-首付这笔钱的沉没成本
        print(sum(pv_cost))
        return money


if __name__=='__main__':

    i=1
    A=1700000
    B=1000000
    X=300
    Y=30
    temp_a=[]
    temp_b=[]
    temp_x=[]
    temp_y=[]
    while(i<=10):
        i=i+1
        A=A+500000
        B=B-50000
        X=X+20
        Y=Y-2
        temp_a.append(A)
        temp_b.append(B)
        temp_x.append(X)
        temp_y.append(Y)
    with open('/Users/sherry/Desktop/test.csv', 'w') as csvfile:
        writer=csv.writer(csvfile)
        #贷款时间和我们价值的关系
        var_a=1700000
        var_b=1000000
        var_y=10
        var_x =500
        result=[]
        print(temp_a)
        for var_a in temp_a:
            b = House_invest(var_a, var_b, var_x, var_y)
        #    #print("现在的结果是")
        #    #print(b.real_value())
            result.append(b.real_value())
        writer.writerow(result)

        #print(result)
        #b = House_invest(var_a, var_b, var_x, var_y)
        print(b.real_value())





