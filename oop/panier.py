#Define a class called Panier that represents a shopping cart
class Panier:
    #initialize the Panier with an empty
    def __init__(self):
        self.articles = []
    

    #Define a fxn to add articles to our parnier
    def ajouter(self,nom_article, prix):
        article = (nom_article, prix)
        self.articles.append(article)

    #Define the fxn to delete
    def supprimer(self, nom_article):
        for article in self.articles:
            if article[0] == nom_article:
                self.articles.remove(article)
                break
    
    #Calculate and return total price
    def Cal_total(self):
        total = 0
        for article in self.articles:
            total += article[1]
        return total
    

pan = Panier()

#Ajouter les article
pan.ajouter("Orange", 100)
pan.ajouter("Spaghetti", 400 )
pan.ajouter("Fromage", 50 )

#Affiche les article dan le panier'
print('Article dans le Panier')
for article in pan.articles:
    print(article[0], "-", article[1])


#Calculate the total
prix_total = pan.Cal_total()
print("Le Prix total:", prix_total)

#Supprimer un article
pan.supprimer("Orange")
print("\n Nouveua Panier:")
for article in pan.articles:
    print(article[0], "-", article[1])

prix_total = pan.Cal_total()
print("Total Quantity: ", prix_total)

#Finished
