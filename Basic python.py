# -*- coding: utf-8 -*-

"""

Created on Thu Feb 22 15:59:59 2018

 

@author: trupti.patel01

"""

from collections import Counter,defaultdict

Users=[{"id":0,"name":"Hero"},

       {"id":1,"name":"Dunn"},

       {"id":2,"name":"Sue"},

       {"id":3,"name":"Chi"},

       {"id":4,"name":"Thor"},

       {"id":5,"name":"Clive"},

       {"id":6,"name":"Hicks"},

       {"id":7,"name":"Devin"},

       {"id":8,"name":"Kate"},

       {"id":9,"name":"Klein"}

 

      ]

friendship=[(0,1),(0,2),(1,2),(1,3),(2,3),(3,4),(4,5),(5,6),(5,7),(6,8),(7,8),(8,9)]

 

for user in Users:

    user["Friends"]=[]

 

for i,j in friendship:

    Users[i]["Friends"].append(Users[j])

    Users[j]["Friends"].append(Users[i])

def  number_of_friends(user):

    return len(user["Friends"])

 

total_connections =sum(number_of_friends(user) for user in Users)

print("Total connections :",total_connections)

avg_connection=total_connections/len(Users)

print("Avarage connections :",avg_connection)

print("**************************************************")

#For finding people who have largest number of friends and leaste number of friedns

 

my_total_friends=[(user["id"],number_of_friends(user)) for user in Users]

 

 

my_total_friends.sort(key=lambda x:x[1],reverse=True)

print("person who has largest number of connection to least number of connection by user id:")

print(my_total_friends)

print("**************************************************")

def not_the_same(user,other_user):

    return user["id"] != other_user["id"]

 

def not_friend(user,other_user):

    return all(not_the_same(friend,other_user)

               for friend in user["Friends"])

   

def mutual_friends(user):

    return Counter( foaf["id"]

       for friend in user["Friends"]

       for foaf in friend["Friends"]

       if not_the_same(user,foaf)

       and not_friend(user,foaf))

 

print("user's mutual connections :")

print(mutual_friends(Users[0]))

print("**************************************************")

 

 

interests=[(0,"Hadoop"),(0,"Big Data"),(0,"HBase"),(0,"Java"),(0,"Spark"),(0,"Strom"),

           (0,"Cassandra"),(1,"NoSQL"),(1,"MongoDB"),(1,"Cassandra")

           ,(1,"HBase"),(1,"Postgres"),(2,"Python"),(2,"scikit-learn"),

           (2,"scipy"),(2,"numpy"),(2,"statsmodels"),(2,"Pandas"),(3,"R")

           ,(3,"Python"),(3,"statistic"),(3,"regression"),(3,"probablity")

           ,(4,"machine learning"),(4,"regression"),(4,"decesion trees"),

           (4,"libsvm"),(5,"Python"),(0,"R"),(5,"Java"),(5,"C++"),(5,"haskell"),

           (5,"Programming languages"),(6,"statistic"),(6,"probablity"),(6,"mathematics"),

           (6,"theory"),(7,"machine learning"),(7,"scikit-learn"),(7,"mahout"),

           (7,"neural networks"),(8,"neural networks"),(8,"deep learning"),(8,"Big Data"),

           (8,"artificial intelligence"),(9,"Hadoop"),(9,"Java"),(9,"MapReduce"),(9,"Big Data")]

 

 

def User_with_interest(target_interest):

    return [user_id

            for user_id,user_interest in interests

            if user_interest == target_interest]

   

print("User which are interested in Hadoop")   

print(User_with_interest("Hadoop"))

print("**************************************************")

#defaultdic is work same as normal dict but only diff is value fields data type is specified upon  initialization

#user id by interest

print("list of users in particulat interest")

User_id_by_interest=defaultdict(list)

 

for user_id,user_interest in interests:

    User_id_by_interest[user_interest].append(user_id)

   

print(User_id_by_interest)

 

#interest by userid

interest_by_userid=defaultdict(list)

 

for user_id,user_interest in interests:

    interest_by_userid[user_id].append(user_interest)

print("**************************************************")

print("list of interests based on user id")

print(interest_by_userid)

 

print("**************************************************")

def most_common_interest_with(user):

    return Counter(interested_userid

                   for interest in interest_by_userid[user["id"]]

                   for interested_userid in User_id_by_interest[interest]

                   if interested_userid != user["id"])

print("who has most common interest with given user")

print(most_common_interest_with(Users[0]))

 

print("**************************************************")

 

salaries_and_tenures=[(83000,8.7),(88000,8.1),

                      (48000,0.7),(76000,6),

                      (69000,6.5),(76000,7.5),

                       (60000,2.5),(83000,10),

                      (48000,1.9),(63000,4.2)]

 

def tenure_bucket(tenure):

    if tenure<2:

        return "less than 2"

    elif tenure<5:

        return "between 2 and 5"

    else:

        return "more than 5"

 

salary_by_tenure_bucket=defaultdict(list)

for salary,tenure in salaries_and_tenures:

    bucket=tenure_bucket(tenure)

    salary_by_tenure_bucket[bucket].append(salary)

   

print("salary bucket wise:")  

avarage_salary_by_bucket={

        tenure_bucket:sum(salaries)/len(salaries)

        for tenure_bucket,salaries in salary_by_tenure_bucket.items()

        }   

print(avarage_salary_by_bucket)

print("**************************************************")