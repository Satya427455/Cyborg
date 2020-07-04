item_no=0
order=[]
item=[]
price=[]
item_type=[]
class food():
    global order
    global item
    global item_no
    global item_type
    all_ingredients={"pizza crust": 1,"cheese": 0.8,"ham": 0.8,"pineapple":0.5,"meatball": 1,"bacon":0.7,"mushroom":1,"olives":1.5,"spaghetti": 1,"tomatoes":0.7,"pepporoni":0.7,"parsley":0.8}
    def __init__(self):
        pass
    def determine_item_no(self):
        global item_no
    def determine_item(self):
        for i in range(0,item_no):
            if 'pizza crust' in order[i]:
                item.append("pizza")
            else:
                item.append("pasta")
    def determine_item_type(self):
        for j in range(0,item_no):
            if 'ham'or 'bacon'or 'meatball' or 'pepporoni' in order[j]:
                item_type.append("non-veg")
            else:
                item_type.append("veg")
    def determine_price(self):
        global price     
        for k in range(0,item_no):
            cost = 0
            for ingredient in order[k]:
               cost = cost+self.all_ingredients[ingredient]
               price.append(cost)            
class pizza(food):
    ingredients = {"pizza crust": 1,"cheese": 0.8,"ham": 0.8,"pineapple":0.5,"meatball": 1,"bacon":0.7,"mushroom":1,"olives":1.5}
    base_ingredients = ["pizza crust","cheese"]
    def __init__(self):
        pass
    def predefined_pizza(self):
        global order
        global item_no
        a1= int(input("1.Mexican\n2.Spice heaven\n"))
        if a1==1:
            order.append(["pizza crust","cheese","ham","olives"])
            item_no = item_no+1
        elif a1==2:
            order.append(["pizza crust","cheese","meatball","bacon"])
            item_no=item_no+1
        else:
            print("Please enter a valid option!")
            pizza.predefined_pizza(self)
        menu()
    def custom_pizza(self):
        global order 
        global item_no
        wish=""
        wish_final=[]
        new_wish=[]
        wish=input("What are the ingredients you wish to add?? \n1.ham\n2.pineapple\n3.meatball\n4.bacon\n5.mushroom\n6.olives")
        wish_final=wish.split( )
        new_wish.extend(self.base_ingredients)
        for i in wish_final:
            if i in self.ingredients:
                if i in new_wish:
                    print("You have added the items more than once")
                    pizza.custom_pizza(self)
                else:
                    new_wish.append(i)
            else:
                print("Select a valid add on")
                pizza.custom_pizza(self)
            print(new_wish)
            if new_wish!=["pizza crust","cheese"]:
                item_no=item_no+1
                order.append(new_wish)
            print(order)    
class pasta(food):
    ingredients_pasta = {"spaghetti": 1,"cheese": 0.8,"ham": 0.8,"tomatoes":0.7,"meatball": 1,"pepporoni":0.7,"mushroom":1,"parsley":0.8}
    base_ingredients_pasta = ["spaghetti","cheese"]
    def __init__(self):
        pass
    def predefined_pasta(self):
        global order
        global item_no
        wish1= int(input("1.Sweet Cream pasta\n2.Silican pasta\n"))
        if wish1==1:
            order.append(["spaghetti","cheese","meatball","tomatoes"])
            item_no+=item_no+1
        elif wish1==2:
            order.append(["spaghetti","cheese","pepporoni","parsley"])
            item_no=item_no+1
        else:
            print("Select a valid option")
            pizza.predefined_pizza(self)
        menu()
    def custom_pasta(self):
        global order
        global item_no
        wish2=""
        wish2_final=[]
        new_buy=[]
        wish2=input("What are the ingredients you wish to add?? \n1.ham\n2.tomatoes\n3.meatballs\n4.pepporoni\n5.mushroom\n6.parsley")
        wish2_final=wish2.split( )
        for i in  wish2_final:
            if i in self.ingredients_pasta:
                if i in new_buy:
                    new_order = []
                    new_order.extend(self.base_ingredients_pasta)
                    print( "You added same ingredient twice.Please enter the ingredients again.")
                    pasta.custom_pasta(self)
                else:
                    new_order.append(i)
            else:
                print("Please enter a valid add-on.")
                pasta.custom_pasta(self)
        print(new_order)
        if new_order != ["spaghetti","cheese"]:
            item_no=item_no+1
            order.append(new_order)
        print(order)
        menu()

def menu():
    print("******menu******")
    a=int(input("How can I help you?\n1.Order a new pizza\n2.Order a new a new pasta\n3.Show your order"))
    if a==1:
        user_wish_pizza=int(input("Which type of pizza you want you order?\n1.Predefined pizza\n2.Custom pizza"))
        if user_wish_pizza==1:
            piz.predefined_pizza()
        elif user_wish_pizza==2:
            piz.custom_pizza()
        else:
            print("Enter a valid option")
    elif a==2:
        user_wish_pasta=int(input("Which type of pasta you want you order?\n1.Predefined pasta\n2.Custom pasta"))
        if user_wish_pasta==1:
            pas.predefined_pasta()
        elif user_wish_pasta==2:
            pas.custom_pasta()
        else:
            print("Enter a valid option")
    elif a==3:
        summary()
    else:
        print("Please enter a valid option")
        menu()
        
def summary():
    global item_no
    total_food.determine_item()
    total_food.determine_item_type()
    total_food.determine_price()
    i=0
    for i in range (0,item_no):
        print("item",i+1,"is", item_type[i], item[i])
        print("It has", order[i])
        print("Cost:",price[i])
    print("Total number of items bought:", item_no)
    print("Total amount:", sum(price))
    
       
piz=pizza()
pas=pasta()
total_food=food()   
menu()
 
        
        
            
        
    
              
    
         
                    
                
                
                
            
        
        
        
        
    
    
    