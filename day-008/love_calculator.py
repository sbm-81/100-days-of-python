def calculate_love_score(name1,name2):
    name=name1+name2
    # print(name)
    text_name=name.lower()
    # print(text_name)
    total=0
    total_love=0
    
    loop_c=len(text_name)
    while loop_c!=0:
        loop_c-=1
        if ('t' in text_name[loop_c]) or ('r' in text_name[loop_c]) or ('u' in text_name[loop_c]) or ('e' in text_name[loop_c]):
            
            total+=1
            # print("Found letter:", text_name[loop_c], "total: ", total)

    loop_c=len(text_name)
    # print("total love calculation")
    while loop_c!=0:
        loop_c-=1
        if ('l' in text_name[loop_c]) or ('o' in text_name[loop_c]) or ('v' in text_name[loop_c]) or ('e' in text_name[loop_c]):
            
            total_love+=1
            # print("Found letter:", text_name[loop_c], "total: ", total_love)
       
    love_score=total*10+total_love     
    # print("love score: ", love_score)
    print(love_score)

    
    
calculate_love_score("Angela Yu", "Jack Bauer")