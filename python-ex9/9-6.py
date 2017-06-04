def main():
    f1 = open("test1.txt",'r')  
    f2 = open("test2.txt",'r')  
    row = 0 
    for (line1,line2) in zip(f1,f2):  
        row += 1  
        if line1 == line2:  
            pass  
        else:  
            col = 0;  
            print row 
            for (a,b) in zip(line1,line2):  
                if a == b:  
                    col += 1  
                else:  
                    print col,  
    f1.close()  
    f2.close()
    
if __name__ == "__main__":
    main()