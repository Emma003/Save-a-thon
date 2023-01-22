
current_profile = None
discordID = None
name = None
salary = None
utility_bills = None
transport = None
housing = None
budget_plan = None

def new_profile(messageArr, user_id):
    global name, discordID

    discordID = user_id
    name = messageArr[1]
    return "`enter $record_income <monthly_income> to add your monthly income`"


# mycursor.execute("ALTER TABLE test_table ADD COLUMN age INT")
# mycursor.execute("INSERT INTO test_table (name, salary) VALUES (%s,%s)", ("emma", 5000))
# mycursor.execute("SELECT name, salary FROM goals")
# db.commit()

# myres = mycursor.fetchone()
# print(myres)
# mycursor.execute("SHOW TABLES")
# mycursor.execute("DESCRIBE profiles")
#
# for x in mycursor:
#     print(x)