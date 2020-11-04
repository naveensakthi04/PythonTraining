import json


class JsonData:

    def get_status(self):
        with open("gateways.json", "r+") as f:
            content = json.load(f)
            return list(list(content.items())[0][1].items())[0][1].get("status")

    def update_status(self, arg):
        try:
            with open("gateways.json", "r+") as f:
                content = json.load(f)
                temp1 = list(content.items())[0][0]
                temp2 = list(list(content.items())[0][1].items())[0][0]
                content.get(temp1).get(temp2).update({"status" : arg})


            with open("gateways.json", "w+") as f:
                json.dump(content, f)
        except Exception:
            print("Something went wrong!")


# Driver code
obj = JsonData()
choice = input("1. Get status\n2. Update Status\nEnter your choice:  ")
if choice == "1":
    status = obj.get_status()
    print(status)
elif choice == "2":
    status = input("status: ")
    obj.update_status(status)
    print("Success")
