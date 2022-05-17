from crypt import methods
from flask import Flask, jsonify, request
import json
import uuid

app = Flask(__name__)

# Main Route
@app.route("/")
def main():
  return Purchase.get("1202929")

 
# All purchases Route
@app.route("/api/purchases", methods=["GET"])
def allPurchases():
  return AllPurchases.get()

# Single Purchase Route
@app.route("/api/purchase/<id>", methods=["GET"])
def getPurchase(id):
  return Purchase.get(id)

# Add Purchase Route
@app.route("/api/purchases", methods=["POST"])
def addPurchase():
  newPurchase = jsonify(request.json)
  return AllPurchases.add(newPurchase.name, newPurchase.description, newPurchase.price)

# Delete Purchase Route
@app.route("/api/purchase/<id>", methods=["DELETE"])
def deletePurchase(id):
  return Purchase.delete(id)




# Purchase class
class Purchase():
  # Get Purchase
  def get(purchaseId):
    with open("purchases.json", "r") as f:
      allPurchases = json.load(f)
    return jsonify(allPurchases[purchaseId])

  # Delete Purchase
  def delete(purchaseId):
    with open("purchases.json", "r") as f:
      allPurchases = json.load(f)
      del allPurchases[purchaseId]
      
    with open("purchases.json", "w") as r:
      json.dump(allPurchases, r)
      return jsonify({"Message": "Deleted Succesfully"})

class AllPurchases():
  def get():
    with open("purchases.json", "r") as f:
      allPurchases = json.load(f)      
      return jsonify(allPurchases)
  
  def add(name, description, price):
    with open("purchases.json", "r") as f:
      allPurchases = json.load(f)
      randomId = 33
      allPurchases[randomId] = {name: name, description: description, price: price}
    
    with open("purchases.json", "w") as r:
      json.dump(allPurchases, r)
      return "Succesfully Added Purchase"

    



if __name__ == "__main__":
  app.run(port=3000,debug=True)