import mysql.connector 
def add_file_to_liste(liste, path_file,file):
    with open(path_file+file,'r') as f:
        for line in f:
            for Word in line.split():
                Word = Word.replace('.','')
                Word = Word.replace('!','')
                Word = Word.replace(':','')
                Word = Word.replace('(','')
                Word = Word.replace(')','')
                Word = Word.replace('?','')
                Word = Word.replace(',','')
                liste.append(Word)

def filtered_in_len_tow(liste):
    list_filtre = []
    for x in liste:
        if(len(x) > 2):
            list_filtre.append(x)
    return list_filtre

def filtered_with_liste_vide(liste , liste_empty_words):
    for i in liste_empty_words :
        for j in liste : 
            if j.lower() == i:
                liste.remove(j)
    return liste   

def remove_occur_from_list(liste):
    hey = []
    for x in range(len(liste)):
        hey.append((liste[x],liste.count(liste[x])))  
    liste = list(set(hey))
    return liste 

def display_list(liste):
    i = 0
    for x in liste:
        print(i,x)
        i +=1

def insert_to_bd(mydb,liste,file):
    mycursor = mydb.cursor()
    for words in liste:
        mycursor.execute("INSERT INTO liste_mots (words,number_of_words,file_name) VALUES (%s,%s,%s)",(words[0],words[1],file))
    mycursor.execute("Commit")

def delete_to_bd(mydb):
    mycursor = mydb.cursor()
    mycursor.execute("DELETE FROM liste_mots")
    mycursor.execute("Commit")

def display_in_bd(mydb):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM liste_mots")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def check_in_bd(mydb,mots):
    mycursor = mydb.cursor()
    sql = "SELECT * file_name FROM liste_mots WHERE words = %s"
    adr = (mots, )
    mycursor.execute(sql, adr)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)



def main():
    mydb = mysql.connector.connect(
        host="localhost",
        user="python3",
        password="python3",
        database="File"
    )
    path_file = "./file/"
    file_texte = "texte.txt"
    file_confience = "confience.txt"
    file_hypermedia = "hypermedia.txt"
    file_informatique = "informatique.txt"
    file_prenoms = "prenoms.txt"
    file_words_empty = "mots_vides.txt"
    liste1 =[];liste2 =[];liste3 =[];liste4 =[]
    liste5 =[];liste_empty_words =[]

    add_file_to_liste(liste1, path_file ,file_texte)
    add_file_to_liste(liste2, path_file ,file_confience)
    add_file_to_liste(liste3, path_file ,file_hypermedia)
    add_file_to_liste(liste4, path_file ,file_informatique)
    add_file_to_liste(liste5, path_file ,file_prenoms)

    add_file_to_liste(liste_empty_words, path_file,file_words_empty)

    liste1 = filtered_in_len_tow(liste1)
    liste2 = filtered_in_len_tow(liste2)
    liste3 = filtered_in_len_tow(liste3)
    liste4 = filtered_in_len_tow(liste4)
    liste5 = filtered_in_len_tow(liste5)

    filtered_with_liste_vide(liste1 , liste_empty_words)
    filtered_with_liste_vide(liste2 , liste_empty_words)
    filtered_with_liste_vide(liste3 , liste_empty_words)
    filtered_with_liste_vide(liste4 , liste_empty_words)
    filtered_with_liste_vide(liste5 , liste_empty_words)
   
    liste1 = remove_occur_from_list(liste1)
    liste2 = remove_occur_from_list(liste2)
    liste3 = remove_occur_from_list(liste3)
    liste4 = remove_occur_from_list(liste4)
    liste5 = remove_occur_from_list(liste5)
  
    display_list(liste1)
    
    insert_to_bd(mydb,liste1,file_texte)
    insert_to_bd(mydb,liste2,file_confience)
    insert_to_bd(mydb,liste3,file_hypermedia)
    insert_to_bd(mydb,liste4,file_informatique)
    insert_to_bd(mydb,liste5,file_prenoms)
    #delete_to_bd(mydb)
    display_in_bd(mydb)
    #check_in_bd(mydb,'pages')
if __name__ == '__main__':
    main()
