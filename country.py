countries = ["brazil", "argentina"]

country = input("Enter a country name: ").lower()

if country in countries:
    print("We have visited that country")
else :
    print("We have NOT visited that country yet")